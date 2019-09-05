# PowersHell >> $env:FLASK_APP = "flaskblog.py"
#            >> $env:FLASK_ENV = "development"
# YouTube link: https://www.youtube.com/watch?v=Wfx4YBzg16

from flaskblog import app

if __name__ == "__main__":
    app.run(debug=True)
