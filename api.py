from fastapi import FastAPI
from routes.items_routes import item_api_router

app = FastAPI()

app.include_router(item_api_router)