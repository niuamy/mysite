from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello', methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)

@app.route('/welcomeRecruiter', methods=["POST"])
def welcomeRecruiter():
    return render_template("welcomeRecruiter.html")

@app.route('/welcomeFriend', methods=["POST"])
def welcomeFriend():
    return render_template("welcomeFriend.html")

@app.route('/friend', methods=["POST"])
def friend():
    return render_template("friend.html")
