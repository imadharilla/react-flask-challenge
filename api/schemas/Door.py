from models.Door import Door
from db.database import ma 

class DoorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Door
