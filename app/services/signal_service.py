from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.signal import Signal, Aspect, AspectType
from app.schemas.signal import SignalCreate, AspectCreate, AspectUpdate


class SignalService:
    @staticmethod
    def create_signal(db: Session, signal: SignalCreate):
        db_signal_id = db.query(Signal).filter(Signal.id == signal.id).first()
        if db_signal_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Signal with id {signal.id} already exists",
            )

        db_signal_name = db.query(Signal).filter(Signal.name == signal.name).first()
        if db_signal_name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Signal with name {signal.name} already exists",
            )

        db_signal = Signal(id=signal.id, name=signal.name)
        db.add(db_signal)
        db.commit()
        db.refresh(db_signal)
        return db_signal

    @staticmethod
    def get_signals(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Signal).offset(skip).limit(limit).all()

    @staticmethod
    def get_signal(db: Session, signal_id: int):
        db_signal = db.query(Signal).filter(Signal.id == signal_id).first()
        if db_signal is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Signal with id {signal_id} not found",
            )
        return db_signal


class AspectService:
    @staticmethod
    def create_aspect(db: Session, signal_id: int, aspect: AspectCreate):
        db_signal = db.query(Signal).filter(Signal.id == signal_id).first()
        if db_signal is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Signal with id {signal_id} not found",
            )


        db_aspect = Aspect(
            type=aspect.type,
            is_on=False,
            signal_id=signal_id,
        )
        db.add(db_aspect)
        db.commit()
        db.refresh(db_aspect)
        return db_aspect

    @staticmethod
    def get_aspect(db: Session, aspect_id: int):
        db_aspect = db.query(Aspect).filter(Aspect.id == aspect_id).first()
        if db_aspect is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Aspect with id {aspect_id} not found",
            )
        return db_aspect

    @staticmethod
    def update_aspect_state(db: Session, aspect_id: int, aspect_update: AspectUpdate):
        db_aspect = db.query(Aspect).filter(Aspect.id == aspect_id).first()
        if db_aspect is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Aspect with id {aspect_id} not found",
            )

        if aspect_update.is_on is True:
            opposite_type = (
                AspectType.RESTRICTIVE
                if db_aspect.type == AspectType.PERMISSIVE
                else AspectType.PERMISSIVE
            )

            opposite_aspect = (
                db.query(Aspect)
                .filter(
                    Aspect.signal_id == db_aspect.signal_id,
                    Aspect.type == opposite_type,
                    Aspect.is_on.is_(True),
                )
                .first()
            )

            if opposite_aspect:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=(
                        f"Cannot turn ON {db_aspect.type} aspect when "
                        f"{opposite_type} aspect is already ON"
                    ),
                )


        db_aspect.is_on = aspect_update.is_on
        db.commit()
        db.refresh(db_aspect)
        return db_aspect

    @staticmethod
    def get_signal_aspects(db: Session, signal_id: int):
        db_signal = db.query(Signal).filter(Signal.id == signal_id).first()
        if db_signal is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Signal with id {signal_id} not found",
            )

        return db_signal
