

from flask import Flask, request, render_template, redirect
from keywords_finder import get_keywords

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/find")
def find():
    youtube_code = request.args.get("code")
    data = get_keywords(youtube_code).split(",")
    return render_template("index.html", keywords=data)

if __name__ == "__main__":
    app.run()