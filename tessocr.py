# -*-encoding:utf-8-*-
import pytesseract
from PIL import Image
import cv2
import numpy
import re

def binarization(image):
    # 转成灰度图
    imgry = image.convert('L')
    # 二值化，阈值可以根据情况修改
    threshold = 100
    table = []
    for i in range(256):
        if i < threshold:
            table.append(1)
        else:
            table.append(0)
    out = imgry.point(table, '1')
    return out


def get_GPS_info(image,className,showPic=False,offsetx1=0,offsetx2=0,offsety1=0,offsety2=0):
    # image = Image.open(imageFile)
    # 已经通过实验找到图片中的GPS固定位置
    regionx=(882,1000,1117,1058)#x的坐标
    regiony=(1130,1000,1342,1058)#y的坐标
    # 转换成黑白图像
    out = binarization(image)
    out_y=out.crop(regiony)
    out_x=out.crop(regionx)
    # 识别经度字符串
    text_x = pytesseract.image_to_string(out_x,config='-l eng')  # 0使用eng文解析图片
    # 过滤无效信息
    num_x = re.sub("\D", "", text_x)
    num_x = num_x[:3] + '.' + num_x[3:]
    # 识别纬度字符串
    text_y = pytesseract.image_to_string(out_y,config='-l eng')  # 0使用eng文解析图片
    # 过滤无效信息
    num_y = re.sub("\D", "", text_y)
    num_y = num_y[:2] + '.' + num_y[2:]
    if showPic:
        out_x.show()
        out_y.show()
    return "%s|(%s,%s)"%( className,num_x, num_y )



if __name__ == '__main__':
    get_GPS_info("frame00339.jpg","test")
