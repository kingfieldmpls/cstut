# PowersHell >> $env:FLASK_APP = "flaskblog.py"
#            >> $env:FLASK_ENV = "development"
# https://youtu.be/QnDWIZuWYW0?t=622

from flask import Flask, render_template

app = Flask(__name__)


posts = [
    {
        "author": "Rob Martin",
        "tite": "Blog Post 1",
        "content": "First post content",
        "date_posted": "August 15, 2019",
    },
    {
        "author": "Rod Martin",
        "tite": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "August 15, 2019",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
