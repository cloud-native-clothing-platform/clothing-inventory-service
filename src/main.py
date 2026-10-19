"""Inventory API starter with guarded stock adjustments."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Clothing Inventory Service", version="1.0.0")
class Stock(BaseModel): product_id: str; quantity: int = Field(ge=0)
class Adjustment(BaseModel): delta: int
STOCK: dict[str, int] = {"tee-001": 100, "hood-001": 40}
@app.get("/health")
def health(): return {"status": "ok", "service": "inventory"}
@app.get("/inventory/{product_id}", response_model=Stock)
def get_stock(product_id: str):
    if product_id not in STOCK: raise HTTPException(404, "Inventory item not found")
    return Stock(product_id=product_id, quantity=STOCK[product_id])
@app.post("/inventory/{product_id}/adjust", response_model=Stock)
def adjust_stock(product_id: str, adjustment: Adjustment):
    if product_id not in STOCK: raise HTTPException(404, "Inventory item not found")
    updated = STOCK[product_id] + adjustment.delta
    if updated < 0: raise HTTPException(409, "Insufficient stock")
    STOCK[product_id] = updated
    return Stock(product_id=product_id, quantity=updated)
