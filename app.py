import random
from config import app
@app.get('/message')
def greet():
    return "Hello Micro services HOw are you doing"
@app.get('/number')
def fun():
    num = random.randint(0,100)
    return f"{num} is returned"    