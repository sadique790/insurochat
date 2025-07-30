
# app.py
from flask import Flask, request, jsonify, render_template
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_message = request.json["message"]
    bot_reply = get_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    pass
    
# app.py
from flask import Flask, request, jsonify, render_template
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_message = request.json["message"]
    bot_reply = get_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":

    app.run(debug=True)