"""
    Модуль содержит юнит-тесты инструментов модуля compare_tools

    author: https://github.com/egor43
"""

import unittest
from image_comparsion import image_opener
from image_comparsion import image_metrick
from image_comparsion import compare_tools


class TestCompareTools(unittest.TestCase):
    """
        Набор тестовых кейсов для тестирования функций 
        модуля дополнительного инструментария сравнения изображений
    """

    def setUp(self):
        """
            Подготовка необходимых данных
        """
        self.img1_path = "./tests/files/1.png"
        with open(self.img1_path, "rb") as image_bs:
            self.img1 = image_opener.get_img_from_byte_stream(image_bs, is_gray_scale=True)
    
        self.img2_path = "./tests/files/2.png"
        with open(self.img2_path, "rb") as image_bs:
            self.img2 = image_opener.get_img_from_byte_stream(image_bs, is_gray_scale=True)
        
        self.img3_path = "./tests/files/3.png"
        with open(self.img3_path, "rb") as image_bs:
            self.img3 = image_opener.get_img_from_byte_stream(image_bs, is_gray_scale=True)
        
        self.img4_path = "./tests/files/4.png"
        self.img5_path = "./tests/files/5.png"
    
    def test_hash_match_rates(self):
        """
            Тестирование получения степеней cовпадения хешей изображений
        """
        metricks=("avg", "wav")
        img1_hashes = image_metrick.image_metricks(self.img1, metricks)
        img2_hashes = image_metrick.image_metricks(self.img2, metricks)
        match_rates = compare_tools.hash_match_rates(img1_hashes, img2_hashes)
        self.assertTrue(match_rates)
    
    def test_hash_match_rates_len(self):
        """
            Тестирование количества хешей изображений, возвращаемое 
            при вычислении степеней совпадения
        """
        metricks=("avg", "wav", "dif")
        img1_hashes = image_metrick.image_metricks(self.img1, metricks)
        img2_hashes = image_metrick.image_metricks(self.img2, metricks)
        match_rates = compare_tools.hash_match_rates(img1_hashes, img2_hashes)
        self.assertEqual(len(match_rates), len(metricks))
    
    def test_hash_match_rates_custom_metrick(self):
        """
            Тестирование получения сепеней совпадения указанных метрик
        """
        metricks=("wav", "dif")
        img1_hashes = image_metrick.image_metricks(self.img1, metricks)
        img2_hashes = image_metrick.image_metricks(self.img2, metricks)
        match_rates = compare_tools.hash_match_rates(img1_hashes, img2_hashes)
        self.assertTrue("wav" in match_rates)
        self.assertTrue("dif" in match_rates)

    def test_hash_match_rates_empty(self):
        """
            Тестирование получения степеней cовпадения пустых хешей изображений
        """
        match_rates = compare_tools.hash_match_rates({}, {})
        self.assertFalse(match_rates)

    def test_image_match_rates(self):
        """
            Тестирование получения степеней овпадения изображений
        """
        match_rates = compare_tools.image_match_rates(self.img1, self.img2)
        self.assertTrue(match_rates)
    
    def test_image_match_rates_for_equals_img(self):
        """
            Тестирование получения 100% степеней совпадений для одинаковых изображений
        """
        match_rates = compare_tools.image_match_rates(self.img1, self.img1)
        self.assertTrue(all([rate == 100.0 for rate in match_rates.values()]))
    
    def test_image_match_rates_for_not_equals_img(self):
        """
            Тестирование получения не 100% степеней совпадений для различных изображений
        """
        match_rates = compare_tools.image_match_rates(self.img1, self.img2)
        self.assertTrue(all([rate != 100.0 for rate in match_rates.values()]))

    def test_image_match_rates_with_custom_metrick(self):
        """
            Тестирование получения степеней совпадения по указанным метрикам
        """
        metricks = ("dif", "avg", "per", "wav")
        match_rates = compare_tools.image_match_rates(self.img1, self.img2, metricks=metricks)
        self.assertTrue("dif" in match_rates)
        self.assertTrue("avg" in match_rates)
        self.assertTrue("per" in match_rates)
        self.assertTrue("wav" in match_rates)
    
    def test_orb_match_rate(self):
        """
            Тестирование получения процента совпадения изображений по дескрипторам ORB детектора
        """
        match_percent = compare_tools.orb_match_rate(self.img2, self.img3)
        self.assertTrue(match_percent >= 0 and match_percent <= 100)

    def test_orb_match_rate_for_equals_img(self):
        """
            Тестирование получения близкого к 100% совпадения одинаковых изображений по дескрипторам ORB детектора
        """
        match_percent = compare_tools.orb_match_rate(self.img2, self.img2)
        self.assertTrue(match_percent >= 97 and match_percent <= 100)