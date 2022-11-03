from business.utils import convert_model_to_dict
from schema import user as SchemaUser
from db.models.user import User
from db.repo import userrepo


def fetch_user():
    rows = userrepo.get_user()
    return [convert_model_to_dict(row) for row in rows]

def insert_user(schema_user):
    schema_user_dict = {key: value for key, value in schema_user.dict().items() if key != 'id'}
    user = User(**schema_user_dict)
    userrepo.insert_user(user)

def update_user(id, schema_user):
    user = schema_user.dict()
    del user['id']
    userrepo.update_user(id, user)

def delete_user(id):
    userrepo.delete_user(id)