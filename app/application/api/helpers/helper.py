
import re
from ..models.models import User

def format_name(user: User)-> User:
    user_dic = user._asdict()
    user_dic["firt_name"] = user.first_name.capitalize()
    user_dic["last_name"] = user.last_name.capitalize()
    return User(**user_dic)
