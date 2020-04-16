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
