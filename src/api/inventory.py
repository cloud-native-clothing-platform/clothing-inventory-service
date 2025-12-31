from fastapi import APIRouter
from src.models.schemas import InventoryItem, InventoryResponse

router = APIRouter()

@router.post("/", response_model=InventoryResponse)
def add_item(item: InventoryItem):
    return InventoryResponse(
        sku=item.sku,
        available_quantity=item.quantity,
        status="AVAILABLE"
    )

@router.get("/{sku}", response_model=InventoryResponse)
def get_item(sku: str):
    return InventoryResponse(
        sku=sku,
        available_quantity=100,
        status="AVAILABLE"
    )
