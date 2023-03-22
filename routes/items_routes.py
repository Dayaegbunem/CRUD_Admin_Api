from fastapi import APIRouter
from config.database import collection_name
from models.items_model import Item
from schemas.items_schema import item_serializer, items_serializer
from bson import ObjectId

item_api_router = APIRouter()

#read all titles
@item_api_router.get('/')
async def get_items():
    items = items_serializer(collection_name.find())
    return {'status': 'ok', 'data': items}

#read a single title 
@item_api_router.get('/{id}')
async def get_item(id: str):
    item = items_serializer(collection_name.find({'_id': ObjectId(id)}))
    return {'status': 'ok', 'data': item}

#Create a new title
@item_api_router.post('/')
async def post_item(item: Item):
    _id = collection_name.insert_one(dict(item))
    item = item = items_serializer(collection_name.find({'_id': _id.inserted_id}))
    return {'status': 'ok', 'data': item}

#Update existing title
@item_api_router.put('/{id}')
async def update_item(id: str, item: Item):
    collection_name.find_one_and_update({'_id': ObjectId(id)}, {
        '$set': dict(item)
    })
    item = items_serializer(collection_name.find({'_id': ObjectId(id)}))
    return {'status': 'ok', 'data': item}

#Delete a single title
@item_api_router.delete('/{id}')
async def delete_item(id: str):
    collection_name.find_one_and_delete({'_id': ObjectId(id)})
    return {'status': 'ok', 'data': []}

