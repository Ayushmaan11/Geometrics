from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("authentication/login.html")

@app.route("/register")
def register():
    return render_template("authentication/register.html")


if __name__ == '__main__' :
    app.run(host='0.0.0.0',debug=True,use_reloader=True,reloader_type="stat")

