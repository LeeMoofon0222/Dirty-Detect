from ultralytics import YOLO
import torch
import torchvision

model = YOLO("best.pt")
model.conf = 0.2
source="C:/Users/Moofon/桌面/髒污圖片二/images - 2024-01-21T024827.048.jpg"
#source="C:/Users/Moofon/桌面/input.mp4"
save_dir = "C:/Users/Moofon/桌面/Dirty-Detect/Predict"
result = model.predict(source,mode="predict", save=True, save_dir=save_dir,device=0)