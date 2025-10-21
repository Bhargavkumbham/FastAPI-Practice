from typing import Annotated

from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()

# Pydantic model for common headers
class CommonHeaders(BaseModel):
    model_config = {"extra": "forbid"} # Forbid extra headers not defined in the model

    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []

# Endpoint to read headers
@app.get("/items/")
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers