"""
    Модуль предоставляет инструменты получения метрик изображений

    author: https://github.com/egor43
"""

import imagehash
import skimage


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
