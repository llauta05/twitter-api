#python native
from dataclasses import field
from datetime import date, datetime
from typing import Optional, List
from uuid import UUID


#pydantic
from pydantic import BaseModel, EmailStr, Field

#fastapi
from fastapi import FastAPI
from fastapi import status

app = FastAPI()

#models
class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(..., min_length=8)

class User(UserBase):
    first_name : str = Field(..., min_length=1, max_length=50)
    last_name : str = Field(..., min_length=1, max_length=50)
    birth_date: Optional[date] = Field(default=None)

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(..., max_length=256, min_length=1)
    created_at: datetime = Field(default=date.today)
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

#path operations
@app.get(path="/")
def home():
    return {"Twitter API": "working"}

##Users
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="register a User",
    tags=["Users"]
)
def signup():
    pass

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="login a User",
    tags=["Users"]
)
def login():
    pass

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="show all users",
    tags=["Users"]
)
def users():
    pass

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="show a user",
    tags=["Users"]
)
def show_a_user():
    pass

@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="delete a user",
    tags=["Users"]
)
def delete_a_user():
    pass

@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="update a user",
    tags=["Users"]
)
def update_a_user():
    pass

##tweets

@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="show all tweets",
    tags=["Tweets"]
)
def home():
    return {"twitter api":"working"}

@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="post a tweet",
    tags=["Tweets"]
)
def post():
    pass

@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="show a tweet",
    tags=["Tweets"]
)
def show_a_tweet():
    pass

@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="delete a tweet",
    tags=["Tweets"]
)
def delete_a_tweet():
    pass

@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="update a tweet",
    tags=["Tweets"]
)
def update_a_tweet():
    pass
