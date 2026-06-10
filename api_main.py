from fastapi import FastAPI

app = FastAPI()

@app.post("/users")
def create_user(name: str):
    return {
        "message": f"Welcome {name}"
    }