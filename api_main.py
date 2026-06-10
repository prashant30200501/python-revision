"""from fastapi import FastAPI

app = FastAPI()

@app.post("/users")
def create_user(name: str):
    return {
        "message": f"Welcome {name}"
    }"""


from fastapi import FastAPI

app = FastAPI()

@app.post("/car")
def get_car(name :str , year : int):
    return{
        "message": f"car is {name} year is {year}"
        
    }