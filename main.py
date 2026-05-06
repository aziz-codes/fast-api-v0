from fastapi import FastAPI
from mock.users import users as user_data

#fast api ref as app.
app = FastAPI()
#first get route.
@app.get("/users")
def users():
    return {"message":"Users route","data":user_data}