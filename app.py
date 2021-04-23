from flask import Flask, jsonify , request
from flask_cors import CORS
import random
from main import Main

app = Flask(__name__)
CORS(app)

main = Main()

@app.route('/')
def hello_world():
    return jsonify('Hello World!')


@app.route('/random' , methods=["GET"])
def getRandomNumbers():
    num = []
    for x in range(10):
        num.append(random.randint(0,500))
    return jsonify(num)


@app.route("/sendMsg" , methods=["POST"])
def sendMessage():
    data = request.get_data().decode('utf-8')
    data = data.split(",")
    main.addMessage(data[0] , data[1])
    return jsonify(main.getMessages())

@app.route("/getMessages" , methods=["GET"])
def getMessages():
    return jsonify(main.getMessages())

if __name__ == '__main__':
    app.run()
