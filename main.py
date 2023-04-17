from fastapi import Body, FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World ..."}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    #return {"message": "successfully created posts"}
    return {"new_post": f"title {payLoad['title']} content: {payLoad['content']}"}
