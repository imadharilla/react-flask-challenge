from models.Address import Address
from db.database import ma 

class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address
