# -*- coding:utf-8 -*-
__author__ = 'Microcosm'
 
import cv2
import numpy as np
from matplotlib import pyplot as plt
from timeit import default_timer as timer
from PIL import Image,ImageFont,ImageDraw

def detect_video(video_path, output_path=""):
    import cv2
    vid = cv2.VideoCapture(video_path)
    if not vid.isOpened():
        raise IOError("Couldn't open webcam or video")
    video_FourCC    = int(vid.get(cv2.CAP_PROP_FOURCC))
    video_fps       = vid.get(cv2.CAP_PROP_FPS)
    video_size      = (int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)),
                        int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    isOutput = True if output_path != "" else False
    if isOutput:
        print("!!! TYPE:", type(output_path), type(video_FourCC), type(video_fps), type(video_size))
        out = cv2.VideoWriter(output_path, video_FourCC, video_fps, video_size)
    accum_time = 0
    curr_fps = 0
    fps = "FPS: ??"
    prev_time = timer()
    while True:
        return_value, frame = vid.read()
        image = Image.fromarray(frame)
        image = templateMatch(image)
        result = np.asarray(image)
        curr_time = timer()
        exec_time = curr_time - prev_time
        prev_time = curr_time
        accum_time = accum_time + exec_time
        curr_fps = curr_fps + 1
        if accum_time > 1:
            accum_time = accum_time - 1
            fps = "FPS: " + str(curr_fps)
            curr_fps = 0
        cv2.putText(result, text=fps, org=(3, 15), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.50, color=(255, 0, 0), thickness=2)
        cv2.namedWindow("result", cv2.WINDOW_NORMAL)
        cv2.imshow("result", result)
        if isOutput:
            out.write(result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

input_img_name = ""
img = cv2.imread(input_img_name)
def templateMatch(img,template_file="template.jpg"):
    img2 = img[200:1250,:,:].copy()
    template = cv2.imread(template_file)
    w,h = template.shape[0:2][::-1]
     
    # 6 中匹配效果对比算法
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCORR', 'cv2.TM_SQDIFF']
     
    for meth in methods:
        img = img2.copy()
     
        method = eval(meth)
     
        res = cv2.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
     
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
     
        cv2.rectangle(img,top_left, bottom_right, 0, 2)
     
        print(meth)
        return img

detect_video("/Users/zhoulu/myscp/match_temp/2018-11-13_16_35_40.mp4")
