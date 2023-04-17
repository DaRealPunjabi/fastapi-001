from turtle import title
from typing import Optional
#from fastapi import Body, FastAPI

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "favorite foods", "content": "I like pizza", "id": 2}]    

@app.get("/")
def root():
    return {"message": "Hello World ..."}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    # print(post)
    # print(post.dict())
    print(max([x['id'] for x in my_posts]))
    post_dict = post.dict()
    #post_dict['id'] = randrange(1, 10000000)
    post_dict['id'] = max([x['id'] for x in my_posts]) + 1
    my_posts.append(post_dict)
    return {"data": post_dict}

    # return {"data": post}
