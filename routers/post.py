from fastapi import APIRouter
from database import post_table,comment_table,database
from models.post import (
    UserPostIn,
    UserPost,
    CommentIn,
    Comment
)

router = APIRouter()

@router.post("/post",response_model=UserPost)
async def create_post(post: UserPostIn):
    query = post_table.insert.values(body=post.body)
    last_record_id = await database.execute(query)
    return {**post.dict(),"id":last_record_id}

@router.get("/post",response_model=UserPost)
async def get_all_posts():
    query = post_table.select()
    return await database.fetch_all(query)

@router.post("/comment",response_model=Comment)
async def create_comment(comment: CommentIn):
    query = comment_table.insert.values(body=comment.body,post_id=comment.post_id)

@router.get("/post/{post_id}/comment",response_model=Comment)
async def get_comments_on_post(post_id: int):
    query = comment_table.select().where(post_id==post_id)
    return await database.fetch_all(query)