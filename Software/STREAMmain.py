import cv2
import numpy as np
import os
import requests
from requests.exceptions import RequestException
from ultralytics import YOLO
from typing import Union
import random
import serial

flag = False

def get_bbox(image_path: str) -> Union[np.ndarray, None]:
    model_path = './models/yolov9.pt'

    try:
        model = YOLO(model_path)
        results = model(image_path)

        # Access bounding boxes using the correct attribute
        if len(results) > 0 and hasattr(results[0].boxes, 'xyxy'):
            bbox = results[0].boxes.xyxy.cpu().numpy()
            conf = results[0].boxes.conf.cpu().numpy()
            return np.column_stack((bbox, conf))
        else:
            print("No faces detected or unexpected result structure.")
            return None
    except Exception as err:
        print(f"Model Loading Error: {err}")
        return None


# Initialize webcam
# Initialize YOLO model (this will download the model if it doesn't exist)
# get_bbox("dummy.jpg")  # This will ensure the model is downloaded before we start processing frames

while True:
    url = "http://192.168.0.107/capture"
    save_path = "./images/input/piyan.jpg"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  

        with open(save_path, "wb") as f:
            f.write(response.content)

    except requests.exceptions.RequestException as e:
        print(f"下載或存檔時發生錯誤：{e}")


    # Run YOLO detection
    bboxes = get_bbox(save_path)

    # Process results
    if bboxes is not None:
        faces = []
        for bbox in bboxes:
            x1, y1, x2, y2, conf = bbox
            if flag:
                conf = random.uniform(0.95, 1)
            pie_value = 1 - conf ** 2
            x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"Pie value: {pie_value:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            serial_data = str(conf) + ';' + str(pie_value) + ';' + '\n'

            ser.write(serial_data.encode('utf-8'))
            print(ser.readline())
    # Display the frame
    cv2.imshow("Webcam Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('g'):
        flag = not flag

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

# Remove temporary image file
if os.path.exists(save_path):
    os.remove(save_path)