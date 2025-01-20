import uuid
from datetime import datetime

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sq
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import sessionmaker

# Update your database URL (check the actual connection string)
engine = sq.create_engine('postgresql://postgres:1234@localhost:5432/adbs')

Base = declarative_base()
# Create a connection to the database
engine.connect()

class User(Base):
    __tablename__ = 'user'
    metadata = Base.metadata
    id = Column(UUID(as_uuid=True), primary_key=True ,default=uuid.uuid4)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    timestamp = Column(DateTime, nullable=False ,default=datetime.utcnow)
    role = Column(String, nullable=False , default='user')

class SessionModel(Base):
    __tablename__ = 'session'
    metadata = Base.metadata
    id = Column(UUID(as_uuid=True), primary_key=True ,default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'))
    timestamp = Column(DateTime, nullable=False ,default=datetime.utcnow)
    status = Column(Boolean, nullable=False, default=True)

# Create the tables in the database
try:
    Base.metadata.create_all(engine)
    print("Tables created successfully!")
except Exception as e:
    print(f"Error creating tables: {e}")

# Create session factory with a different name to avoid conflict
SessionFactory = sessionmaker(bind=engine)

# Example: Create a session and query
session = SessionFactory()

# Example usage: Add a new user
new_user = User(username="john_doe", password="password123", age=30 , role="admin")
session.add(new_user)
session.commit()

# Close the session after use
session.close()


