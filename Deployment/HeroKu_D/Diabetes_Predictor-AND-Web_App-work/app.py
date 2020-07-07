import pickle

import numpy as np
from flask import Flask, render_template, request

model = pickle.load(open("diabetes.pkl", 'rb'))

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    try:
        if request.method == "POST":
            preg = float(request.form['pregnancies'])
            glucose = float(request.form['glucose'])
            bp = float(request.form['bloodpressure'])
            st = float(request.form['skinthickness'])
            insulin = float(request.form['insulin'])
            bmi = float(request.form['bmi'])
            dpf = float(request.form['dpf'])
            age = float(request.form['age'])

            l = [preg, glucose, bp, st, insulin, bmi, dpf, age]
            l = np.asarray(l)
            l = np.reshape(l, (1, 8))
            # l = preprocessing.scale(l)
            pred = model.predict(l)

            return render_template("result.html", prediction=pred[0])
    except:
        return render_template("result.html", no_value=1)


if __name__ == '__main__':
    app.run(debug=True)
