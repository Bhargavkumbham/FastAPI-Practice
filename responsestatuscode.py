from fastapi import FastAPI

app = FastAPI()

# Endpoint with custom response status code
@app.post("/items/", status_code=201) # 201 Created for post creation
async def create_item(name: str):
    return {"name": name}