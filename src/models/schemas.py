from pydantic import BaseModel

class InventoryItem(BaseModel):
    sku: str
    quantity: int

class InventoryResponse(BaseModel):
    sku: str
    available_quantity: int
    status: str
