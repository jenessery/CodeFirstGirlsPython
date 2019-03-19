from flask import Flask, render_template, request
from horoscopeapi import get_horoscope, zodiac_sign

app = Flask("MyApp")

def calcgen(year):
    import datetime
    today = datetime.datetime.now()
    if year> today.year:
        raise Exception("Year of birth cannot be in the future.")
    elif year>1995:
         gen = "Gen Z"
    elif year>1976:
        gen = "Gen Y"
    elif year>1965:
        gen = "Gen X"
    elif year<1900:
        raise Exception("Year of birth cannot be prior to 1900.")
    else:
        gen = "an unknown generation"
    return gen

@app.route("/")

def default():
    return render_template("index.html", name="Internet Stranger")

@app.route("/welcome")

def welcome():
    return "Welcome World"

@app.route("/<name>")
def hello_someone(name):
    return render_template("index.html", name=name.title())

@app.route("/yourgeneration",methods=["POST"])
def showgeneration():
    form_data = request.form
    year = form_data["year"]
    try:
        return render_template("gen.html", gen=calcgen(int(year)).title(), year=year)
    except:
        return "Please input a valid year."

@app.route("/horoscope",methods=["POST"])
def showhoroscope():
    form_data = request.form
    day = form_data["day"]
    month = form_data["month"]
    data = get_horoscope(zodiac_sign(int(month),int(day)))
    try:
        return render_template("horoscope.html", data=data, day=day, month=month)
    except:
        return "Please input a valid day & month."

app.run(debug=True)
