

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 18:19:09 2018
@author: Administrator
"""

import os
from PIL import Image

# 切割图片
def splitimage(src, rownum, colnum, dstpath):
    img = Image.open(src)
    w, h = img.size
    if rownum <= h and colnum <= w:
        print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
        print('图片切割')

        s = os.path.split(src)
        if dstpath == '':
            dstpath = s[0]
        fn = s[1].split('.')
        basename = fn[0]
        ext = fn[-1]

        num = 0
        rowheight = h // rownum
        colwidth = w // colnum
        for r in range(rownum):
            for c in range(colnum):
                box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                img.crop(box).save(os.path.join(dstpath, basename + '_' + str(num) + '.' + ext), ext)
                num = num + 1

        print('共生成 %s 张小图片。' % num)
    else:
        print('error')


# 创建文件夹
def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        print(path + ' 目录已存在')
        return False


folder = r'/Users/birder/Downloads/all/train/images'  # 存放图片的文件夹
path = os.listdir(folder)
import numpy as np
def rle_encode(im):
    '''
    im: numpy array, 1-mask, 0-background
    Returns run length as string
    '''
    pixels = im.flatten(order='F')
    pixels = np.concatenate([[0], pixels, [0]])
    runs = np.where(pixels[1:] != pixels[:-1])[0] + 1
    runs[1::2] -= runs[::2]
    return ' '.join(str(x) for x in runs)
img1 = Image.open("/Users/birder/Downloads/all/train/New/masks/0a1742c740_0.png")
img2 = Image.open("/Users/birder/Downloads/all/train/New/masks/0a1742c740_1.png")
img3 = Image.open("/Users/birder/Downloads/all/train/New/masks/0a1742c740_2.png")
img4 = Image.open("/Users/birder/Downloads/all/train/New/masks/0a1742c740_3.png")
im1 = np.array(img1,dtype=np.uint8)
im2 = np.array(img2,dtype=np.uint8)
im3 = np.array(img3,dtype=np.uint8)
im4 = np.array(img4,dtype=np.uint8)
imgh = np.hstack((im1,im2))
imgv = np.hstack((im3,im4))
img = np.vstack((imgh,imgv))
rlestring = rle_encode(img)


def rleToMask(rleString, height, width):
    # width heigh
    rows, cols = height, width
    try:
        # get numbers
        rleNumbers = [int(numstring) for numstring in rleString.split(' ')]
        # get pairs
        rlePairs = np.array(rleNumbers).reshape(-1, 2)
        # create an image
        img = np.zeros(rows * cols, dtype=np.uint8)
        # for each pair
        for index, length in rlePairs:
            # get the pixel value
            index -= 1
            img[index:index + length] = 255

        # reshape
        img = img.reshape(cols, rows)
        img = img.T

    # else return empty image
    except:
        img = np.zeros((cols, rows))

    return img
img = rleToMask(rlestring,100,100)
#img = np.resize(img,[101,101])
img = Image.fromarray(img)
img = img.resize((101,101))
img.save('/Users/birder/Downloads/all/a.png')
#img = img.resize((101,101))
#import matplotlib.pyplot as plt
#plt.imshow(img)
#plt.show()

#
# img = img.resize((101, 101))
#
# img.save("/Users/birder/Downloads/all/train/New/0ab5e14937_0.png", "PNG")
# print(path)
#
# for each_bmp in path:  # 批量操作
#     first_name, second_name = os.path.splitext(each_bmp)
#     each_bmp = os.path.join(folder, each_bmp)
#     src = each_bmp
#     print(src)
#     print(first_name)
#     # 定义要创建的目录
#     mkpath = "/Users/birder/Downloads/all/train/New/images/"
#     # 调用函数
#     mkdir(mkpath)
#     if os.path.isfile(src):
#         dstpath = mkpath
#         if (dstpath == '') or os.path.exists(dstpath):
#             row = int(2)  # 切割行数
#             col = int(2)  # 切割列数
#             if row > 0 and col > 0:
#                 splitimage(src, row, col, dstpath)
#             else:
#                 print('无效的')
#         else:
#             print('图片保存目录 %s 不存在！' % dstpath)
#     else:
#         print('图片文件 %s 不存在！' % src)

