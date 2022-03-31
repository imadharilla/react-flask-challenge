from flask_sqlalchemy import SQLAlchemy
import os 
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


def get_db_config():
    # return 'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
    #     user=os.environ.get('POSTGRES_USER'),
    #     passwd='',
    #     host=os.environ.get('POSTGRES_HOST'),
    #     port=os.environ.get('POSTGRES_PORT'),
    #     db=os.environ.get('POSTGRES_DB_NAME'))
    
    return 'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user='kiwi',
        passwd='',
        host='localhost',
        port='5432',
        db='kiwi')