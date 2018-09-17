# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET
from os import getcwd

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

classes = ["traffic sign", "well cover"]

def convert_annotation(dir_id, image_id, list_file):
    in_file = open('VOCdevkit/VOC2007/Annotations/%s/frame%s.xml'%(dir_id, image_id), encoding='UTF-8')
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

def run():
    dir_image_ids = open('VOCdevkit/VOC2007/ImageSets/Main/train_tw.txt').read().strip().split()
    image_ids = [ x.split('-')[1] for x in dir_image_ids]
    dir_ids = [ x.split('-')[0] for x in dir_image_ids]
    list_file = open('train_tw.txt', 'w')
    for k in range(len(image_ids)):
        image_id = image_ids[k]
        dir_id = dir_ids[k]
        list_file.write('%s/VOCdevkit/VOC2007/JPEGImages/%s/frame%s.jpg'%(wd,dir_id, image_id))
        convert_annotation(dir_id, image_id, list_file)
        list_file.write('\n')
    list_file.close()

run()