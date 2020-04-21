"""
    Модуль предоставляет вспомогательные инструменты

    author: https://github.com/egor43
"""

import statistics
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


def max_image(images):
    """
        Возвращает изображение с максимальным размером (разрешением)
        Params:
            images - последовательность изображений
        Return:
            Image - изображение с максимальным размером 
    """
    return max(images, key=lambda img: img.width * img.height, default=None)


def is_avg_exceeded_threshold(seq, threshold, strict_equality=False):
    """
        Проверяет, превысило ли среднее значение последовательности 
        определенный порог
        Params:
            seq - последовательность значений
            threshold - порог значения, превышение которого проверяется
            strict_equality - флаг определяющий строгое/нестрогое равенство
                              при сравнении с пороговым значением
        Return:
            bool - превысило ли среднее значение последовательности заданный порог
    """
    if not seq:
        return False

    avg_value = statistics.mean(seq)
    if strict_equality:
        compare_method = getattr(avg_value, "__gt__")
    else:
        compare_method = getattr(avg_value, "__ge__")
    return compare_method(threshold)
