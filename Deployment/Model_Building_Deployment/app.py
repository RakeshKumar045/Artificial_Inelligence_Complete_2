import pickle

# from sklearn.externals import joblib
import joblib
import pandas as pd
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/model_building', methods=['GET'])
def model_building():
    print("start")
    df = pd.read_csv("spam_dataset.csv")

    df_data = df[["CONTENT", "CLASS"]]
    df_x = df_data['CONTENT']
    df_y = df_data.CLASS
    # Extract Feature With CountVectorizer
    corpus = df_x
    cv = CountVectorizer()
    X = cv.fit_transform(corpus)  # Fit the Data

    # Save the Count Vectorizer
    # filename_cv = 'count_vector.pkl'
    # pickle.dump(cv, open(filename_cv, 'wb'))

    # Save the model as a pickle in a file
    joblib.dump(cv, 'count_vector_joblib.pkl')

    X_train, X_test, y_train, y_test = train_test_split(X, df_y, test_size=0.33, random_state=42)
    clf = MultinomialNB()
    clf.fit(X_train, y_train)
    # clf.score(X_test, y_test)

    # Save the Model
    # filename_model = 'raka_spam_model.pkl'
    # pickle.dump(clf, open(filename_model, 'wb'))

    joblib.dump(clf, 'raka_spam_model_joblib.pkl')

    print("Success")

    return '<h1>Spam Detection model has been built successful by Trishala! Enjoy & Party & Dance!</h1>'


@app.route('/predict', methods=['POST'])
def predict():
    # load the model from disk
    # filename_model_load = 'raka_spam_model.pkl'
    # loaded_model = pickle.load(open(filename_model_load, 'rb'))
    loaded_model = joblib.load('raka_spam_model_joblib.pkl')

    # Save the Count Vectorizer
    file_loaded_cv = 'count_vector.pkl'
    loaded_cv = pickle.load(open(file_loaded_cv, 'rb'))
    loaded_cv = joblib.load('count_vector_joblib.pkl')

    if request.method == 'POST':
        comment = request.form['comment']
        print("Comment : ", comment)

        data = [comment]

        print("data : ", data)
        vect = loaded_cv.transform(data).toarray()

        print("vector : ", vect)

        my_prediction = loaded_model.predict(vect)

        print("model prediction : ", my_prediction)

    return render_template('result.html', prediction=my_prediction)


if __name__ == '__main__':
    app.run(debug=True, port=6060)
