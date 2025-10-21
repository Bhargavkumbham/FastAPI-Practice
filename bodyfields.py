from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
# Pydantic model for request body with field constraints and metadata
class Product(BaseModel):
    name: str = Field(..., title="Product Name", max_length=100, description="Name of the product")
    price: float = Field(..., gt=0, description="Price must be greater than zero")
    description: Optional[str] = Field(None, max_length=300, title="Product Description")
    in_stock: bool = Field(True, description="Is the product currently in stock?")

@app.post("/products/", response_model=Product)
async def create_product(product: Product):
    return product
