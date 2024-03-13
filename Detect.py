from ultralytics import YOLO


model = YOLO("best(100).pt")

#source="C:/Users/Moofon/桌面/髒污圖片二/images - 2024-01-21T024827.048.jpg"
#source="C:/Users/Moofon/桌面/input.mp4"
#source="C:/Users/Moofon/桌面/髒污圖片二/images - 2024-01-21T024327.665.jpg"
source="C:/Users/Moofon/桌面/髒污圖片五/images (54).jpg"
#source="C:/Users/Moofon/桌面/髒污圖片二/images - 2024-01-21T024345.459.jpg"
#result = model.predict(source,mode="predict", save=True, save_dir=save_dir,device=0)

results = model(source, mode="predict", conf = 0.2,save_crop=True, name="C:/Users/Moofon/桌面/Output", exist_ok=True, device=0)

