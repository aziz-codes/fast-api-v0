from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message":"Welcome to FAST API."}


@app.get("/users")
def users():
    return {"message":"Users route"}