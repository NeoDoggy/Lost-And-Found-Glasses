from ultralytics import YOLO

# Load a model
model = YOLO("models/ivan.pt")  # pretrained YOLO11n model

# Run batched inference on a list of images
results = model("http://192.168.0.107:81/stream", stream=True)  # return a generator of Results objects

# Process results generator
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs 
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk