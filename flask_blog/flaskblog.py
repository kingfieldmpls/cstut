# PowersHell >> $env:FLASK_APP = "flaskblog.py"
#            >> $env:FLASK_ENV = "development"
# YouTube link: https://youtu.be/UIJKdCIEXUQ?t=704


from flask import Flask, render_template, url_for, flash, redirect  # noqa: F401
from forms import RegistrationForm, LoginForm

app = Flask(__name__)


app.config["SECRET_KEY"] = "922903b5c9704ab45341228764219fbb"

posts = [
    {
        "author": "Rob Martin",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "August 15, 2019",
    },
    {
        "author": "Rod Martin",
        "title": "Blog Post 2",
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
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
