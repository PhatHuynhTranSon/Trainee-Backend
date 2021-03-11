from flask import Flask
from flask_restful import Api
from config import (
    DATABASE_URI
)
from database import database as db

# Create app
app = Flask(__name__)
api = Api(app)

# Set up database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI

@app.before_first_request
def create_all_tables_before_requests():
    db.create_all()

if __name__ == "__main__":
    # Don't use debug=True in production
    app.run(port=3000, debug=True)