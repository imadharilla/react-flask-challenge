from db.database import db 

class UserDoorPermission(db.Model):
    __tablename__ = "user_door_permissions"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    door_id = db.Column(db.Integer)
    creation_time = db.Column(db.String)
