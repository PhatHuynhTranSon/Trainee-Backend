from database import database as db
from uuid import uuid4


class Project(db.Model):
    __tablename__ == "projects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    location_name = db.Column(db.String(255)) # This denotes the project location name in s3 bucket
    description = db.Column(db.String(255))

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.generate_location_name()

    def generate_location_name(self):
        # Generate a unique uuid string
        self.location_name = uuid4().hex

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()