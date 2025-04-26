from flask import Flask
from routes.client import client
from config.config import DATABASE_CONNECTION_URI
from models.db import db

app = Flask(__name__)

app.register_blueprint(client)

app.config["SQLALCHEMY_DATABASE_URI"]= DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    from models.client import Client
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)