from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/random' , methods=["GET"])
def getRandomNumbers():
    num = []
    for x in range(10):
        num.append(random.randint(0,500))
    return jsonify(num)


if __name__ == '__main__':
    app.run()
