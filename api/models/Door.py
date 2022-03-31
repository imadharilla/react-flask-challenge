from db.database import db 

class Door(db.Model):
    __tablename__ = "doors"
    id = db.Column(db.Integer, primary_key=True)
    sensor_uuid = db.Column(db.String)
    name = db.Column(db.String)
    address_id = db.Column(db.Integer, db.ForeignKey("addresses.id"))
    installation_time = db.Column(db.String)
