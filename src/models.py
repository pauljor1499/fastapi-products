from pydantic import BaseModel, Field


# Model for Item
class Item(BaseModel):
    id: str = Field(default=None, alias="_id")
    name: str = Field(default=None, alias="name")
    description: str = Field(default=None, alias="description")
    price: float = Field(default=None, alias="price")


# Model for Item Create
class ItemCreate(BaseModel):
    name: str
    description: str
    price: float


# Model for user login
class User(BaseModel):
    username: str
    password: str


# Model for the token response
class Token(BaseModel):
    access_token: str
    token_type: str