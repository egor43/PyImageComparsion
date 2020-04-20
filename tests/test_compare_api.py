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

    def test_image_hash_compare(self):
        """
            Тестирование определения схожести хешей изображений
        """
        match_threshold_hash_percent = 75
        self.assertFalse(compare_api.image_hash_compare(self.img1, self.img2, match_threshold_hash_percent))

    def test_image_hash_compare_low_threshold_percent(self):
        """
            Тестирование определения схожести различных хешей изображений при условии низкого порога точности
        """
        match_threshold_hash_percent = 0
        self.assertTrue(compare_api.image_hash_compare(self.img1, self.img2, match_threshold_hash_percent))

    def test_image_hash_compare_max_threshold_percent(self):
        """
            Тестирование определения схожести идентичных хешей изображений при условии 100% порога точности
        """
        match_threshold_hash_percent = 100
        self.assertTrue(compare_api.image_hash_compare(self.img2, self.img2, match_threshold_hash_percent))

    def test_orb_match_rate(self):
        """
            Тестирование получения процента совпадения изображений по дескрипторам ORB детектора
        """
        match_percent = compare_api.orb_match_rate(self.img2, self.img3)
        self.assertTrue(match_percent >= 0 and match_percent <= 100)

    def test_orb_match_rate_for_equals_img(self):
        """
            Тестирование получения близкого к 100% совпадения одинаковых изображений по дескрипторам ORB детектора
        """
        match_percent = compare_api.orb_match_rate(self.img2, self.img2)
        self.assertTrue(match_percent >= 97 and match_percent <= 100)
    
    def test_image_orb_compare(self):
        """
            Тестирование определения схожести ORB дескирпторов изображений
        """
        match_threshold_orb_percent = 75
        self.assertFalse(compare_api.image_orb_compare(self.img2, self.img3, match_threshold_orb_percent))
    
    def test_image_orb_compare_low_threshold_percent(self):
        """
            Тестирование определения схожести различных ORB дескирпторов изображений при условии низкого порога точности
        """
        match_threshold_orb_percent = 0
        self.assertTrue(compare_api.image_orb_compare(self.img2, self.img3, match_threshold_orb_percent))

    def test_image_orb_compare_high_threshold_percent(self):
        """
            Тестирование определения схожести идентичных ORB дескирпторов изображений при условии высокого порога точности
        """
        match_threshold_orb_percent = 98
        self.assertTrue(compare_api.image_orb_compare(self.img2, self.img2, match_threshold_orb_percent))

    def test_fast_image_compare(self):
        """
            Тестирование быстрого сравнения различных изображений 
        """
        self.assertFalse(compare_api.fast_image_compare(self.img1_path, self.img2_path))
    
    def test_fast_image_compare_equals(self):
        """
            Тестирование быстрого сравнения идентичных изображений 
        """
        self.assertTrue(compare_api.fast_image_compare(self.img2_path, self.img2_path))
    
    def test_fast_image_compare_similar(self):
        """
            Тестирование быстрого сравнения похожих изображений 
        """
        self.assertTrue(compare_api.fast_image_compare(self.img4_path, self.img5_path))
