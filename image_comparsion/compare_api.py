"""
    Модуль предоставляет api сравнения изображений

    author: https://github.com/egor43
"""

from . import constants
from . import image_opener
from . import compare_tools


def fast_image_compare(img_1_path, img_2_path,
                       match_threshold_hash_percent=constants.MATCH_THRESHOLD_HASH_PERCENT):
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
    img_1 = image_opener.get_img(img_1_path)
    img_2 = image_opener.get_img(img_2_path)
    return compare_tools.image_hash_compare(img_1, img_2, match_threshold_hash_percent)


def full_image_compare(img_1_path, img_2_path, 
                       match_threshold_hash_percent=constants.MATCH_THRESHOLD_HASH_PERCENT,
                       match_threshold_orb_percent=constants.MATCH_THRESHOLD_ORB_PERCENT):
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
    img_1 = image_opener.get_img(img_1_path)
    img_2 = image_opener.get_img(img_2_path)

    hash_compare = compare_tools.image_hash_compare(img_1, img_2, match_threshold_hash_percent)
    if hash_compare:
        return hash_compare
    # Оценку схожести по ORB используем только если не определили схожесть по хешам,
    # т.к. оценка схожести по ORB - достаточно затратная по времени операция
    return compare_tools.image_orb_compare(img_1, img_2, match_threshold_orb_percent)


def fast_grouping_similar_images(image_paths, match_threshold_hash_percent=constants.MATCH_THRESHOLD_HASH_PERCENT):
    """
        Быстрая группировка изображений на основании хешей.
        Возвращает генератор.
        Params:
            image_paths - список путей или url'ов к изображениям
            match_threshold_hash_percent - порог совпадения хешей с которого
                                           можно считать изображения похожими
        Return:
            list - группа похожих изображений.
    """
    images = image_opener.get_images(image_paths)
    yield from compare_tools.grouping_similar_images(images, match_threshold_hash_percent, with_orb_comparsion=False)


def full_grouping_similar_images(image_paths, 
                                 match_threshold_hash_percent=constants.MATCH_THRESHOLD_HASH_PERCENT,
                                 match_threshold_orb_percent=constants.MATCH_THRESHOLD_ORB_PERCENT):
    """
        Группировка изображений на основании хешей и orb дескриторов.
        Из-за проверки совпадения orb дескрипторов метод работает медленно.
        Возвращает генератор.
        Params:
            image_paths - список путей или url'ов к изображениям
            match_threshold_hash_percent - порог совпадения хешей с которого
                                           можно считать изображения похожими
            match_threshold_orb_percent - порог совпадения ORB дескриторов с которого
                                          можно считать изображения похожими.
        Return:
            list - группа похожих изображений.
    """
    images = image_opener.get_images(image_paths)
    yield from compare_tools.grouping_similar_images(images, 
                                                     match_threshold_hash_percent,
                                                     match_threshold_orb_percent)
