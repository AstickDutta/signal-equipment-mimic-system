from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres:root123@localhost:5432/signal_equipment")

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(result.all())
