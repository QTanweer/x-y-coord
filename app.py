from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/random_coordinates")
def get_random_coordinates():
    x = random.randint(0, 1080)
    y = random.randint(0, 1920)
    return {"x_coord": x, "y_coord": y}