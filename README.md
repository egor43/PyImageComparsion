# PyImageComparsion
Version in another language: [Русский :ru:](https://github.com/egor43/PyImageComparsion/blob/master/README.ru.md "Русский")

PyImageComparsion is a package that provides a simple API and a set of tools for determining the degree of similarity of images.

# Principle of operation
Two approaches are used to assess the degree of similarity of images: comparison of hashes and comparison of ORB descriptors. Since working with ORB descriptors is quite an expensive process, it is used only in case of image mismatch based on hash match assessment.
The conceptual comparison can be broken down into the following steps:
1. Get images;
2. Get image metrics (hashes and ORB descriptors);
3. Estimate the degree of hash match;
4. If it was not possible to determine the hash match, estimate the degree of ORB descriptors match;
5. Return the result of identity assessment.

# Main components
The PyImageComparsion package consists of the following main components:
- **compare_api** - image comparison API;
- **image_opener** - capture/open an image;
- **image_metrick** - calculating image metrics;
- **compare_tools** - an extended set of image comparison tools.

# Installation
You can copy the package folder and set dependencies manually, or install the package using "setup.py". Below you will find several options for installing and running testing.
## Installation from source code
```
$ python setup.py install
```
## Test launches
```
$ python setup.py test
```
## Launch in docker
At the moment, there are several docker image assemblies. By default, when the container starts, testing of the main functions of the package is started, at the end of which the container finishes its work.
### Launching the latest version of the package
```
$ docker run egorrich/py_image_comparsion
```
### Launch a specific version
You can run the required version of the package. To do this, execute the command below, replacing **VERSION** with the version of the desired release.
```
$ docker run egorrich/py_image_comparsion:release-VERSION
```
Examples:
```
$ docker run egorrich/py_image_comparsion:release-0.3
```
```
$ docker run egorrich/py_image_comparsion:release-0.1
```
### Launching the latest developer build
```
$ docker run egorrich/py_image_comparsion:dev
```

# Main usage options
The following uses imply that you have PyImageComparsion installed.
## Quick comparison of two images
This comparison is based only on evaluating the hash match of the two images.
```python
from image_comparsion import compare_api

img_1_path = "./tests/files/2.png"
img_2_url = "https://raw.githubusercontent.com/egor43/PyImageComparsion/master/tests/files/3.png"

is_similar = compare_api.fast_image_compare(img_1_path, img_2_url)
print(is_similar)
```
## Complete comparison of two images
Full image comparison evaluates not only the degree of image hash matching, but also the degree of ORB descriptors matching. The descriptors are only compared if the comparison of hashes has not yielded a positive result.
```python
from image_comparsion import compare_api

img_1_path = "./tests/files/2.png"
img_2_url = "https://raw.githubusercontent.com/egor43/PyImageComparsion/master/tests/files/3.png"

is_similar = compare_api.full_image_compare(img_1_path, img_2_url)
print(is_similar)
```
## Fast grouping of similar images
Quick grouping allows you to group similar images based on an estimate of the degree of match of hash images.
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
## Full grouping of similar images
Full grouping allows you to group similar images based on an estimate of the degree of match of hash images and an estimate of ORB descriptors match.
Due to the comparison of descriptors, this function works much longer than fast grouping, but has higher accuracy.
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
## Specifying a match threshold
Some image comparison functions allow you to specify the matching threshold value at which the images will be considered the same.
### Setting the hash match threshold = 50%
```python
from image_comparsion import compare_api

img_1_path = "./tests/files/2.png"
img_2_url = "https://raw.githubusercontent.com/egor43/PyImageComparsion/master/tests/files/3.png"

is_similar = compare_api.fast_image_compare(img_1_path, img_2_url, match_threshold_hash_percent=50)
print(is_similar)
```
### Setting the ORB descriptor match threshold = 15%
```python
from image_comparsion import compare_api

img_1_path = "./tests/files/2.png"
img_2_url = "https://raw.githubusercontent.com/egor43/PyImageComparsion/master/tests/files/3.png"

is_similar = compare_api.full_image_compare(img_1_path, img_2_url, match_threshold_orb_percent=15)
print(is_similar)
```
### Setting hash match threshold = 50% and ORB descriptors = 15%
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
## Other use cases
Other uses can be studied in the attached tests or by studying the modules provided in the package in detail.
