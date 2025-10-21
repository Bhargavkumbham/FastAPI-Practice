from fastapi import FastAPI, Path
from enum import Enum

app = FastAPI()

#Basic path parameter
@app.get("/items/{item_id}")
def read_item(item_id: str):
    return {"item_id": item_id}

#Path parameter with type annotation and validation
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

#Enum for predefined values
class CarBrand(str, Enum):
    toyota = "toyota"
    ford = "ford"
    honda = "honda"

@app.get("/cars/{brand}")
def get_car(brand: CarBrand):
    return {
        "brand": brand.value
    }

#Path parameter containing paths (Starlette's :path converter)
@app.get("/files/{file_path:path}")
def read_file(file_path: str):
    return {"file_path": file_path}

#Numeric validation with Path.Here the value must be between 1 and 1000
@app.get("/products/{product_id}")
def get_product(product_id: int = Path(ge=1, le=1000)):
    return {"product_id": product_id}

#Route order matters There will be a conflict with /users/{user_id} if this is not defined first. So, we have to define this route before the one with path parameter. 
@app.get("/users/me")
def get_current_user():
    return {"user": "current"}

