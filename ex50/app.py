from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    greeting = "Hello World"
    return render_template("index.html", greeting=greeting)

@app.route("/foo")
def foo():
    name = "Dima"
    return render_template("foo.html", master=name)

if __name__ == "__main__":
    app.run()