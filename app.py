from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from constants import (
    DatabaseConstants,
    RouteConstants,
    SQLAlchemyConstants
)

app = Flask(__name__)

app.config[SQLAlchemyConstants.CONFIG_URI_NAME] = f'{DatabaseConstants.TYPE}:///{DatabaseConstants.NAME}'

app.config[SQLAlchemyConstants.CONFIG_TRACK_MODIFICATIONS] = True

db = SQLAlchemy(app)


@app.route(RouteConstants.HOME)
def home():
    return 'home'


if __name__ == '__main__':
    app.run(debug=True)
