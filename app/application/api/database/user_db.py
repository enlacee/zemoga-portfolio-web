from typing import List

from .connection import _fetch_one
from ..models.models import User
from ..models.exceptions import UserNotFound

def detail(user: User) -> User:
    query = "SELECT * FROM users WHERE id=?"
    parameters = [user.id]
    record = _fetch_one(query, parameters)
    if record is None:
        raise UserNotFound(f"No user with id: {user.id}")
    user = User(
        id=record[0],
        first_name=record[1],
        last_name=record[2],
        email=record[3],
        image_url=record[4],
        description=record[5],
        skills=record[6]
    )
    return user