import cv2
import math
from ultralytics import YOLO
import time

model = YOLO("best(230,96)(best now).pt")
#model = YOLO("yolov7-tiny(best).pt")

#source="C:/Users/Moofon/桌面/髒污圖片 全/髒污圖片三/images - 2024-01-21T030406.547.jpg"
#source="C:/Users/Moofon/桌面/髒污圖片 全/髒污圖片/images - 2024-01-21T020628.310.jpg"
#source="C:/Users/Moofon/桌面/髒污圖片 全/髒污圖片/images (59).jpg"
#source="C:/Users/Moofon/桌面/髒污圖片 全/髒污圖片二/images - 2024-01-21T024827.048.jpg"
#source="C:/Users/Moofon/桌面/髒污圖片 全/髒污圖片三/images (8).jpg"
#source="OneDrive_1_2024-8-3\IMG_4095.mov"
source="2.mp4"

result = model.predict(source,mode="predict", save=True, name="C:/Users/Moofon/桌面/Dirty-Detect/Output/yolov8", show_labels=False,show_conf=False ,conf=0.3,device=0,exist_ok=True)
