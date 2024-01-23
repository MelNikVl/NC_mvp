from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Boolean, Float

# вид базы данных
Base = declarative_base()


class Users:
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    chat_id: int = Column(Integer)
    username: str = Column(String)
    password: str = Column(String)
    is_admin: bool = Column(Boolean, default=False)