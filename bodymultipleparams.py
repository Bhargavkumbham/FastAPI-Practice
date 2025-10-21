from fastapi import FastAPI, Body, Path, Query
from pydantic import BaseModel

# Pydantic models for request body
class Product(BaseModel):
    name: str
    price: float

class Detail(BaseModel):
    info: str

app = FastAPI()

@app.post("/products/{prod_id}")
async def create_product(
    prod_id: int = Path(..., description="Product ID"), # Path Parameter
    product: Product = Body(embed=True), # embed is used to wrap the body parameters under "product" if there are multiple body params
    detail: Detail = Body(),
    rating: int = Body(ge=1, le=5)
):
    return {"prod_id": prod_id, "product": product, "detail": detail, "rating": rating}
