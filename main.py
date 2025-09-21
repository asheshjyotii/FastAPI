from fastapi import FastAPI
from fastapi.params  import Body
from pydantic import BaseModel
from typing import Optional
import os

#path declaration
BASE_DIR = os.getcwd()

# pydantic validation(model) declaration
class Post(BaseModel):
    title : str
    content : str
    draft : bool = False
    rating : Optional[int] = None

# data loading
def data_load():
    posts ={}
    with open (BASE_DIR + '/data/data.txt', 'r') as f:
        data = f.read()
        data = data.split('\n')
        for i,data_  in enumerate(data):
            posts[i]=data_
    return posts

# data creation

def data_creation(data):
    with open(BASE_DIR + '/data/data.txt', 'a') as f:
        f.write(data + '\n')


app = FastAPI()

@app.get('/')
def home():
    return {
        'message' : 'Hello from the other side!!'
    }

# Get all posts

@app.get('/posts')
def get_posts():
    data = data_load()
    print(data)
    return {
        'posts' : data
    }

# Create post
@app.post('/posts')

# def create_post(request_body : Post):
#     print(request_body)
#     return {
#         "title" : request_body.title,
#         "content" : request_body.content
#     }

def create_post(request_body:Post):
    print(request_body)
    data = request_body.dict()
    data_creation(str(data))
    return {
        "data" : "data saved"
    }

# Get single post
@app.get('/posts/{post_id}')
def get_single_post(post_id : int):
    data = data_load()
    data = data.get(post_id)
    print(data)
    return {
        # 'title' : data['title'],
        # 'content' : data['content'],
        # 'draft' : data['draft'],
        # 'rating' : data['rating']
        data
    }