from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.signal import AspectUpdate, Aspect
from app.services.signal_service import AspectService

router = APIRouter()


@router.get("/{aspect_id}", response_model=Aspect)
def read_aspect(aspect_id: int, db: Session = Depends(get_db)):
    return AspectService.get_aspect(db=db, aspect_id=aspect_id)


@router.patch("/{aspect_id}", response_model=Aspect)
def update_aspect_state(
    aspect_id: int, aspect: AspectUpdate, db: Session = Depends(get_db)
):
    return AspectService.update_aspect_state(
        db=db, aspect_id=aspect_id, aspect_update=aspect
    )
