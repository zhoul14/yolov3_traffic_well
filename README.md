# keras-yolo3

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

## Introduction

A Keras implementation of YOLOv3 (Tensorflow backend) inspired by [allanzelener/YAD2K](https://github.com/allanzelener/YAD2K).


---

## 依赖库安装

1. windows系统下确保有安装如下工具：
    - git https://www.git-scm.com/download/win  （git工具和git bash mingw64工具）
    - anaconda3 https://repo.anaconda.com/archive/Anaconda3-5.2.0-Windows-x86_64.exe （python安装包）
    - tessarctor-ocr https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-4.0.0dev-20170510.exe （坐标识别模块,安装博客可见      https://www.cnblogs.com/jianqingwang/p/6978724.html ）
   分别下载安装后保证在windows下能找到git和git bash
2. 在windows下启动git bash
    1) 首先检测git的安装，运行下面的代码：
    ```
      git --version
    ```
    应当显示
    ```
    $ git --version
    git version x.xx.x.windows.1
    ```
   2) 检验anaconda3的安装:
    ```
      python --version
    ```
    应当显示
    ```
      $ python --version
    Python 3.6.5 :: Anaconda, Inc.
    ```
   3) 检验tesseract-ocr（orc模块尚未完全加入，目前可以不用装）
    ```
       tesseract -v
    ```
    正确的输出应该为：
    ```
    $ tesseract -v
    tesseract v4.0.0-beta.1.20180608
    leptonica-1.76.0
    libgif 5.1.4 : libjpeg 8d (libjpeg-turbo 1.5.3) : libpng 1.6.34 : libtiff 4.0.9 : zlib 1.2.11 :     libwebp 0.6.1 : libopenjp2 2.2.0
    ```
    若报错通常为环境变量配置错误，重新配置环境变量后重启git bash即可
3. 安装python依赖包和源代码
    ```
    pip install opencv-python tensorflow keras -i https://pypi.tuna.tsinghua.edu.cn/simple
    ```
    若有其他报错则继续安装依赖包
    
    下载源代码
    ```
       git clone https://github.com/zhoul14/yolov3_traffic_well.git
    ```
4. 将权重文件yolo.h5放置到yolov3_traffic_well/model_data路径下（不然会运行第5步的python yolo.py会报错：找不到yolo.h5文件)

    权重文件请联系我、汪所或者谭哲（周六发到qq邮箱的yolo压缩包就是）

5. 在yolov3根目录下，在git bash中运行
    ```
    python yolo.py
    ```

  不报错则表示安装正常，报错请联系1214279441@qq.com

6. 更改tw_yolo.py的输入图片文件位置
    将文件206行位置代码
    ```
        path="C:/Users/12142/Desktop/keras-yolo3/VOCdevkit/VOC2007/JPEGImages/1016/*.jpg"
        outdir = "C:/Users/12142/Desktop/keras-yolo3/VOCdevkit/VOC2007/SegmentationClass"
        gps_file =  "C:/Users/12142/Desktop/keras-yolo3/VOCdevkit/VOC2007/gps_infos.csv"
    ```

    ```
        path="你的输入图片路径/*.jpg"
        outdir = "你的输出图片路径"
        gps_file = "你的gps输出图片路径"
    ```
    之后运行：
    ```
        python tw_yolo.py
    ```
    结果图片会存放在outdir中
7. 视频播放
```
    python tw_yolo_video.py 1016-1020.3gp out.3gp gpsinfo.csv
---
> 以下为原始keras-yolo的readme可做参考

## Quick Start

1. Download YOLOv3 weights from [YOLO website](http://pjreddie.com/darknet/yolo/).
2. Convert the Darknet YOLO model to a Keras model.
3. Run YOLO detection.

```
wget https://pjreddie.com/media/files/yolov3.weights
python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
python yolo_video.py [OPTIONS...] --image, for image detection mode, OR
python yolo_video.py [video_path] [output_path (optional)]
```

For Tiny YOLOv3, just do in a similar way, just specify model path and anchor path with `--model model_file` and `--anchors anchor_file`.

### Usage
Use --help to see usage of yolo_video.py:
```
usage: yolo_video.py [-h] [--model MODEL] [--anchors ANCHORS]
                     [--classes CLASSES] [--gpu_num GPU_NUM] [--image]
                     [--input] [--output]

positional arguments:
  --input        Video input path
  --output       Video output path

optional arguments:
  -h, --help         show this help message and exit
  --model MODEL      path to model weight file, default model_data/yolo.h5
  --anchors ANCHORS  path to anchor definitions, default
                     model_data/yolo_anchors.txt
  --classes CLASSES  path to class definitions, default
                     model_data/coco_classes.txt
  --gpu_num GPU_NUM  Number of GPU to use, default 1
  --image            Image detection mode, will ignore all positional arguments
```
---

4. MultiGPU usage: use `--gpu_num N` to use N GPUs. It is passed to the [Keras multi_gpu_model()](https://keras.io/utils/#multi_gpu_model).

## Training

1. Generate your own annotation file and class names file.
    One row for one image;
    Row format: `image_file_path box1 box2 ... boxN`;
    Box format: `x_min,y_min,x_max,y_max,class_id` (no space).
    For VOC dataset, try `python voc_annotation.py`
    Here is an example:
    ```
    path/to/img1.jpg 50,100,150,200,0 30,50,200,120,3
    path/to/img2.jpg 120,300,250,600,2
    ...
    ```

2. Make sure you have run `python convert.py -w yolov3.cfg yolov3.weights model_data/yolo_weights.h5`
    The file model_data/yolo_weights.h5 is used to load pretrained weights.

3. Modify train.py and start training.
    `python train.py`
    Use your trained weights or checkpoint weights with command line option `--model model_file` when using yolo_video.py
    Remember to modify class path or anchor path, with `--classes class_file` and `--anchors anchor_file`.

If you want to use original pretrained weights for YOLOv3:
    1. `wget https://pjreddie.com/media/files/darknet53.conv.74`
    2. rename it as darknet53.weights
    3. `python convert.py -w darknet53.cfg darknet53.weights model_data/darknet53_weights.h5`
    4. use model_data/darknet53_weights.h5 in train.py

---

## Some issues to know

1. The test environment is
    - Python 3.5.2
    - Keras 2.1.5
    - tensorflow 1.6.0

2. Default anchors are used. If you use your own anchors, probably some changes are needed.

3. The inference result is not totally the same as Darknet but the difference is small.

4. The speed is slower than Darknet. Replacing PIL with opencv may help a little.

5. Always load pretrained weights and freeze layers in the first stage of training. Or try Darknet training. It's OK if there is a mismatch warning.

6. The training strategy is for reference only. Adjust it according to your dataset and your goal. And add further strategy if needed.

7. For speeding up the training process with frozen layers train_bottleneck.py can be used. It will compute the bottleneck features of the frozen model first and then only trains the last layers. This makes training on CPU possible in a reasonable time. See [this](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html) for more information on bottleneck features.
