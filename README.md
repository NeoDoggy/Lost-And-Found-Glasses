# Lost-And-Found-Glasses

Software has the model and the code for running the software  
The firmware is for an esp32-s3 camera, feel free to upload it to your board with Arduino IDE

## Table of Contents
- [Training](#training)
- [Implementation](#implementation)

## Training

1. Navigate to the `./Software/yolo/` directory and open the `YOLO11.ipynb` notebook.
2. Start running from the `setup` cell and ensure all required `pip` packages are installed.
3. Run the `predict` cell to verify if `yolo11n.pt` is loaded successfully.
4. Locate and run the `import roboflow` cell:
   - Provide your `api_key`, `workspace`, and `project` information to load the dataset from Roboflow.
5. Update the `data.yaml` file:
   - Modify the `train`, `val`, and `test` paths from relative to absolute paths to avoid errors.
6. In the `Detection` cell, adjust the following parameters:
   - `data`: Set to the absolute path of your `data.yaml` file.
   - `epochs`: Specify the number of epochs as per your requirement.
   - `imgsz`: Set the image size to your preference.
   - Load the `yolo11n.pt` model.
7. Start the training process.
8. Once training is complete, locate the `best.pt` file and move it to the `./Software/model` directory.

## Implementation

**Note:** All implementation scripts must be run simultaneously.

1. Run `./Software/saveImg.py`:
   - This script connects to the ESP32 camera at the URL `http://192.168.0.107/capture`.
   - Captured images will be saved to the `./Software/images/input` directory.

2. Run `./Software/main.py`:
   - Loads the `best.pt` model to predict the objects in the images saved in `./Software/images/input`.
   - Displays recognition results using the `pygame` interface.

3. Run `./Software/STREAMmain.py`:
   - If `main.py` detects an object, it returns parameters used to confirm whether an object has been scanned.

4. Run `./Software/monitor_db.py`:
   - Continuously checks if the detected object's time is later than the `database last seen` time.
   - If true, updates the database.

5. Run `./Software/showDB.py`:
   - Displays all objects and their `last seen time` from the database using a `pygame` interface.


