from models.UserDoorPermission import UserDoorPermission
from db.database import ma 

class UserDoorPermissionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserDoorPermission
