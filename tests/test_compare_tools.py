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
            self.img1 = image_opener.get_img_from_byte_stream(image_bs)
    
        self.img2_path = "./tests/files/2.png"
        with open(self.img2_path, "rb") as image_bs:
            self.img2 = image_opener.get_img_from_byte_stream(image_bs)
        
        self.img3_path = "./tests/files/3.png"
        with open(self.img3_path, "rb") as image_bs:
            self.img3 = image_opener.get_img_from_byte_stream(image_bs)
        
        self.img4_path = "./tests/files/4.png"
        with open(self.img4_path, "rb") as image_bs:
            self.img4 = image_opener.get_img_from_byte_stream(image_bs)
        
        self.img5_path = "./tests/files/5.png"
        with open(self.img5_path, "rb") as image_bs:
            self.img5 = image_opener.get_img_from_byte_stream(image_bs)
  
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
    
    def test_image_hash_compare(self):
        """
            Тестирование определения схожести хешей изображений
        """
        match_threshold_hash_percent = 75
        self.assertFalse(compare_tools.image_hash_compare(self.img1, self.img2, match_threshold_hash_percent))

    def test_image_hash_compare_low_threshold_percent(self):
        """
            Тестирование определения схожести различных хешей изображений при условии низкого порога точности
        """
        match_threshold_hash_percent = 0
        self.assertTrue(compare_tools.image_hash_compare(self.img1, self.img2, match_threshold_hash_percent))

    def test_image_hash_compare_max_threshold_percent(self):
        """
            Тестирование определения схожести идентичных хешей изображений при условии 100% порога точности
        """
        match_threshold_hash_percent = 100
        self.assertTrue(compare_tools.image_hash_compare(self.img2, self.img2, match_threshold_hash_percent))
    
    def test_image_orb_compare(self):
        """
            Тестирование определения схожести ORB дескирпторов изображений
        """
        match_threshold_orb_percent = 75
        self.assertFalse(compare_tools.image_orb_compare(self.img2, self.img3, match_threshold_orb_percent))
    
    def test_image_orb_compare_low_threshold_percent(self):
        """
            Тестирование определения схожести различных ORB дескирпторов изображений при условии низкого порога точности
        """
        match_threshold_orb_percent = 0
        self.assertTrue(compare_tools.image_orb_compare(self.img2, self.img3, match_threshold_orb_percent))

    def test_image_orb_compare_high_threshold_percent(self):
        """
            Тестирование определения схожести идентичных ORB дескирпторов изображений при условии высокого порога точности
        """
        match_threshold_orb_percent = 98
        self.assertTrue(compare_tools.image_orb_compare(self.img2, self.img2, match_threshold_orb_percent))
    
    def test_hash_metrick_compare(self):
        """
            Тестирование определения схожести метрик (описывающих хешей) двух изображений.
        """
        img2_metricks = image_metrick.image_metricks(self.img2)
        img3_metricks = image_metrick.image_metricks(self.img3)
        self.assertFalse(compare_tools.hash_metrick_compare(img2_metricks, img3_metricks))

    def test_hash_metrick_compare_equals(self):
        """
            Тестирование определения схожести метрик (описывающих хешей) двух одинаковых изображений.
        """
        img2_metricks = image_metrick.image_metricks(self.img2)
        self.assertTrue(compare_tools.hash_metrick_compare(img2_metricks, img2_metricks))

    def test_orb_metrick_compare(self):
        """
            Тестирование определения схожести метрик (orb дескрипторов) двух изображений.
        """
        img2_metricks = image_metrick.image_metricks(self.img2)
        img3_metricks = image_metrick.image_metricks(self.img3)
        self.assertFalse(compare_tools.orb_metrick_compare(img2_metricks, img3_metricks))

    def test_orb_metrick_compare_equals(self):
        """
            Тестирование определения схожести метрик (orb дескрипторов) двух одинаковых изображений.
        """
        img2_metricks = image_metrick.image_metricks(self.img2)
        self.assertTrue(compare_tools.orb_metrick_compare(img2_metricks, img2_metricks))

    def test_grouping_similar_images(self):
        """
            Тестирование группировки похожих изображений
        """
        images = [self.img2, self.img3, self.img4, self.img5]
        for group in compare_tools.grouping_similar_images(images):
            self.assertTrue(len(group) > 0)
    
    def test_grouping_similar_images_equal(self):
        """
            Тестирование группировки похожих изображений.
            В случае одинаковых изображений
        """
        images = [self.img2, self.img2, self.img2, self.img2]
        for group in compare_tools.grouping_similar_images(images):
            self.assertTrue(len(group) == len(images))
    
    def test_grouping_similar_images_without_orb(self):
        """
            Тестирование группировки похожих изображений.
            В случае группировки без использования orb дескрипторов
        """
        images = [self.img2, self.img3, self.img4, self.img5]
        for group in compare_tools.grouping_similar_images(images, with_orb_comparsion=False):
            self.assertTrue(len(group) > 0)
    
    def test_grouping_similar_images_equal_without_orb(self):
        """
            Тестирование группировки похожих изображений.
            В случае одинаковых изображений и группировки без использования orb дескрипторов
        """
        images = [self.img2, self.img2, self.img2, self.img2]
        for group in compare_tools.grouping_similar_images(images, with_orb_comparsion=False):
            self.assertTrue(len(group) == len(images))
