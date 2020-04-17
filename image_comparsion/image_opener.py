"""
    Модуль предоставляет инструменты открытия изображений из различных источников
    и преобразование их к стандартным объектам PIL.Image.Image 

    author: https://github.com/egor43
"""

import requests
from PIL import Image


def get_img_from_path(binary_stream, is_gray_scale=False):
    """
        Возвращает изображение.
        Params:
            binary_stream - бинарный поток данных изображения
            is_gray_scale - флаг определяющий необходимость преобразования
                            изображения в оттенки серого (черно-белое)
        Return:
            PIL.Image.Image - изображение
    """
    image = Image.open(binary_stream)
    if is_gray_scale:
        image = image.convert("L")
    return image


def get_img_from_url(image_url, is_gray_scale=False):
    """
        Возвращает изображение полученное по переданному url.
        Params:
            image_url - url адрес изображения
            is_gray_scale - флаг определяющий необходимость преобразования
                            изображения в оттенки серого (черно-белое)
        Return:
            PIL.Image.Image - изображение
    """
    response = requests.get(image_url, stream=True)
    return get_img_from_path(response.raw, is_gray_scale)
