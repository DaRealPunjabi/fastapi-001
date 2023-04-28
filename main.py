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

# list of dictionaries
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "favorite foods", "content": "I like pizza", "id": 2}]    

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
            

@app.get("/")
def root():
    return {"message": "Hello World ..."}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.get("/posts/{id}")
def get_post(id: int):
    print(id)
    print(type(id))
    # try:
    #     i = int(id)
    #     print(type(i))
    # except ValueError as verr:
    #     print("id does not contain anything convertible to int")
    # except Exception as ex:
    #     print("Exception occurred while converting to int")
    # print(type(i))
    print(my_posts[1])
    d = {x['id']: x for x in my_posts}
    print(d)
    print('d1')
    d1 = list(filter(lambda tag: tag['id'] == 2, my_posts))
    print(d1)
 
    #post =  find_post(int(id))
    post =  find_post(id)
    print(post)
    return {"post_detail": post}
    #return {"post_detail": f"Here is post {id}"}
    #return {"post_detail": d1}


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
