import json
from flask import Flask, make_response, request
from db.database import get_db_config, db
from models.Address import Address
from models.User import User
from models.Door import Door
from models.UserDoorPermission import UserDoorPermission
from schemas.User import UserSchema
from schemas.Address import AddressSchema
from schemas.UserDoorPermission import UserDoorPermissionSchema
from schemas.Door import DoorSchema

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)

## Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = get_db_config()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


## Routes 

@app.route("/api/doors/", methods=["GET"])
def get_doors_list():
    doors_schema = DoorSchema(many=True)
    doors = Door.query.paginate()
    json_response = {}
    json_response['data'] = doors_schema.dumps(doors.items, ensure_ascii=False)
    json_response['nbr_pages'] = doors.pages
    json_response['current_page'] = doors.page
    json_response['total'] = doors.total
    response = make_response(json_response)
    response.headers["Content-Type"] = "application/json"
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')