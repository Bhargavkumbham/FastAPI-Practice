from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

# Pydantic model for request body
class Product(BaseModel):
    name: str
    price: float
    description: str | None = None  # This is an optional field

# Endpoint combining path params, query params, and request body
@app.put("/products/{product_id}")
def update_product(
    product_id: int,                # Path parameter
    product: Product,               # Request body (Pydantic model)
    discount: float | None = Query(None, gt=0, lt=1)  # Optional query parameter
):
    # Access model fields directly. This allows to unpack the model into a dictionary if needed
    product_data = product.model_dump()  # For Pydantic v2 # Use product.dict() for Pydantic v1
    
    # Use the values in your logic
    final_price = product.price
    if discount:
        final_price *= (1 - discount)
    return {
        "product_id": product_id,
        "product": product_data,
        "discount": discount,
        "final_price": final_price
    }
