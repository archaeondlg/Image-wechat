#!/usr/bin/python
# coding:UTF-8

from PIL import Image


def fill_image(image, color='white'):
    width, height = image.size
    # python中的三目运算
    length = width if width > height else height
    # 新生成图片，参数：模式（一般RGB），尺寸，背景色（默认黑）
    new_image = Image.new(image.mode, (length, length), color)
    # 在之前新纯色图片上粘贴图片
    if width > height:
        new_image.paste(image, (0, int((length - height) / 2)))
    else:
        new_image.paste(image, (int((length - width) / 2), 0))
    return new_image


def cut_image(image):
    width, height = image.size
    img_length = int(width / 3)
    boxs = []
    for y in xrange(3):
        for x in xrange(3):
            box = (x * img_length, y * img_length, (x + 1) * img_length, (y + 1) * img_length)
            boxs.append(box)
    images = [image.crop(box) for box in boxs]
    return images


def save_image(images):
    for index, item in images:
        item.save(str(index) + '.png', 'PNG')


if __name__ == '__main__':
    file_path = 'photo.jpg'
    image = Image.open(file_path)
    image = fill_image(image, 'white')
    image_list = cut_image(image)

    save_image(image_list)
