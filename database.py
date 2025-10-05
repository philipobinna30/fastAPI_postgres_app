from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydb"


# Create engine
engine = create_engine(DATABASE_URL)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Access the values
db_url = os.getenv("DATABASE_URL")
secret_key = os.getenv("SECRET_KEY")
api_key = os.getenv("API_KEY")

print("Database URL:", db_url)
print("Secret Key:", secret_key)
print("API Key:", api_key)

