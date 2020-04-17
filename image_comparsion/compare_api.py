"""
    Модуль предоставляет api сравнения изображений

    author: https://github.com/egor43
"""

from . import image_metrick


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
    base_img_hashes = image_metrick.image_metricks(base_img, metricks)
    comparable_img_hashes = image_metrick.image_metricks(comparable_img, metricks)

    result = {}
    for metrick_name, base_img_hash_value in base_img_hashes.items():
        difference_percent = image_metrick.hamming_distance_percent(base_img_hash_value,
                                                                    comparable_img_hashes[metrick_name])
        # Нам нужны проценты совпадений а не различий
        result[metrick_name] = 100 - difference_percent
    return result
