# EDA Packages

# ML Packages
# EDA Packages
import pandas as pd
from flask import Flask, render_template, request
# ML Packages
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=['POST'])
def predict():
    print("hi 1 ")
    # Link to dataset from github
    global my_prediction, comment
    url = "https://raw.githubusercontent.com/Jcharis/Machine-Learning-Web-Apps/master/Youtube-Spam-Detector-ML-Flask-App/YoutubeSpamMergedData.csv"
    df = pd.read_csv(url)
    df_data = df[["CONTENT", "CLASS"]]
    print("hi 2")
    # Features and Labels
    df_x = df_data['CONTENT']
    df_y = df_data.CLASS
    # Extract Feature With CountVectorizer
    corpus = df_x
    cv = CountVectorizer()
    X = cv.fit_transform(corpus)  # Fit the Data
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, df_y, test_size=0.33, random_state=42)
    # Naive Bayes Classifier
    from sklearn.naive_bayes import MultinomialNB
    clf = MultinomialNB()
    clf.fit(X_train, y_train)
    clf.score(X_test, y_test)
    # Alternative Usage of Saved Model
    # ytb_model = open("naivebayes_spam_model.pkl","rb")
    # clf = joblib.load(ytb_model)

    print("hi 4")

    if request.method == 'POST':
        comment = request.form['comment']
        print("comment : ", comment)
        data = [comment]
        print("data : ", data)
        vect = cv.transform(data).toarray()
        print("vector : ", vect)
        my_prediction = clf.predict(vect)
        print("prediction : ", my_prediction)
    return render_template('results.html', prediction=my_prediction, comment=comment)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
