from pydantic import BaseModel #for validate data (serializers)
from typing import List

class UserPostIn(BaseModel):
    body: str

class UserPost(UserPostIn): #Dry dont repeat yourself
    id: int

class CommentIn(BaseModel):
    post_id: int
    body: str

class Comment(CommentIn):
    id: int

class UserPostWithComments(BaseModel):
    post: UserPost
    comments: List[Comment]