from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

# here I define a Pydantic model to developed query parameters with validation
class ProductFilter(BaseModel):
    search: str = Field(description="Search term")
    category: str = Field(description="Product category")
    limit: int = Field(10, gt=0, le=100, description="Max results")
    tags: List[str] = Field([], description="Tag filter")

    model_config = {"extra": "forbid"}  # Rejects unknown parameters

# Define the endpoint using the Pydantic model for query parameters
@app.get("/products/")
async def get_products(filters: ProductFilter):
    return filters
