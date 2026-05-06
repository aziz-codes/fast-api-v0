from fastapi import FastAPI
from mock.users import users as user_data
from pydantic import BaseModel


class User(BaseModel):
    name:str
    age: int

#fast api ref as app.
app = FastAPI()
#first get route.
@app.get("/users")
def users():
    return {"message":"Users route","data":user_data}

@app.post("/users")
def post_users(user:User):
    payload = {
        "id":len(user_data)+1,
        "name": user.name,
        "age": user.age
    }
    user_data.append(payload)
    return{"message":"user created","data":payload}
