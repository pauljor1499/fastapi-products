from fastapi import FastAPI, HTTPException, status
from src.models import Item
from src.commons.serializers import item_serializer
from bson import ObjectId
from typing import List
from src.database import collection




app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to Paul Jor API"}


@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    result = collection.insert_one(item.dict())
    new_item = collection.find_one({"_id": result.inserted_id})
    return item_serializer(new_item)


@app.get("/items/", response_model=List[Item], status_code=status.HTTP_200_OK)
def get_items():
    items = list(collection.find())
    return [item_serializer(item) for item in items]


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: str):
    item = collection.find_one({"_id": ObjectId(item_id)})
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item_serializer(item)


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: str, updated_item: Item):
    result = collection.update_one({"_id": ObjectId(item_id)}, {"$set": updated_item.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    item = collection.find_one({"_id": ObjectId(item_id)})
    return item_serializer(item)


@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    result = collection.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item successfully deleted"}
