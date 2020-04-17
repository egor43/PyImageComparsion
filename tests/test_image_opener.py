"""
    Модуль содержит юнит-тесты методов модуля image_opener

    author: https://github.com/egor43
"""

import unittest
import io
import PIL
from image_comparsion import image_opener


class TestImageOpener(unittest.TestCase):
    """
        Набор тестовых кейсов для тестирования получения изображений
    """

    def setUp(self):
        """
            Подготовка необходимых данных
        """
        self.img_path = "./tests/files/1.png"
        self.img_url = "https://pythonworld.ru/m/img/python-3.png"

    def test_get_img_from_byte_stream_empty_raise(self):
        """
            Тестирование получения исключения при передаче пустого байтового потока
        """
        empty_byte_stream = io.BytesIO(b'')
        self.assertRaises(PIL.UnidentifiedImageError, image_opener.get_img_from_byte_stream, empty_byte_stream)

    def test_get_img_from_byte_stream(self):
        """
            Тестирование получения изображения
        """
        with open(self.img_path, "rb") as img_byte_stream:
            img = image_opener.get_img_from_byte_stream(img_byte_stream)
            self.assertTrue(img.getdata())
    
    def test_get_img_from_byte_stream_gray_scale(self):
        """
            Тестирование получения изображения в оттенках серого
        """
        with open(self.img_path, "rb") as img_byte_stream:
            img = image_opener.get_img_from_byte_stream(img_byte_stream, is_gray_scale=True)
            self.assertEqual(img.mode, "L")
    
    def test_get_img_from_byte_stream_not_gray_scale(self):
        """
            Тестирование получения изображения в цветном режиме
        """
        with open(self.img_path, "rb") as img_byte_stream:
            img = image_opener.get_img_from_byte_stream(img_byte_stream)
            self.assertNotEqual(img.mode, "L")

    def test_get_img_from_url_empty_raise(self):
        """
            Тестирование получения исключения при получении некорректного изображения по url
        """
        image_url = "https://ya.ru"
        self.assertRaises(PIL.UnidentifiedImageError, image_opener.get_img_from_url, image_url)
    
    def test_get_img_from_url(self):
        """
            Тестирование получения изображения по url
        """
        img = image_opener.get_img_from_url(self.img_url)
        self.assertTrue(img.getdata())

    def test_get_img_from_url_gray_scale(self):
        """
            Тестирование получения изображения по url в оттенках серого
        """
        img = image_opener.get_img_from_url(self.img_url, is_gray_scale=True)
        self.assertEqual(img.mode, "L")
        
    def test_get_img_from_url_not_gray_scale(self):
        """
            Тестирование получения изображения по url в цветном режиме
        """
        img = image_opener.get_img_from_url(self.img_url)
        self.assertNotEqual(img.mode, "L")

    def test_get_img_by_path(self):
        """
            Тестирование получения изображения по пути
        """
        img = image_opener.get_img(self.img_path)
        self.assertTrue(img.getdata())
    
    def test_get_img_by_url(self):
        """
            Тестирование получения изображения по url
        """
        img = image_opener.get_img(self.img_url)
        self.assertTrue(img.getdata())
    
    def test_get_img_by_path_gray_scale(self):
        """
            Тестирование получения изображения оттенках серого
        """
        img = image_opener.get_img(self.img_path, is_gray_scale=True)
        self.assertEqual(img.mode, "L")
    
    def test_get_img_by_url_gray_scale(self):
        """
            Тестирование получения изображения по url в цветном режиме
        """
        img = image_opener.get_img(self.img_url)
        self.assertNotEqual(img.mode, "L")
