"""
    Модуль предоставляет api сравнения изображений

    author: https://github.com/egor43
"""

import statistics
from . import image_opener
from . import compare_tools
from . import helpers


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
    match_rates = compare_tools.image_match_rates(base_img, comparable_img)
    if statistics.mean(match_rates.values()) >= match_threshold_hash_percent:
        return True
    return False


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
    match_rate = compare_tools.orb_match_rate(base_img, comparable_img)
    if match_rate >= match_threshold_orb_percent:
        return True
    return False


def fast_image_compare(img_1_path, img_2_path, match_threshold_hash_percent=75):
    """
        Быстрое сравнение изображений по average hash и wavelet hash.
        Params:
            img_1_path - путь до изображения или url изображения
            img_2_path - путь до изображения или url изображения
            match_threshold_hash_percent - порог совпадения хешей с которого
                                           можно считать изображения похожими
        Return:
            bool - являются ли изображения похожими
    """
    img_1 = image_opener.get_img(img_1_path, is_gray_scale=True)
    img_2 = image_opener.get_img(img_2_path, is_gray_scale=True)
    return image_hash_compare(img_1, img_2, match_threshold_hash_percent)


def full_image_compare(img_1_path, img_2_path, match_threshold_hash_percent=75, match_threshold_orb_percent=60):
    """
        Сравнение изображений по average hash и wavelet hash.
        При негативном результате сравнения производится сравнение по соответствию ORB дескрипторов.
        Params:
            img_1_path - путь до изображения или url изображения
            img_2_path - путь до изображения или url изображения
            match_threshold_hash_percent - порог совпадения хешей с которого
                                           можно считать изображения похожими.
            match_threshold_orb_percent - порог совпадения ORB дескриторов с которого
                                          можно считать изображения похожими.
        Return:
            bool - являются ли изображения похожими
    """
    img_1 = image_opener.get_img(img_1_path, is_gray_scale=True)
    img_2 = image_opener.get_img(img_2_path, is_gray_scale=True)

    hash_compare = image_hash_compare(img_1, img_2, match_threshold_hash_percent)
    if hash_compare:
        return hash_compare
    # Оценку схожести по ORB используем только если не определили схожесть по хешам,
    # т.к. оценка схожести по ORB - достаточно затратная по времени операция
    return image_orb_compare(img_1, img_2, match_threshold_orb_percent)


def fast_grouping_similar_images(images, match_threshold_hash_percent=75):
    """
        Быстрая группировка похожих изображений по average hash и wavelet hash.
        Params:
            images - последовательность изображений
            match_threshold_hash_percent - порог совпадения хешей с которого
                                           можно считать изображения похожими.
        Return:
            list - 2D список сгруппированных похожих изображений.
                   [[img_from_group1, img_from_group1, ...],
                    [img_from_group2, img_from_group2, ...],
                    [...], ...]
    """
    pass
