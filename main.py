#python native
import json
from datetime import date, datetime
from typing import Optional, List
from uuid import UUID

#pydantic
from pydantic import BaseModel, EmailStr, Field

#fastapi
from fastapi import Body, FastAPI
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
class UserRegister(User):
    password: str = Field(..., min_length=8)

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(..., max_length=256, min_length=1)
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

#path operations

##Users
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="register a User",
    tags=["Users"]
)
def signup(user: UserRegister = Body(...)):
    with open("users.json","r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user

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
    with open("users.json", "r", encoding="utf=8") as f:
        results = json.loads(f.read())
        return results

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
