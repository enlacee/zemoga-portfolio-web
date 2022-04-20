from typing import List

from ..database import user_db
from ..models.models import User
from ..helpers import helper

def details(user: User) -> User:
    return user_db.detail(user)