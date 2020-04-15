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
    def test_get_image_empty_raise(self):
        """
            Тестирование получения исключения при передаче пустого байтового потока
        """
        empty_byte_stream = io.BytesIO(b'')
        self.assertRaises(PIL.UnidentifiedImageError, image_opener.get_img, empty_byte_stream)

    def test_get_image(self):
        """
            Тестирование получения изображения
        """
        with open("./tests/files/1.png", "rb") as img_byte_stream:
            img = image_opener.get_img(img_byte_stream)
            self.assertTrue(img.getdata())
    
    def test_get_image_gray_scale(self):
        """
            Тестирование получения изображения в оттенках серого
        """
        with open("./tests/files/1.png", "rb") as img_byte_stream:
            img = image_opener.get_img(img_byte_stream, is_gray_scale=True)
            self.assertEqual(img.mode, "L")
    
    def test_get_image_rgb(self):
        """
            Тестирование получения изображения в rgb
        """
        with open("./tests/files/1.png", "rb") as img_byte_stream:
            img = image_opener.get_img(img_byte_stream)
            self.assertEqual(img.mode, "RGB")
