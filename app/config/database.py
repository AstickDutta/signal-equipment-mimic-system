import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Get database URL from environment variable, fallback to PostgreSQL for local dev
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:root@localhost:5432/signal_equipment"
)

# Handle PostgreSQL URL format
if DATABASE_URL.startswith("postgresql://"):
    engine = create_engine(DATABASE_URL)
else:
    # SQLite configuration (for backward compatibility)
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
