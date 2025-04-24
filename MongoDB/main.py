# requirements.txt
# pip install fastapi uvicorn pymongo

# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from bson import ObjectId
from pymongo import MongoClient
import os

app = FastAPI()

# MongoDB connection
MONGO_URL = "mongodb://localhost:27017"
client = MongoClient(MONGO_URL)
db = client["testdb"]
collection = db["items"]

# Helper to convert MongoDB documents
def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc

# Pydantic models
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class UpdateItem(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]

@app.post("/items", response_model=dict)
def create_item(item: Item):
    result = collection.insert_one(item.dict())
    new_item = collection.find_one({"_id": result.inserted_id})
    return serialize_doc(new_item)

@app.get("/items", response_model=List[dict])
def get_items():
    items = list(collection.find({}))
    return [serialize_doc(doc) for doc in items]

@app.get("/items/{item_id}", response_model=dict)
def get_item(item_id: str):
    try:
        item = collection.find_one({"_id": ObjectId(item_id)})
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ObjectId")
    if item:
        return serialize_doc(item)
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=dict)
def update_item(item_id: str, item: UpdateItem):
    update_data = {k: v for k, v in item.dict().items() if v is not None}
    try:
        result = collection.update_one({"_id": ObjectId(item_id)}, {"$set": update_data})
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ObjectId")
    if result.modified_count == 1:
        updated_item = collection.find_one({"_id": ObjectId(item_id)})
        return serialize_doc(updated_item)
    raise HTTPException(status_code=404, detail="Item not found or no update performed")

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    try:
        result = collection.delete_one({"_id": ObjectId(item_id)})
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ObjectId")
    if result.deleted_count == 1:
        return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

# To run the server with this command
## uvicorn main:app --reload
