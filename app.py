from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/")
def welcome():
    return "hello world"

from controller import *

if __name__ == '__main__':
    app.run(debug=True)

#mvc - model view architecture