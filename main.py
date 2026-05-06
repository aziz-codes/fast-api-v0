from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message":"Welcome to FAST API."}


@app.get("/users")
def users():
    users = [{"name":f"user-{user}","age":user*4} for user in range(1,6)]
    return {"message":"Users route","data":users}