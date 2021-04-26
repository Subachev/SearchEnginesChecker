"""Скрипт для создания и наполнения тестовой таблицы."""
import json

from db_handler import table_name, sql_conn


# Тестовые данные
SITES = [
    {
        "url": "https://www.google.ru/",
        "search_element": "q",
        "cookie": [
            {"name": "test1", "value": "test2"},
            {"name": "test3", "value": "test4"},
        ],
    },
    {
        "url": "https://yandex.ru/",
        "search_element": "text",
        "cookie": [{"name": "test5", "value": "test6"}],
    },
    {"url": "https://mail.ru/", "search_element": "q", "cookie": []},
    {"url": "https://duckduckgo.com/", "search_element": "q", "cookie": []},
    {"url": "https://www.bing.com/", "search_element": "q", "cookie": []},
    {"url": "h1", "search_element": "q", "cookie": []},
]

cursor = sql_conn.cursor()

cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
sql_conn.commit()

cursor.execute(
    f"""CREATE TABLE {table_name}
    (url TEXT, search_element TEXT, cookies TEXT);"""
)

for site in SITES:
    cookie = json.dumps(site["cookie"])
    cursor.execute(
        f"""INSERT INTO {table_name} VALUES
        ('{site["url"]}', '{site["search_element"]}', '{cookie}');"""
    )
sql_conn.commit()
