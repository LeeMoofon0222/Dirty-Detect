from ultralytics import YOLO


model = YOLO("best(141,64).pt")

#source="C:/Users/Moofon/桌面/髒污圖片 全/髒污圖片三/images - 2024-01-21T030406.547.jpg"
#source="C:/Users/Moofon/桌面/髒污圖片 全/髒污圖片/images - 2024-01-21T020628.310.jpg"
#source="C:/Users/Moofon/桌面/髒污圖片 全/髒污圖片/images (59).jpg"
#source="C:/Users/Moofon/桌面/髒污圖片 全/髒污圖片二/images - 2024-01-21T024827.048.jpg"
#source="C:/Users/Moofon/桌面/髒污圖片 全/髒污圖片三/images (8).jpg"
source="C:/Users/Moofon/桌面/髒污圖片 全/input.mp4"

result = model.predict(source,mode="predict", save=True, name="C:/Users/Moofon/桌面/Output/64", show_labels=False,show_conf=False ,conf=0.3,device=0,exist_ok=True)

