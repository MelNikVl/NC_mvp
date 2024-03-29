import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# расположение базы для разных систем
db_path = os.path.join(os.path.dirname(__file__), "nc.db")
SQLALCHEMY_DATABASE_URL = f"sqlite:///{db_path}"

# создание движка для работы с базой данных
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# создание сессии для работы с БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# подключение к базе данных. тоесть создается единовразовая сессия при обращении и сразу же закрывается
def get_db():
    try:
        db = SessionLocal()
        # bind_after_commit(db)
        yield db
    finally:
        db.close()