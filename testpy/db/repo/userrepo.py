from db.models.user import User
from db.connection import get_db
db = get_db()

def get_user():
    user = User.objects
    return user


def insert_user(user):
    user.save()


def update_user(id, schema_user):
    user = User.objects(id=id)[0]
    user.update(**schema_user)


def delete_user(id):
    user = User.objects(id=id)[0]
    user.delete()
