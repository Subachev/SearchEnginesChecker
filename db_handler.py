import sqlite3
import json
from typing import Any, Dict, List


db_name = "example.db"
table_name = "sites_data"
sql_conn = sqlite3.connect(db_name)


def get_sites_data() -> List[Dict[str, Any]]:
    """Получение сайтов с данными из базы данных.

    Returns:
        Список словарей с сайтами и их данными.
    """
    cursor = sql_conn.cursor()
    return [
        {"url": row[0], "search_element": row[1], "cookies": json.loads(row[2])}
        for row in cursor.execute(f"SELECT * FROM {table_name}")
    ]
