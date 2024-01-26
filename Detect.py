from ultralytics import YOLO

# Load a model
#model = YOLO("yolov8n.pt")  # load an official model
model = YOLO("C:/Users/Moofon/桌面/Dirty-Detect/runs/detect/train3/weights/best.pt")  # load a custom model

# Predict with the model
results = model.predict(source="C:/Users/Moofon/桌面/髒污圖片/images (71).jpg",save=True)  # predict on an image