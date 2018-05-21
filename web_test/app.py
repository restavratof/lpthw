from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    greeting = 'Welcome Guest!'
    return render_template("index.html", greeting=greeting)


@app.route("/hello", methods=['POST', 'GET'])
def hello():
    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index_laid_out.html", greeting=greeting)
    else:
        return render_template("hello_form.html")

@app.route("/test")
def test():
    return render_template("template_example.html")

if __name__ == "__main__":
    app.run()