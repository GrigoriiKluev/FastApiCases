from fastapi import APIRouter, Depends, status,HTTPException, Response
from sqlalchemy.orm import Session
from .. import schemas, database , models , hashing
from typing import List
from ..repository import user



router = APIRouter(
    tags=['users'],
    prefix='/user'
)
get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request:schemas.User,  db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    return user.get(id, db)