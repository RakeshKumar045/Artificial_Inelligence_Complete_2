import os

import sentry_sdk
from config import FLASK_SECRET_KEY, UPLOAD_FOLDER, LABELS, WTF_CSRF_TIME_LIMIT, SENTRY_INIT
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect, CSRFError
from processing import get_label, upload_file_to_s3, allowed_file
from sentry_sdk.integrations.flask import FlaskIntegration
from werkzeug.utils import secure_filename

# https://github.com/rowhitswami/Indian-Paper-Currency-Prediction

# Sentry Initialization
sentry_sdk.init(
    dsn=SENTRY_INIT,
    integrations=[FlaskIntegration()]
)

# Flask config
app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['WTF_CSRF_TIME_LIMIT'] = WTF_CSRF_TIME_LIMIT
CSRFProtect(app)
CORS(app)


@app.route("/", methods=["GET"])
def main():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        error = 'No Image Found!'
        return jsonify({"error": error}), 400

    file = request.files['file']
    if file.filename == '':
        error = 'No image selected for uploading'
        return jsonify({"error": error}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(os.path.join(file_path))
        uploaded = upload_file_to_s3(file_path, filename)
        if uploaded:
            predicted_labels = get_label(filename, file_path)
            if predicted_labels:
                os.remove(file_path)
                return jsonify({
                    "labels": LABELS,
                    "data": predicted_labels
                }), 200
            else:
                error = "Unable to save predictions. Please try again!"
                return jsonify({"error": error}), 500
        else:
            error = "Couldn't process and upload your image. Please try again!"
            return jsonify({"error": error}), 500
    else:
        error = 'Allowed image types are -> png, jpg, jpeg'
        return jsonify({"error": error}), 400


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return jsonify({"error": e.description + " Try refreshing the page."}), 400
