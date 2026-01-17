import cv2
import numpy as np
from ultralytics import YOLO
from sort import Sort

model = YOLO("yolov8n.pt")
tracker = Sort()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, stream=True)
    detections = []

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])

            if conf > 0.3:
                detections.append([x1, y1, x2, y2, conf])

    detections = np.array(detections)

    if len(detections) > 0:
        tracks = tracker.update(detections)

        for t in tracks:
            x1, y1, x2, y2, tid = map(int, t)
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(frame,f"ID {tid}",(x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)

    cv2.imshow("Task 4 Object Detection", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
