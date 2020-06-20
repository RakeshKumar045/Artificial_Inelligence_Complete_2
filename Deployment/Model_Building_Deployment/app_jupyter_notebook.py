# from sklearn.externals import joblib
import joblib
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    loaded_model = joblib.load('raka_spam_model_joblib_jupyter.pkl')

    # Save the Count Vectorizer
    loaded_cv = joblib.load('count_vector_joblib_jupyter.pkl')

    if request.method == 'POST':
        comment = request.form['comment']
        data = [comment]

        vect = loaded_cv.transform(data).toarray()

        my_prediction = loaded_model.predict(vect)

    return render_template('result.html', prediction=my_prediction)


if __name__ == '__main__':
    app.run(debug=True, port=6060)
