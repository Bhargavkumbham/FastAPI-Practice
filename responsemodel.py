from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic models for request and response
class UserIn(BaseModel):
    username: str
    password: str
# Response model
class UserOut(BaseModel):
    username: str

@app.post("/register", response_model=UserOut)# Endpoint to register a user this uses response model
def register(user: UserIn):
    return UserOut(username=user.username) # Return only the username in the response
