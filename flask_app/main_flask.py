from flask import Flask, render_template

app = Flask("MyApp")

@app.route("/")

def default():
    return render_template("index.html", name="Internet Stranger")

@app.route("/welcome")

def welcome():
    return "Welcome World"

@app.route("/<name>")
def hello_someone(name):
    return render_template("index.html", name=name.title())

@app.route("/gen",methods=["POST"])
def thankyou():
    return "Thank you for your entry"

app.run(debug=True)
