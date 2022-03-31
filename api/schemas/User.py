from models.User import User
from db.database import ma 

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
