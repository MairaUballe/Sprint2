from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://fwjdsqkxcjpjsk:78980a33998a3d2d0947e3c819986d2a0c07d3b0a7addad3bb6bf599e475842f@ec2-54-157-4-216.compute-1.amazonaws.com:5432/d4o9p1h00n845r"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

session = SessionLocal()
Base = declarative_base()
Base.metadata.schema = "OCCUPO_DB"