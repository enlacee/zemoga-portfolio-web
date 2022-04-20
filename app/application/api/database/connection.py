from contextlib import contextmanager
from typing import Any, Iterator, List, Optional
import sqlite3
from config import Config

DATABASE_PATH = Config.DATABASE_PATH

@contextmanager
def __get_cursor() -> Iterator[sqlite3.Cursor]:
    """
    Create a function with a contextManager to cursosr sqlite
    """
    connection: sqlite3.Connection = sqlite3.connect(DATABASE_PATH)
    cursor: sqlite3.Cursor = connection.cursor()
    try:
        yield cursor
        connection.commit()
    finally:
        cursor.close()
        connection.close()

def _fetch_one(query: str, parameters: Optional[List[str]] = None) -> Any:
    if parameters is None:
        parameters = []
    
    with __get_cursor() as cursor:
        cursor.execute(query, parameters)
        return cursor.fetchone()