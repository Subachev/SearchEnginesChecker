from typing import Any, Dict, List

from db_handler import get_sites_data
from default_logger import console_logger

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys


class SearchEnginesChecker:
    """Проверка сайтов поисковых систем."""
    def __init__(self, page_load_timeout: int = 10) -> None:
        self.page_load_timeout = page_load_timeout

    def __enter__(self):
        """Инициализации контекста."""
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(self.page_load_timeout)
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """Финализация контекста."""
        self.driver.close()

    def check_site(
        self,
        url: str,
        search_element: str,
        cookies: List[Dict[str, Any]],
        search_query: str,
    ) -> None:
        """Проверка сайта.

        Args:
            url: сайт.
            search_element: имя элемента поиска.
            cookies: список словарей с куками.
            search_query: строка с поисковым запросом.
        """
        self.driver.get(url)

        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.get(url)
        element = self.driver.find_element_by_name(search_element)
        element.clear()
        element.send_keys(search_query)
        element.send_keys(Keys.ENTER)


with SearchEnginesChecker() as checker:
    for site_data in get_sites_data():
        url = site_data["url"]
        try:
            checker.check_site(**site_data, search_query="hello world")
            console_logger.info(f"{url} - success")
        except TimeoutException:
            console_logger.info(f"{url} - missed by timeout")
        except WebDriverException as err:
            console_logger.info(f"{url} - failed. Error: {err}")
