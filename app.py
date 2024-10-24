from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/")
def welcome():
    return "hello world"

from controller import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.',port=5001)

#mvc - model view architecture