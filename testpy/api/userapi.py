import traceback
from fastapi import APIRouter, HTTPException
from business import userservice
from schema.user import User

router = APIRouter(prefix="/user")


@router.get('')
def api_fetch_user():
    return userservice.fetch_user()

@router.post('')
def api_insert_user(user: User):
    userservice.insert_user(user)
    return "success"

@router.put('/{id}')
def api_update_user(id: str, user: User):
    userservice.update_user(id, user)
    return "success"

@router.delete('/{id}')
def api_delete_user(id: str):
    userservice.delete_user(id)
    return "success"