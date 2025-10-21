from fastapi import FastAPI, Query
from enum import Enum
from typing import Optional

app = FastAPI()

#Required query parameter, default-valued, and optional
@app.get("/items/{item_id}")
def read_item(
    item_id: str,
    needy: str,  # required query parameter
    skip: int = 0,  # default-valued query parameter
    limit: int|None = None  # optional query parameter
):
    return {
        "item_id": item_id,
        "needy": needy,
        "skip": skip,
        "limit": limit
    }

#Boolean query parameter (auto-conversion from string)
@app.get("/flags/")
def get_flag(active: bool = Query(False)):
    return {"active": active}

#Enum as query parameter
class Color(str, Enum): 
    red = "red" 
    green = "green" 
    blue = "blue"

@app.get("/colors/")
def get_color(color: Color):
    return {"color": color}

#Multiple path and query parameters together
@app.get("/products/{product_id}")
def get_product(
    product_id: int,
    available: bool = Query(True),
    category: Optional[str] = None
):
    return {
        "product_id": product_id,
        "available": available,
        "category": category
    }

#Combination of required, default, and optional query parameters
@app.get("/search/")
def search(
    q: str,  # required
    page: int = 1,  # default
    sort: Optional[str] = None  # optional
):
    return {
        "q": q,
        "page": page,
        "sort": sort
    }
