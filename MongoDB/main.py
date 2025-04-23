# requirements.txt
# pip install fastapi uvicorn motor

# main.py
from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from typing import List, Optional
from bson import ObjectId
import os

app = FastAPI()

# MongoDB connection URI
MONGO_URL = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URL)
db = client["testdb"]
collection = db["items"]

# Helper to convert MongoDB document to JSON serializable
def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc

# Pydantic models
class Item(BaseModel):
    name: str
    description: Optional[str]
    price: float

class UpdateItem(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]

@app.post("/items", response_model=dict)
async def create_item(item: Item):
    result = await collection.insert_one(item.dict())
    new_item = await collection.find_one({"_id": result.inserted_id})
    return serialize_doc(new_item)

@app.get("/items", response_model=List[dict])
async def get_items():
    items = []
    cursor = collection.find({})
    async for doc in cursor:
        items.append(serialize_doc(doc))
    return items

@app.get("/items", response_model=List[dict])
async def get_items():
    items = []
    cursor = collection.find({})
    async for doc in cursor:
        items.append(serialize_doc(doc))
    return items

@app.get("/items/{item_id}", response_model=dict)
async def get_item(item_id: str):
    item = await collection.find_one({"_id": ObjectId(item_id)})
    if item:
        return serialize_doc(item)
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=dict)
async def update_item(item_id: str, item: UpdateItem):
    update_data = {k: v for k, v in item.dict().items() if v is not None}
    result = await collection.update_one({"_id": ObjectId(item_id)}, {"$set": update_data})
    if result.modified_count == 1:
        updated_item = await collection.find_one({"_id": ObjectId(item_id)})
        return serialize_doc(updated_item)
    raise HTTPException(status_code=404, detail="Item not found or no update performed")

@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    result = await collection.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 1:
        return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

## uvicorn main:app --reload
