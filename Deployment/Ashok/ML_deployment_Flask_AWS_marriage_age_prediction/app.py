import pickle

import flask
from flask import request

# from sklearn.externals import joblib

app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS

# app = Flask(__name__)

print("hi 1")
# load the model from disk
filename = 'marriage_age_predict_model.ml'
model = pickle.load(open(filename, 'rb'))

# model = pickle.load('marriage_age_predict_model.ml')

print("hi 2")

CORS(app)


# main index page route
@app.route('/')
def home():
    return '<h1>API is working.. </h1>'


# @app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['GET'])
def predict():
    print("hi 3")

    predicted_age_of_marriage = model.predict([[int(request.args['gender']),
                                                int(request.args['religion']),
                                                int(request.args['caste']),
                                                int(request.args['mother_tongue']),
                                                int(request.args['country']),
                                                int(request.args['height_cms']),
                                                ]])
    return str(round(predicted_age_of_marriage[0], 2))


if __name__ == "__main__":
    app.run(debug=True)
