# -*- coding: utf-8 -*-

from PIL import Image
import os, random, time, datetime

pwd = os.path.dirname(os.path.realpath(__file__))
img_path = os.path.abspath(os.path.dirname(pwd)) + os.path.sep + 'images' + os.path.sep

def save_image (b_image) :
  if not os.path.exists(img_path) :
    # 如果不存在图片目录，进行创建图片目录
    os.makedirs(img_path)
  with Image.open(b_image) as f :
    # 设置图片格式
    img_format = '.'
    if f.format == 'JPEG' :
      img_format += 'jpg'
    elif f.format == 'PNG' :
      img_format += 'png'
    elif f.format == 'GIF' :
      img_format += 'gif'
    else :
      return '图片格式不支持'

    # 设置图片名称
    timestamp = int(time.time() * 1000)
    img_name = time.strftime("%Y%m%d-") + str(timestamp) + '-' + str(random.randint(1, 99999))

    full_path = img_path + img_name + img_format
    # 保存图片
    f.save(full_path, f.format)
    return img_name + img_format

if __name__ == '__main__' :
  with open(img_path + '584e0d51534b6.jpg', 'rb') as file :
    img_url = save_image(file)
    print(img_url)