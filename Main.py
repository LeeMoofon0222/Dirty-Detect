from ultralytics import YOLO
# import os
# os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE" 

# Load a model
#model = YOLO("yolov8n.pt")  # load an official model
model = YOLO("C:/Users/Moofon/桌面/Dirty-Detect/runs/detect/train6/weights/best.pt")  # load an official model
model.conf = 0.1
results = model.train(data="data.yaml", epochs=3)
# Validate the model
results = model.val(data="data.yaml")  # no arguments needed, dataset and settings remembered