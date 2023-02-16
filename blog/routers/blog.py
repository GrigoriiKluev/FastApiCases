from fastapi import APIRouter, Depends, status,HTTPException, Response
from sqlalchemy.orm import Session
from .. import schemas, database , models, oauth2
from typing import List
from .. repository import blog


router = APIRouter(
    tags=['blogs'],
    prefix='/blog'
)
get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/' , status_code=status.HTTP_201_CREATED)
def create_blog(request:schemas.Blog, db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)



@router.delete('/{id}' , status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)



@router.put('/{id}' , status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int, request:schemas.Blog, db:Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)