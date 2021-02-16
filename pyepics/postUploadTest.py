import os
import time

from pvaccess import *
from flask import Flask, jsonify
from flask import request
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET', 'POST'])
def get_data():
    print(request.form)
    file = request.files['file']
    print(file.filename)

    filename = secure_filename(file.filename)
    file.save(os.path.join('/home/scwook', filename))
    return 'OK'

if __name__ == "__main__":
    app.run(host="localhost", port="8080")

