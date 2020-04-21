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

    def test_full_image_compare(self):
        """
            Тестирование полного сравнения различных изображений 
        """
        self.assertFalse(compare_api.full_image_compare(self.img2_path, self.img3_path))
    
    def test_full_image_compare_equals(self):
        """
            Тестирование полного сравнения идентичных изображений 
        """
        self.assertTrue(compare_api.full_image_compare(self.img3_path, self.img3_path))
    
    def test_full_image_compare_similar(self):
        """
            Тестирование быстрого сравнения похожих изображений 
        """
        self.assertTrue(compare_api.full_image_compare(self.img4_path, self.img5_path))
