from fastapi import FastAPI, Query
from typing import Annotated, Optional, Literal

app = FastAPI()

@app.get("/products/")
def get_products(
    category: Annotated[
        str|None,
        Query( min_length=3, max_length=20, title="Category", description="Product category to filter by")
    ] = None,
    price_from: Annotated[
        float|None,
        Query( ge=0, title="Min Price", description="Minimum price")
    ] = None,
    price_to: Annotated[
        float|None,
        Query( ge=0, title="Max Price", description="Maximum price")
    ] = None,
    brands: Annotated[
        list[str]|None,
        Query( title="Brands", description="List of brands to filter")
    ] = None,
    sort_by: Annotated[
        Literal["name", "price", "rating"],
        Query( title="Sort By", description="Sort products by this field")
    ] = "name",
    page: Annotated[
        int,
        Query( ge=1, title="Page", description="Page number")
    ] = 1,
    page_size: Annotated[
        int,
        Query( ge=1, le=100, title="Page Size", description="Number of products per page")
    ] = 20,
):
    return {
        "category": category,
        "price_from": price_from,
        "price_to": price_to,
        "brands": brands,
        "sort_by": sort_by,
        "page": page,
        "page_size": page_size
    }
