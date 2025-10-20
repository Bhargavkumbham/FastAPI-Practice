from fastapi import FastAPI

app=FastAPI()

#without type validation
@app.get("/products/{product_id}")
async def get_product_by_id(product_id):
    return {"Product_id":product_id}

#with type validation
@app.get("/products/{product_id}")
async def get_product_by_id(product_id:int):
    return {"Product_id":product_id}

#using multiple path params
@app.get("/users/{user_id}/posts/{post_id}")
async def user_post(user_id: int, post_id: str):
    return {"user_id": user_id, "post_id": post_id}

#order of path parameters is necessary first should be fixed path and then dynamic path
@app.get("/profiles/me")
async def get_current_profile():
    return {"profile": "current user"}

@app.get("/profiles/{profile_id}")
async def get_profile(profile_id: str):
    return {"profile": profile_id}

#path parameter with enum(restricting path params to certain values)
from enum import Enum
from fastapi import FastAPI

class DeviceType(str, Enum):
    phone = "phone"
    tablet = "tablet"
    laptop = "laptop"

app = FastAPI()

@app.get("/devices/{device_type}")
async def get_device(device_type: DeviceType):
    if device_type is DeviceType.phone:
        return {"device_type": device_type, "message": "Mobile Device"}
    if device_type.value == "tablet":
        return {"device_type": device_type, "message": "Tablet Device"}
    return {"device_type": device_type, "message": "Laptop Device"}

#path parameter accepting slash(path converter)
from fastapi import FastAPI

app = FastAPI()

@app.get("/files/{file_path:path}")
async def read_file_path(file_path: str):
    return {"file_path": file_path}
