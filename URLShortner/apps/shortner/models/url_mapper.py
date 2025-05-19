from database import Base
from sqlalchemy import Column, String

class URLMapper(Base):
    
    __tablename__ = "url_mapper"
    
    url = Column(String(2048), nullable=False)
    hash_str = Column(String(255), nullable=False)
    tiny_url = Column(String(255), nullable=False)