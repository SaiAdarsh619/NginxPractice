from flask import Flask, render_template
from flask import request, jsonify
from flask_cors import CORS

import os

app = Flask(__name__, template_folder='./')
CORS(app,)

@app.route("/")
def index():
    return render_template('getfile.html')

@app.route("/uploadfile", methods=["POST"])
def receive_data():
    if 'file' not in request.files:
        return jsonify({'message': 'file not sent'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'message': 'no file selected'}), 400

    # Ensure the uploads directory exists
    if not os.path.exists('./uploads'):
        os.makedirs('./uploads')

    file.save("./uploads/" + file.filename)
    return jsonify({'message': 'file saved successfully'}), 200

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
