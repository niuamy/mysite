from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

mail_settings ={
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": "FILL IN",
    "MAIL_PASSWORD": "FILL IN"
}

app.config.update(mail_settings)
mail = Mail(app)


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
    with app.app_context():
        friendMSG = request.form.get("friendMessage")
        msgBody = str(friendMSG)
        msg = Message(subject="A Friend Wants to Meet Up!", sender="FILL IN", recipients=["FILL IN"],body=msgBody)
        mail.send(msg)
    return render_template("friend.html")

if __name__ == '__main__':
    app.run(debug=True)
