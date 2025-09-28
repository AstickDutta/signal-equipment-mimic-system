from pydantic import BaseModel, Field
from typing import List
from app.models.signal import AspectType


class AspectBase(BaseModel):
    type: AspectType


class AspectCreate(AspectBase):
    pass


class AspectUpdate(BaseModel):
    is_on: bool


class Aspect(AspectBase):
    id: int
    is_on: bool
    signal_id: int

    class Config:
        orm_mode = True


class SignalBase(BaseModel):
    name: str


class SignalCreate(SignalBase):
    id: int = Field(..., gt=0)  # Ensure ID is a positive integer


class Signal(SignalBase):
    id: int
    aspects: List[Aspect] = []

    class Config:
        orm_mode = True


class AspectState(BaseModel):
    type: AspectType
    is_on: bool


class SignalAspects(BaseModel):
    signal_id: int
    signal_name: str
    aspects: List[AspectState]