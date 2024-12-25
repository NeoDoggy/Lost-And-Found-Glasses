import requests
import time

def main():
    url = "http://192.168.0.107/capture"

    interval = 0.1

    save_path = "./images/input/piyan.jpg"

    while True:
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  

            with open(save_path, "wb") as f:
                f.write(response.content)

        except requests.exceptions.RequestException as e:
            print(f"下載或存檔時發生錯誤：{e}")

        time.sleep(interval)

if __name__ == "__main__":
    main()
