from flask import Flask

app = Flask("MyApp")

@app.route("/")

def hello():
    return "Hello World"

@app.route("/welcome")

def welcome():
    return "Welcome World"

app.run(debug=True)
