from flask import Flask, render_template, request
from analyzer import analyze_poem
from rhyme_scheme import detect_rhyme_scheme

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    poem = request.form["poem"]

    lines = poem.splitlines()

    result = analyze_poem(lines)

    result["rhyme_scheme"] = detect_rhyme_scheme(lines)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)