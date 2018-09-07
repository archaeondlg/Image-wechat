#!/usr/bin/python
# coding:UTF-8

from PIL import Image


def fill_image(image, color='white'):
    width, height = image.size
    length = width if width > height else height
    new_image = Image.new(image.mode, (length, length), color)
    if width > height:
        new_image.paste(image, (0, int((length - height) / 2)))
    else:
        new_image.paste(image, (int((length - width) / 2), 0))
    return new_image


def deal_image(image):
    width, height = image.size
    img_length = int(width / 3)
    for y in range(3):
        for x in range(3):
            box = (x * img_length, y * img_length, (x + 1) * img_length, (y + 1) * img_length)
            img = image.crop(box)
            img.save(str(x) + '-' + str(y) + '.png', 'PNG')
    return 'success'


if __name__ == '__main__':
    file_path = 'photo.jpg'
    image = Image.open(file_path)
    image = fill_image(image, 'white')
    deal_image(image)
