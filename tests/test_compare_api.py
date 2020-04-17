"""
    Модуль содержит юнит-тесты API методов модуля compare_api

    author: https://github.com/egor43
"""

import unittest
from image_comparsion import image_opener
from image_comparsion import compare_api


class TestCompareApi(unittest.TestCase):
    """
        Набор тестовых кейсов для тестирования функций модуля сравнения изображений
    """

    def setUp(self):
        """
            Подготовка необходимых данных
        """
        self.img1_path = "./tests/files/1.png"
        with open(self.img1_path, "rb") as image_bs:
            self.img1 = image_opener.get_img(image_bs, is_gray_scale=True)
    
        self.img2_path = "./tests/files/2.png"
        with open(self.img2_path, "rb") as image_bs:
            self.img2 = image_opener.get_img(image_bs, is_gray_scale=True)
    
    def test_hash_match_rates(self):
        """
            Тестирование получения степеней овпадения изображений
        """
        match_rates = compare_api.hash_match_rates(self.img1, self.img2)
        self.assertTrue(match_rates)
    
    def test_hash_match_rates_for_equals_img(self):
        """
            Тестирование получения 100% степеней совпадений для одинаковых изображений
        """
        match_rates = compare_api.hash_match_rates(self.img1, self.img1)
        self.assertTrue(all([rate == 100.0 for rate in match_rates.values()]))
    
    def test_hash_match_rates_for_not_equals_img(self):
        """
            Тестирование получения не 100% степеней совпадений для различных изображений
        """
        match_rates = compare_api.hash_match_rates(self.img1, self.img2)
        self.assertTrue(all([rate != 100.0 for rate in match_rates.values()]))

    def test_hash_match_rates_with_custom_metrick(self):
        """
            Тестирование получения степеней совпадения по указанным метрикам
        """
        metricks = ("dif", "avg", "per", "wav")
        match_rates = compare_api.hash_match_rates(self.img1, self.img2, metricks=metricks)
        self.assertTrue("dif" in match_rates)
        self.assertTrue("avg" in match_rates)
        self.assertTrue("per" in match_rates)
        self.assertTrue("wav" in match_rates)
