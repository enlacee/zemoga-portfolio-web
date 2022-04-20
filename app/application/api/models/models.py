from typing import NamedTuple, Optional

class User(NamedTuple):
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    image_url: Optional[str] = None
    description: Optional[str] = None
    skills: Optional[str] = None
    email: Optional[str] = None
