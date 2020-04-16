"""
    Модуль содержит юнит-тесты методов модуля image_metrick

    author: https://github.com/egor43
"""

import unittest
from image_comparsion import image_opener
from image_comparsion import image_metrick


class TestImageMetrick(unittest.TestCase):
    """
        Набор тестовых кейсов для тестирования получения метрик изображения
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
    
    
    def test_average_hash(self):
        """
            Тестирование получения average hash изображения
        """
        avg_hash = image_metrick.average_hash(self.img1)
        self.assertTrue(len(avg_hash.hash))

    def test_perceptual_hash(self):
        """
            Тестирование получения perceptual hash изображения
        """
        p_hash = image_metrick.perceptual_hash(self.img1)
        self.assertTrue(len(p_hash.hash))

    def test_wavelet_hash(self):
        """
            Тестирование получения wavelet hash изображения
        """
        w_hash = image_metrick.wavelet_hash(self.img1)
        self.assertTrue(len(w_hash.hash))

    def test_difference_hash(self):
        """
            Тестирование получения difference hash изображения
        """
        d_hash = image_metrick.difference_hash(self.img1)
        self.assertTrue(len(d_hash.hash))

    def test_orb_descriptors(self):
        """
            Тестирование получения orb дескрипторов изображения
        """
        orb_desc = image_metrick.orb_descriptors(self.img2)
        self.assertTrue(len(orb_desc))

    def test_hamming_distance(self):
        """
            Тестирование получения расстояния Хемминга
        """
        avg_hash_1 = image_metrick.average_hash(self.img1)
        avg_hash_2 = image_metrick.average_hash(self.img2)
        hamming_dist = image_metrick.hamming_distance(avg_hash_1, avg_hash_2)
        self.assertTrue(hamming_dist > 0)

    def test_hamming_distance_equal(self):
        """
            Тестирование получения нулевого расстояния Хемминга для одинаковых хешей
        """
        avg_hash_1 = image_metrick.average_hash(self.img1)
        hamming_dist = image_metrick.hamming_distance(avg_hash_1, avg_hash_1)
        self.assertEqual(hamming_dist, 0)

    def test_hamming_distance_raise_different_hash_length(self):
        """
            Тестирование получения исключения для различных размеров хешей
        """
        avg_hash_1 = image_metrick.average_hash(self.img1)
        avg_hash_2 = image_metrick.average_hash(self.img2, hash_size=64)
        self.assertRaises(AttributeError, image_metrick.hamming_distance, avg_hash_1, avg_hash_2)
