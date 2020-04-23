"""
    Модуль предоставляет инструменты открытия изображений из различных источников
    и преобразование их к стандартным объектам PIL.Image.Image 

    author: https://github.com/egor43
"""

import requests
import io
from PIL import Image
from . import helpers


def get_img_from_byte_stream(binary_stream, is_gray_scale=True):
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


def get_img_from_url(image_url, is_gray_scale=True):
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
    return get_img_from_byte_stream(response.raw, is_gray_scale)


def get_img(image_path, is_gray_scale=True):
    """
        Возвращает изображение полученное по переданному пути или url.
        Params:
            image_path - путь или url адрес изображения
            is_gray_scale - флаг определяющий необходимость преобразования
                            изображения в оттенки серого (черно-белое)
        Return:
            PIL.Image.Image - изображение
    """
    if helpers.is_url(image_path):
        return get_img_from_url(image_path, is_gray_scale)
    
    with open(image_path, "rb") as image_bs:
        image_byte_buf = io.BytesIO(image_bs.read())
        return get_img_from_byte_stream(image_byte_buf, is_gray_scale)


def get_images(image_paths, is_gray_scale=True):
    """
        Возвращает последовательность изображений полученных по путям или url'ам.
        Params:
            image_paths - список путей или url'ов изображений
            is_gray_scale - флаг определяющий необходимость преобразования
                            изображения в оттенки серого (черно-белое)
        Return:
            list - список изображений
    """
    result = []
    return result
    for image_path in image_paths:
        result.append(get_img(image_path, is_gray_scale))
    return result
