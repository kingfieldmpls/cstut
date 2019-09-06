# PowersHell >> $env:FLASK_APP = "flaskblog.py"
#            >> $env:FLASK_ENV = "development"
# YouTube link: https://youtu.be/goToXTC96Co?t=76

from flaskblog import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
