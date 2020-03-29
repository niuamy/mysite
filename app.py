from flask import Flask, render_template, request
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Todo('{self.id}', '{self.name}', '{self.date_created}')"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello', methods=["POST"])
def hello():
    name = request.form.get("name")
    new_name = Todo(name = name)
    try:
        db.session.add(new_name)
        db.session.commit()
        return render_template("hello.html", name=name)
    except:
        return 'ERROR!'

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
        sender = app.config.get("MAIL_USERNAME")
        msg = Message(subject="A Friend Wants to Meet Up!", sender=sender, recipients=["FILL IN"],body=msgBody)
        if sender != "FILL IN":
            mail.send(msg)
    return render_template("friend.html")

@app.route('/activityLog', methods=["POST"])
def activityLog():
    people = Todo.query.all()
    return render_template("activityLog.html", people=people)

if __name__ == '__main__':
    app.run(debug=True)
