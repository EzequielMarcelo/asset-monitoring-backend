from app.db.database import engine

def test_db_connection():
    with engine.connect() as conn:
        assert conn is not None
