from flask import Flask, render_template

app = Flask("MyApp")

@app.route("/")

def hello():
    return "Hello World"

@app.route("/welcome")

def welcome():
    return "Welcome World"

@app.route("/<name>")
def hello_someone(name):
    return render_template("index.html", name=name.title())

app.run(debug=True)
