"""
    Модуль предоставляет функционал для преобразования входящих изображений
    в необходимое представление.

    author: https://github.com/egor43
"""

import requests
from PIL import Image


def get_img(binary_stream, is_gray_scale=False):
    """
        Возвращает изображение.
        Params:
            binary_stream - бинарный поток данных изображения
            is_gray_scale - флаг определяющий необходимость преобразования
                            изображения в оттенки серого (черно-белое)
        Return:
            PIL.Image - изображение
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
            PIL.Image - изображение
    """
    response = requests.get(image_url, stream=True)
    return get_img(response.raw, is_gray_scale)
