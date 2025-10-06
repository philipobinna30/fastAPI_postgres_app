from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base



# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False)

# Base class for models
Base = declarative_base()


from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Access the values
secret_key = os.getenv("SECRET_KEY")
api_key = os.getenv("API_KEY")

print("Secret Key:", secret_key)
print("API Key:", api_key)

