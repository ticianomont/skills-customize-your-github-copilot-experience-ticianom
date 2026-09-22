from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Student Inventory API")


class ItemCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    description: str = ""
    price: float = Field(..., gt=0)


class Item(ItemCreate):
    id: int


items_db = [
    Item(id=1, name="Notebook", description="Blue notebook", price=5.99),
    Item(id=2, name="Pen", description="Black ink pen", price=1.75),
]


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.get("/items")
async def list_items():
    # TODO: return the list of items
    pass


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    # TODO: find item by id and raise 404 if missing
    pass


@app.post("/items", status_code=201)
async def create_item(item: ItemCreate):
    # TODO: create a new item and append it to items_db
    pass
