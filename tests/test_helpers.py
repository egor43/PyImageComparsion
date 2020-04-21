"""
    Модуль содержит юнит-тесты методов модуля helpers

    author: https://github.com/egor43
"""

import unittest
from image_comparsion import helpers
from image_comparsion import image_opener


class TestHelpers(unittest.TestCase):
    """
        Набор тестовых кейсов для тестирования вспомогательных инструментов
    """
    
    def setUp(self):
        """
            Подготовка необходимых данных
        """
        self.img1_path = "./tests/files/1.png"
        self.img1 = image_opener.get_img(self.img1_path, is_gray_scale=True)
    
        self.img2_path = "./tests/files/2.png"
        self.img2 = image_opener.get_img(self.img2_path, is_gray_scale=True)
        
        self.img3_path = "./tests/files/3.png"
        self.img3 = image_opener.get_img(self.img3_path, is_gray_scale=True)

        self.img4_path = "./tests/files/4.png"
        self.img4 = image_opener.get_img(self.img4_path, is_gray_scale=True)

        self.img5_path = "./tests/files/5.png"
        self.img5 = image_opener.get_img(self.img5_path, is_gray_scale=True)

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
    
    def test_max_image(self):
        """
            Темтирование получения изображения максимального размера
        """
        images = [self.img1, self.img2, self.img3, self.img4, self.img5]
        max_image = helpers.max_image(images)
        self.assertEqual(max_image, self.img5)
    
    def test_max_image_empty_seq(self):
        """
            Темтирование получения изображения максимального размера из пустого списка
        """
        images = []
        max_image = helpers.max_image(images)
        self.assertEqual(max_image, None)

    def test_is_avg_exceeded_threshold(self):
        """
            Тестирование проверки превышения средним значением последовательности
            заданного порогового значения
        """
        seq = [3, 3, 3]
        self.assertTrue(helpers.is_avg_exceeded_threshold(seq, 2))
    
    def test_is_avg_exceeded_threshold_positive(self):
        """
            Тестирование проверки превышения средним значением последовательности
            заданного порогового значения.
            В случае нестрогого равенства.
        """
        seq = [2, 2, 2]
        self.assertTrue(helpers.is_avg_exceeded_threshold(seq, 2))
    
    def test_is_avg_exceeded_threshold_negative(self):
        """
            Тестирование проверки превышения средним значением последовательности
            заданного порогового значения.
            В случае не превышения порогового значения
        """
        seq = [1, 1, 1]
        self.assertFalse(helpers.is_avg_exceeded_threshold(seq, 2))
    
    def test_is_avg_exceeded_threshold_empty(self):
        """
            Тестирование проверки превышения средним значением последовательности
            заданного порогового значения. 
            В случае пустой последовательности
        """
        self.assertFalse(helpers.is_avg_exceeded_threshold([], 2))
    
    def test_is_avg_exceeded_threshold_strict(self):
        """
            Тестирование проверки превышения средним значением последовательности
            заданного порогового значения.
            В случае строгого равенства и не превышения порогового значения
        """
        seq = [2, 2, 2]
        self.assertFalse(helpers.is_avg_exceeded_threshold(seq, 2, strict_equality=True))
    
    def test_is_avg_exceeded_threshold_strict_positive(self):
        """
            Тестирование проверки превышения средним значением последовательности
            заданного порогового значения. 
            В случае строгого равенства
        """
        seq = [3, 3, 3]
        self.assertTrue(helpers.is_avg_exceeded_threshold(seq, 2, strict_equality=True))
