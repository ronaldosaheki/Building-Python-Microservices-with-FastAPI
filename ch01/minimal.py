from fastapi import FastAPI
app = FastAPI()

@app.get("/ch01/index")
def index():
    return {"message": "Welcome FastAPI Nerds"}