"""
    Модуль содержит юнит-тесты методов модуля helpers

    author: https://github.com/egor43
"""

import unittest
from image_comparsion import helpers


class TestHelpers(unittest.TestCase):
    """
        Набор тестовых кейсов для тестирования вспомогательных инструментов
    """

    def test_is_url_valid(self):
        """
            Тестирование корректного определения правильного url
        """
        self.assertTrue(helpers.is_url("https://yandex.ru/"))
        self.assertTrue(helpers.is_url("http://yandex.ru/"))
        self.assertTrue(helpers.is_url("HTTPS://yandex.ru/"))
        self.assertTrue(helpers.is_url("HTTP://yandex.ru/"))
    
    def test_is_url_invalid(self):
        """
            Тестирование корректного определения неправильного url
        """
        self.assertFalse(helpers.is_url("ftp://yandex.ru/"))
        self.assertFalse(helpers.is_url("/yandex.ru/"))
        self.assertFalse(helpers.is_url("files/1.png"))
        self.assertFalse(helpers.is_url("http/2.ru"))
    
    