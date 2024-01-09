import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


DB_URL = "postgresql://postgres:{pw}@backend_db:5432/postgres"


if os.environ.get("POSTGRES_DB"):
    engine = create_engine(DB_URL.format(pw=os.environ.get("POSTGRES_PASSWORD")))
else:
    load_dotenv("backend/application/settings/.env")
    engine = create_engine(
        "sqlite:///./sql_app.db", connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
