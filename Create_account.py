from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base
from database import Session

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

def create_account(username, password):
    session = Session()

    # Check if the username already exists
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        print("Error: This username is already taken. Please choose another one.")
        return

    # Create a new user
    new_user = User(username=username, password=password)
    session.add(new_user)
    session.commit()
    print("Account created successfully.")

if __name__ == "__main__":
    # This block is for testing purposes
    from database import initialize_database
    initialize_database()
    create_account("example_user", "password123")
