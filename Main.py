from ultralytics import YOLO
# import os
# os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE" 

# Load a model
model = YOLO("yolov8n.pt")  # load an official model
results = model.train(data="data.yaml", epochs=3)
# Validate the model
results = model.val(data="data.yaml")  # no arguments needed, dataset and settings remembered