"""
    Модуль предоставляет инструменты сравнения изображений

    author: https://github.com/egor43
"""

from . import constants
from . import image_metrick
from . import helpers


def hash_match_rates(base_img_hashes, comparable_img_hashes):
    """
        Возвращает степени совпадения хешей изображений
        Params:
            base_img_hashes - словарь с хешами базового изображения
            comparable_img_hashes - словарь с хешами сравниваемого изображения
        Return:
            dict - словарь со степенями (в процентах)
                   совпадения хешей изображений.
                   Пример: {"avg": 14.59373, "wav": 100.0, ....}
    """
    result = {}
    for metrick_name, base_img_hash_value in base_img_hashes.items():
        difference_percent = image_metrick.hamming_distance_percent(base_img_hash_value,
                                                                    comparable_img_hashes[metrick_name])
        # Нам нужны проценты совпадений а не различий
        result[metrick_name] = 100 - difference_percent
    return result


def image_match_rates(base_img, comparable_img, metricks=constants.DEFAULT_HASHES):
    """
        Степени совпадения хешей изображений
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
    return hash_match_rates(base_img_metricks, comparable_img_metricks)


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


def image_hash_compare(base_img, comparable_img, match_threshold_hash_percent):
    """
        Определение схожести двух изображений по average hash и wavelet hash.
        Params:
            base_img - базовое изображение
            comparable_img - сравниваемое изображение
            match_threshold_hash_percent - порог совпадения хешей с которого
                                           можно считать изображения похожими
        Return:
            bool - являются ли изображения похожими
    """
    match_rates = image_match_rates(base_img, comparable_img)
    return helpers.is_avg_exceeded_threshold(match_rates.values(), match_threshold_hash_percent)


def image_orb_compare(base_img, comparable_img, match_threshold_orb_percent):
    """
        Определение схожести двух изображений по совпадениям точек ORB детектора.
        Params:
            base_img - базовое изображение
            comparable_img - сравниваемое изображение
            match_threshold_orb_percent - порог совпадения ORB дескриторов с которого
                                          можно считать изображения похожими
        Return:
            bool - являются ли изображения похожими
    """
    match_rate = orb_match_rate(base_img, comparable_img)
    return helpers.is_avg_exceeded_threshold([match_rate], match_threshold_orb_percent)


def hash_metrick_compare(base_metricks, comparable_metricks, 
                         match_threshold_hash_percent=constants.MATCH_THRESHOLD_HASH_PERCENT):
    """
        Определение схожести двух метрик по хешам
        Params:
            base_metricks - метрики базового изображения
            comparable_metricks - метрики сравниваемого изображения
            match_threshold_hash_percent - порог совпадения хешей с которого
                                           можно считать изображения похожими
        Return:
            bool - являются ли метрики (хешей) изображений похожими
    """
    base_hash_metricks = helpers.filter_metrick(base_metricks, constants.DEFAULT_HASHES)
    comparable_hash_metricks = helpers.filter_metrick(comparable_metricks, constants.DEFAULT_HASHES)
    match_rates = hash_match_rates(base_hash_metricks, comparable_hash_metricks)
    return helpers.is_avg_exceeded_threshold(match_rates.values(), match_threshold_hash_percent)


def orb_metrick_compare(base_metricks, comparable_metricks, 
                         match_threshold_orb_percent=constants.MATCH_THRESHOLD_ORB_PERCENT):
    """
        Определение схожести двух метрик по orb дескрипторам
        Params:
            base_metricks - метрики базового изображения
            comparable_metricks - метрики сравниваемого изображения
            match_threshold_orb_percent - порог совпадения ORB дескрипторов с которого
                                           можно считать изображения похожими
        Return:
            bool - являются ли метрики (ORB дескритпоров) изображений похожими
    """
    match_rate = image_metrick.match_descriptors_percent(base_metricks["orb"], comparable_metricks["orb"])
    return helpers.is_avg_exceeded_threshold([match_rate], match_threshold_orb_percent)


#TODO: Дописать метод стравниения orb метрик (если нужно)


