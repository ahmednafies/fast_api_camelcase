from fastapi import FastAPI
from models import User


def test_users():
    user = User(first_name="Ahmed", last_name="Nafies", age=19)
    print(user)
