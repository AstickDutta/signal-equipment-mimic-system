from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.signal import (
    SignalCreate,
    AspectCreate,
    Signal,
    Aspect,
    SignalAspects,
)
from app.services.signal_service import SignalService, AspectService

router = APIRouter()


@router.post("/", response_model=Signal, status_code=status.HTTP_201_CREATED)
def create_signal(signal: SignalCreate, db: Session = Depends(get_db)):
    return SignalService.create_signal(db=db, signal=signal)


@router.get("/", response_model=List[Signal])
def read_signals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return SignalService.get_signals(db=db, skip=skip, limit=limit)


@router.get("/{signal_id}", response_model=Signal)
def read_signal(signal_id: int, db: Session = Depends(get_db)):
    return SignalService.get_signal(db=db, signal_id=signal_id)


@router.post(
    "/{signal_id}/aspects/", response_model=Aspect, status_code=status.HTTP_201_CREATED
)
def create_aspect(signal_id: int, aspect: AspectCreate, db: Session = Depends(get_db)):
    return AspectService.create_aspect(db=db, signal_id=signal_id, aspect=aspect)


@router.get("/{signal_id}/aspects", response_model=SignalAspects)
def get_signal_aspects(signal_id: int, db: Session = Depends(get_db)):
    signal = AspectService.get_signal_aspects(db=db, signal_id=signal_id)

    aspect_states = [
        {"type": aspect.type, "is_on": aspect.is_on} for aspect in signal.aspects
    ]

    return {
        "signal_id": signal.id,
        "signal_name": signal.name,
        "aspects": aspect_states,
    }
