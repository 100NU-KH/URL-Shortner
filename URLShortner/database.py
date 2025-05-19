from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker
from sqlalchemy import create_engine, Boolean, Column

SQLALCHEMY_DATABASE_URL = "sqlite:///shortner.db"

class BaseModel:
    
    id: Mapped[int] = mapped_column(primary_key=True)
    is_active: Mapped[bool] = Column(Boolean, default=True)


Base = declarative_base(cls=BaseModel)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()