# PyImageComparsion
Версия на другом языке: [English :uk:](https://github.com/egor43/PyImageComparsion/blob/master/README.md "English")

PyImageComparsion - это пакет предоставляющий простое API и набор инструментов для определения степени схожести изображений.
В основе работы с изображениями лежит использование библиотек:
- [scikit-image](https://github.com/scikit-image/scikit-image "scikit-image")
- [ImageHash](https://github.com/JohannesBuchner/imagehash "ImageHash")

# Принцип работы
Для оценки степени схожести изображений используется два подхода: сравнение хешей и оценка совпадения ORB дескрипторов. Так как работа с ORB дескрипторами - достаточно затратный процесс, он используется только в случае несовпадения изображений на основании оценки степени совпадения хешей.
Концептуально сравнение можно разбить на следующие шаги:
1. Получить изображения;
2. Получить метрики изображений (хеши и ORB дескрипторы);
3. Оценить степень совпадения хешей;
4. Если не удалось определить совпадение по хешам, оцениваем степень совпадения ORB дескрипторов;
5. Возвращаем результат оценки идентичности.

# Основные компоненты
Пакет PyImageComparsion состоит из следующих основных компонентов:
- **compare_api** - API сравнения изображений;
- **image_opener** - получение/открытие изображения;
- **image_metrick** - вычисление метрик изображения;
- **compare_tools** - расширенный набор инструментов сравниения изображений.

# Установка
Вы можете скопировать папку с пакетом и установить зависимости вручную, либо установить пакет с использованием setup. Ниже будут описаны несколько вариантов установки и запуска тестирования.
## Установка из исходного кода
```
$ python setup.py install
```
## Запуск тестов
```
$ python setup.py test
```
## Запуск в docker
На данный момент существует несколько сборок образов docker. По умолчанию, при старте контейнера, запускается тестирование основных функций пакета, по окончании которого, контейнер завершает работу.
### Запуск последней версии пакета
```
$ docker run egorrich/py_image_comparsion
```
### Запуск определенной версии
Вы можете запустить необходимую версию пакета. Для этого необходимо выполнить команду, указанную ниже, заменив **VERSION** версией необходимого релиза.
```
$ docker run egorrich/py_image_comparsion:release-VERSION
```
Примеры:
```
$ docker run egorrich/py_image_comparsion:release-0.3
```
```
$ docker run egorrich/py_image_comparsion:release-0.1
```
### Запуск последней developer сборки
```
$ docker run egorrich/py_image_comparsion:dev
```

# Основные варианты использования
Следующие варианты использования подразумевают наличие установленного пакета PyImageComparsion.
## Быстрое сравнение двух изображений
Данное сравнение основано только на оценке совпадения хешей двух изображений.
```python
from image_comparsion import compare_api

img_1_path = "./tests/files/2.png"
img_2_url = "https://raw.githubusercontent.com/egor43/PyImageComparsion/master/tests/files/3.png"

is_similar = compare_api.fast_image_compare(img_1_path, img_2_url)
print(is_similar)
```
## Полное сравнение двух изображений
Полное сравнение изображений оценивает не только степень совпадения хешей изображений, но и степень совпадения ORB дескрипторов. Дескрипторы сравниваются только если сравнение хешей не дало положительного результата.
```python
from image_comparsion import compare_api

img_1_path = "./tests/files/2.png"
img_2_url = "https://raw.githubusercontent.com/egor43/PyImageComparsion/master/tests/files/3.png"

is_similar = compare_api.full_image_compare(img_1_path, img_2_url)
print(is_similar)
```
## Быстрая группировка похожих изображений
Быстрая группировка позволяет сгруппировать похожие изображения на основании оценки степени совпадения хешей изображений.
```python
from image_comparsion import compare_api

img_1_path = "./tests/files/2.png"
img_2_url = "https://raw.githubusercontent.com/egor43/PyImageComparsion/master/tests/files/3.png"
img_3_path = "./tests/files/4.png"
img_4_url = "https://raw.githubusercontent.com/egor43/PyImageComparsion/master/tests/files/5.png"

img_paths = [img_1_path, img_2_url, img_3_path, img_4_url]

for group in compare_api.fast_grouping_similar_images(img_paths):
    for img in group:
        print(id(img))
    print('===========')
```
## Полная группировка похожих изображений
Полная группировка позволяет сгруппировать похожие изображения на основании оценки степени совпадения хешей изображений и оценки совпадения ORB дескрипторов.
Из-за сравнения дескрпиторов данная функция работает значительно дольше быстрой группировки, но обладает более высокой точностью.
```python
from image_comparsion import compare_api

img_1_path = "./tests/files/2.png"
img_2_url = "https://raw.githubusercontent.com/egor43/PyImageComparsion/master/tests/files/3.png"
img_3_path = "./tests/files/4.png"
img_4_url = "https://raw.githubusercontent.com/egor43/PyImageComparsion/master/tests/files/5.png"

img_paths = [img_1_path, img_2_url, img_3_path, img_4_url]

for group in compare_api.full_grouping_similar_images(img_paths):
    for img in group:
        print(id(img))
    print('===========')
```
## Указание порогового значения степени совпадения
Некоторые функции сравнения изображений позволяют указать значение порога совпадения при достижении которого изображения будут считаться одинаковыми.
### Установка порога совпадения хешей = 50%
```python
from image_comparsion import compare_api

img_1_path = "./tests/files/2.png"
img_2_url = "https://raw.githubusercontent.com/egor43/PyImageComparsion/master/tests/files/3.png"

is_similar = compare_api.fast_image_compare(img_1_path, img_2_url, match_threshold_hash_percent=50)
print(is_similar)
```
### Установка порога совпадения ORB дескрипторов = 15%
```python
from image_comparsion import compare_api

img_1_path = "./tests/files/2.png"
img_2_url = "https://raw.githubusercontent.com/egor43/PyImageComparsion/master/tests/files/3.png"

is_similar = compare_api.full_image_compare(img_1_path, img_2_url, match_threshold_orb_percent=15)
print(is_similar)
```
### Установка порога совпадения совпадения хешей = 50% и ORB дескрипторов = 15%
```python
from image_comparsion import compare_api

img_1_path = "./tests/files/2.png"
img_2_url = "https://raw.githubusercontent.com/egor43/PyImageComparsion/master/tests/files/3.png"
img_3_path = "./tests/files/4.png"
img_4_url = "https://raw.githubusercontent.com/egor43/PyImageComparsion/master/tests/files/5.png"

img_paths = [img_1_path, img_2_url, img_3_path, img_4_url]

for group in compare_api.full_grouping_similar_images(img_paths, match_threshold_hash_percent=50, match_threshold_orb_percent=15):
    for img in group:
        print(id(img))
    print('===========')
```
## Другие варианты использования
Остальные варианты использования можно изучить в прилагаемых тестах или изучив подробно предоставляемые пакетом модули.
