import cv2
import math
from ultralytics import YOLO
import time

model = YOLO("best(230,96)(best now).pt")

source = "C:/Users/Moofon/桌面/髒污圖片 全/IMG_8870.mp4"
cap = cv2.VideoCapture(source)

trackers = {}
start_times = {}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform detection
    results = model.predict(frame)
    current_time = time.time()

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2, cls_id = int(box.xyxy[0][0]), int(box.xyxy[0][1]), int(box.xyxy[0][2]), int(box.xyxy[0][3]), int(box.cls[0])

            conf = math.ceil((box.conf[0]*100))/100
        
            if conf >= 0.3:
                if cls_id not in trackers:
                    # Initialize tracker for new object
                    trackers[cls_id] = cv2.TrackerKCF_create()
                    bbox = (x1, y1, x2 - x1, y2 - y1)
                    trackers[cls_id].init(frame, bbox)
                    start_times[cls_id] = current_time
                else:
                    # Update existing tracker
                    success, bbox = trackers[cls_id].update(frame)
                    if success:
                        # Tracking success
                        x, y, w, h = [int(v) for v in bbox]
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        
                        # Check if object has been tracked for more than 2 seconds
                        if current_time - start_times[cls_id] >= 2:
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            cv2.putText(frame, str(cls_id), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    else:
                        # Tracking failure, stop tracking
                        del trackers[cls_id]
                        del start_times[cls_id]

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
