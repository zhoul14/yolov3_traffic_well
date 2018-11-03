#encoding:utf-8
#!/usr/bin/env python
from werkzeug.utils import secure_filename
from flask import Flask, render_template, jsonify, request, make_response, send_from_directory, abort
import time
import os
import Pic_str
import base64
import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image
from keras import backend as K

# import lane
#my_yolo=None
def detect_img_once(yolo,input_file,output_file):
    print(input_file,output_file)
    try:
        image = Image.open(input_file)
    except:
        print('Open Error! Try again!')
    else:
        r_image = yolo.detect_image(image)
        r_image.save(output_file)
#    yolo.close_session()


#detect_img_once(my_yolo,'/Users/zhoulu/yolov3_traffic_well/upload/2018110220352205.png','test.png')

app = Flask(__name__)
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
 
 
@app.route('/upload')
def upload_test():
    return render_template('up.html')
 
 
my_yolo=YOLO()
# 上传文件
@app.route('/up_photo', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['photo']
    if f and allowed_file(f.filename):
        fname = secure_filename(f.filename)
        print(fname) 
        ext = fname.rsplit('.', 1)[1]
        new_filename = Pic_str.Pic_str().create_uuid() + '.' + ext
        file_pwd = os.path.join(file_dir,new_filename)
        f.save(file_pwd)
        out_file_pwd = os.path.join(file_dir,"out_"+new_filename)
        detect_img_once(my_yolo,file_pwd,out_file_pwd)
#        K.clear_session()
        return show_pic(out_file_pwd)
        return jsonify({"success": 0, "msg": "上传成功"})
    else:
        return jsonify({"error": 1001, "msg": "上传失败"})
 
@app.route('/download/<string:filename>', methods=['GET'])
def download(filename):
    if request.method == "GET":
        if os.path.isfile(os.path.join('upload', filename)):
            return send_from_directory('upload', filename, as_attachment=True)
        pass
    
def show_pic(filename):
    image_data = open(os.path.join(filename), "rb").read()
    response = make_response(image_data)
    response.headers['Content-Type'] = 'image/png'
    return response

# show photo
@app.route('/show/<string:filename>', methods=['GET'])
def show_photo(filename):
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if request.method == 'GET':
        if filename is None:
            pass
        else:
            image_data = open(os.path.join(file_dir, '%s' % filename), "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response
    else:
        pass
 
 
if __name__ == '__main__':
    detect_img_once(my_yolo,'/Users/zhoulu/yolov3_traffic_well/upload/2018110220352205.png','test.png')
    app.run(debug=False,threaded=False)
