from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
import enum

from app.config.database import Base


class AspectType(str, enum.Enum):
    PERMISSIVE = "PERMISSIVE"
    RESTRICTIVE = "RESTRICTIVE"
    OVERRIDE = "OVERRIDE"


class Signal(Base):
    __tablename__ = "signals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    aspects = relationship(
        "Aspect", back_populates="signal", cascade="all, delete-orphan"
    )


class Aspect(Base):
    __tablename__ = "aspects"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum(AspectType), index=True)
    is_on = Column(Boolean, default=False)
    signal_id = Column(Integer, ForeignKey("signals.id"))

    signal = relationship("Signal", back_populates="aspects")
