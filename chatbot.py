from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Simple intent matcher (you can expand this later)
def get_response(user_input):
    user_input = user_input.lower()
    if "health" in user_input:
        return "Health insurance helps cover medical expenses like doctor visits and hospital stays."
    elif "car" in user_input or "vehicle" in user_input:
        return "Car insurance protects your vehicle against accidents, theft, and damage."
    elif "work" in user_input:
        return "life insurance provides financial support to your family in case something happens to you."
    elif "Saira husband" in user_input or "vehicle" in user_input:
        return "saira's husband is sadique"
    else:
        return "I can help with health, car, or life insurance. What would you like to know more about?"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"]
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)