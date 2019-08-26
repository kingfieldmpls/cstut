# PowersHell >> $env:FLASK_APP = "flaskblog.py"
#            >> $env:FLASK_ENV = "development"
# YouTube link: https://www.youtube.com/watch?v=44PvX0Yv368
# I don't understand import routes in __init__
# I don't understand import models in routes.py
# Next vid (after rewatching for comprehension) https://www.youtube.com/watch?v=CSHx6eCkmv0
from flaskblog import app

if __name__ == "__main__":
    app.run(debug=True)
