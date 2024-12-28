import time
import json
from datetime import datetime

def read_last_line(file_path):
    with open(file_path, 'rb') as f:
        try:
            f.seek(-2, 2)  
            while f.read(1) != b'\n':
                f.seek(-2, 1)
        except OSError:
            f.seek(0)
        last_line = f.readline().decode()
    return last_line.strip()

def update_db_if_needed(db_path, key, timestamp):
    with open(db_path, 'r') as db_file:
        db = json.load(db_file)

    if timestamp > db[key]:
        db[key] = timestamp
        with open(db_path, 'w') as db_file:
            json.dump(db, db_file, indent=4)

def monitor_file(txt_file_path, db_file_path):
    last_line = None

    while True:
        try:
            new_last_line = read_last_line(txt_file_path)

            if new_last_line != last_line:  
                last_line = new_last_line
                parts = last_line.split()

                if len(parts) >= 5:
                    key = parts[0]
                    last_element = float(parts[-1])

                    if last_element >= 0.8:
                        current_time = datetime.now().isoformat()
                        print(current_time)
                        update_db_if_needed(db_file_path, key, current_time)

            time.sleep(1)  

        except KeyboardInterrupt:
            print("Terminated by user.")
            break
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(1)

if __name__ == "__main__":
    txt_file_path = "./runs/detect/predict/labels/piyan.txt"  
    db_file_path = "./DB/db.json"    

    monitor_file(txt_file_path, db_file_path)
