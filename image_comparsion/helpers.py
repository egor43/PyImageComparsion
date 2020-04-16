"""
    Модуль предоставляет вспомогательные инструменты

    author: https://github.com/egor43
"""

from urllib.parse import urlparse


def is_url(check_str):
    """
        Является ли переданная строка валидным url адресом.
        Проверяется наличие схемы: http или https
        Params:
            check_str - строка для проверки
        Return:
            bool - является ли переданная строка url со схемой http или https 
    """
    url_parts = urlparse(check_str)
    return url_parts.scheme in ("http", "https")
        