from mongoengine import DynamicDocument
from mongoengine import IntField, StringField, DecimalField, BooleanField
from core.settings import settings


class User(DynamicDocument):

    
    name = StringField()

    meta = {'db_alias': settings.DB_ALIAS, 'collection': "user"}