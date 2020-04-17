"""
    Модуль предоставляет api сравнения изображений

    author: https://github.com/egor43
"""

import statistics
from . import image_metrick
from . import image_opener
from . import helpers


def hash_match_rates(base_img, comparable_img, metricks=("avg", "wav")):
    """
        Степени совпадения хешей изображения
        Params:
            base_img - базовое изображение
            comparable_img - сравниваемое изображение
            metricks=("avg", "wav") - метрики, которые необходимо оценивать:
                               "avg" - average hash;
                               "per" - perceptual hash;
                               "wav" - wavelet hash;
                               "dif" - difference hash.
        Return:
            dict - словарь со степенями (в процентах)
                   совпадения хешей изображений.
                   Пример: {"avg": 14.59373, "wav": 100.0, ....}
    """
    base_img_metricks = image_metrick.image_metricks(base_img, metricks)
    comparable_img_metricks = image_metrick.image_metricks(comparable_img, metricks)

    result = {}
    for metrick_name, base_img_hash_value in base_img_metricks.items():
        difference_percent = image_metrick.hamming_distance_percent(base_img_hash_value,
                                                                    comparable_img_metricks[metrick_name])
        # Нам нужны проценты совпадений а не различий
        result[metrick_name] = 100 - difference_percent
    return result


def orb_match_rate(base_img, comparable_img):
    """
        Степени совпадения изображений по точкам ORB деткетора
        Params:
            base_img - базовое изображение
            comparable_img - сравниваемое изображение
        Return:
            double - степень совпадения (в процентах) изображений
                     на основе анализа точек детектора ORB
    """
    base_img_metricks = image_metrick.image_metricks(base_img, metricks=("orb",))
    comparable_img_metricks = image_metrick.image_metricks(comparable_img, metricks=("orb",))
    return image_metrick.match_descriptors_percent(base_img_metricks["orb"], comparable_img_metricks["orb"])


def fast_image_compare(img_1_path, img_2_path, match_threshold_percent=75):
    """
        Быстрое сравнение изображений по average hash и wavelet hash.
        Params:
            img_1_path - путь до изображения или url изображения
            img_2_path - путь до изображения или url изображения
            match_threshold_percent - порог совпадения хешей с которого
                                      можно считать изображения похожими
        Return:
            bool - являются ли изображения похожими
    """
    img_1 = image_opener.get_img(img_1_path, is_gray_scale=True)
    img_2 = image_opener.get_img(img_2_path, is_gray_scale=True)
    
    match_rates = hash_match_rates(img_1, img_2)
    if statistics.mean(match_rates.values()) >= match_threshold_percent:
        return True
    return False
