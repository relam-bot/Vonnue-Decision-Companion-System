from flask import Flask, render_template, request, jsonify
from src.conversation_manager import ConversationManager

app = Flask(__name__)

manager = ConversationManager()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = manager.process_input(user_input)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)