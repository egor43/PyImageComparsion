"""
    Модуль предоставляет инструменты получения метрик изображений

    author: https://github.com/egor43
"""

import imagehash
from skimage.feature import ORB


def average_hash(img, hash_size=128):
    """
        Вычисление average hash.
        Params:
            img - изображение
            hash_size - размер хеша
        Return:
            ImageHash - объект представляющий хеш изображения
    """
    return imagehash.average_hash(img, hash_size)


def perceptual_hash(img, hash_size=128):
    """
        Вычисление perceptual hash.
        Params:
            img - изображение
            hash_size - размер хеша
        Return:
            ImageHash - объект представляющий хеш изображения
    """
    return imagehash.phash(img, hash_size)


def wavelet_hash(img, hash_size=128):
    """
        Вычисление wavelet hash.
        Params:
            img - изображение
            hash_size - размер хеша
        Return:
            ImageHash - объект представляющий хеш изображения
    """
    return imagehash.whash(img, hash_size)


def difference_hash(img, hash_size=128):
    """
        Вычисление difference hash.
        Params:
            img - изображение
            hash_size - размер хеша
        Return:
            ImageHash - объект представляющий хеш изображения
    """
    return imagehash.dhash(img, hash_size)


def orb_descriptors(img, keypoints=800):
    """
        Вычисление ORB дескрипторов.
        Params:
            img - изображение
            keypoints - максимальное количество точек детектора
        Return:
            np.array - массив дескрипторов (как минмум двумерный)
    """
    extractor = ORB(n_keypoints=keypoints)
    extractor.detect_and_extract(img)
    return extractor.descriptors


def hamming_distance(first_hash, second_hash):
    """
        Вычисление расстояния Хемминга между двумя хешами.
        Params:
            first_hash - хеш изображения
            second_hash - хеш изображения
        Return:
            int - расстояние Хемминга
    """
    if len(first_hash.hash) == len(second_hash.hash):
        return first_hash - second_hash
    raise AttributeError("Хеши изображений имеют различную длину")


def image_metricks(img, metricks=("all",)):
    """
        Получение метрик изображения.
        Params:
            img - изображение
            metricks=("all",) - метрики, которые необходимо получить:
                               "all" - все метрики;
                               "avg" - average hash;
                               "per" - perceptual hash;
                               "wav" - wavelet hash;
                               "dif" - difference hash;
                               "orb" - ORB descriptors.
        Return:
            dict - словарь с вычисленными метриками.
                   Пример: {"avg": ...., "wav": ....}
    """
    result = {}
    
    if "avg" in metricks or "all" in metricks:
        result["avg"] = average_hash(img)
    if "per" in metricks or "all" in metricks:
        result["per"] = perceptual_hash(img)
    if "wav" in metricks or "all" in metricks:
        result["wav"] = wavelet_hash(img)
    if "dif" in metricks or "all" in metricks:
        result["dif"] = difference_hash(img)
    if "orb" in metricks or "all" in metricks:
        result["orb"] = orb_descriptors(img)
    
    return result
