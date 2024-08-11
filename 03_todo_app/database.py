from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLITE3 Database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos_app.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# This flag is used only with sqlite3.
# connect_args = {"check_same_thread": False}
# PostgreSQL Database URL
# SQLALCHEMY_DATABASE_URL = "postgresql://<user>:<password>@<localhost_port>/<database_name>"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# MySQL Database URL
# SQLALCHEMY_DATABASE_URL = (
#     "mysql_pymysql://<user>:<password>@<localhost_port>/<database_name>"
# )
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
