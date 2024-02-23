from ultralytics import YOLO

model = YOLO("best.pt")
model.conf = 0.2
result = model.predict(
    #source="C:/Users/Moofon/桌面/髒污圖片二/images - 2024-01-21T024827.048.jpg",
    source="C:/Users/Moofon/桌面/input.mp4",
    mode="predict",
    save=True,
    device="cpu"
)