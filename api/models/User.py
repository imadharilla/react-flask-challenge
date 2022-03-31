from db.database import db 

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    creation_time = db.Column(db.String)
