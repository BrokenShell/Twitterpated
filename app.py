from flask import Flask, render_template
from Fortuna import d


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/D100")
def d100():
    return render_template("d100.html", d=d)


@app.route("/gamma")
def gamma():
    return render_template("gamma.html")


if __name__ == '__main__':
    app.run(debug=True)
