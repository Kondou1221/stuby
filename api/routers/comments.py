from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm.session import Session
from typing import List

import api.schemas.comments as comment_schma
import api.cruds.comments as comment_crud
from api.db import get_db

router = APIRouter(
    prefix='/comment',
    tags=['comments']
)

#リプライ取得
@router.get("/select",
    summary="リプライ取得",
    response_model=List[comment_schma.select_comment_id] or comment_schma.select_comment_id,
    status_code=status.HTTP_200_OK
    )
async def get_comment(post_id: int, db: Session = Depends(get_db) ):
    comment = comment_crud.get_comment(db, post_id)

    if not comment:
        raise HTTPException(status_code=404, detail="comment does not exist")
    
    return comment

#新規リプライ作成
@router.post("/insert",
    summary="新規リプライ作成",
    status_code=status.HTTP_201_CREATED
    )
async def create_comment(request: comment_schma.base_comment_schma, db: Session = Depends(get_db) ):
    new_comment = comment_crud.create_comment(db, request)

    if not new_comment:
        raise HTTPException(status_code=401, detail="Signup failed")
    
    return {"message":"status OK"}

#リプライいいね追加
@router.post("/insert/good")
async def insert_commentgood(request: comment_schma.commentgood_request, db: Session = Depends(get_db) ):
    new_commentgood = comment_crud.insert_commentgood(db, request)

    if not new_commentgood:
        raise HTTPException(status_code=401, detail="Sign Up")
    
    return {"message":"status OK"}

#リプライいいね削除
@router.delete("/delete/good")
async def delete_commentgood(request: comment_schma.commentgood_request, db: Session = Depends(get_db) ):
    delete_commentgood = comment_crud.delete_commentgood(db, request)

    if not delete_commentgood:
        raise HTTPException(status_code=401, detail="Delete Up")

    return {"message":"status OK"}
