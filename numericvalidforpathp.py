from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/products/{product_id}")
def get_product(# Path Parameters with Numeric Validation and also enforcing positional arguments here
    product_id: Annotated[
        int,
        Path(
            title="Product ID",
            description="Unique identifier for the product (must be between 1000 and 9999)",
            ge=1000,
            le=9999
        )
    ],
    *, # Enforce keyword-only arguments after *
    rating: Annotated[
        float,
        Path(
            title="Product Rating",
            description="Product rating (must be greater than 0 and less than or equal to 5)",
            gt=0,
            le=5
        )
    ]
):
    # Simulate fetching product details
    return {
        "product_id": product_id,
        "rating": rating,
        "details": "Sample product details returned."
    }
