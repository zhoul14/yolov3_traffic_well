import sys

if len(sys.argv) < 2:
    print("Usage: $ python {0} [video_path] [output_path(optional)] [output_gps_info_path(optional)]", sys.argv[0])
    exit()

from tw_yolo import YOLO
from tw_yolo import detect_video

if __name__ == '__main__':
    video_path = sys.argv[1]
    if len(sys.argv) > 2:
        output_path = sys.argv[2]
        if len(sys.argv) == 3:
            detect_video(YOLO(), video_path, output_path,'gps_infos.csv')
        else:
            detect_video(YOLO(), video_path, output_path,sys.argv[3])
    else:
        detect_video(YOLO(), video_path)
