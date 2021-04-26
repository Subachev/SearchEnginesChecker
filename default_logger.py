import logging
import os


def _get_console_logger() -> logging.Logger:
    """Получение консольного логгера.

    Returns:
        Консольный логгер.
    """
    hostname = os.getenv("HOSTNAME")
    fmt = f"[%(asctime)s] - {hostname} - %(levelname)s - %(message)s"

    logger = logging.getLogger("console")
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter(fmt))
    logger.addHandler(ch)

    return logger


console_logger = _get_console_logger()
