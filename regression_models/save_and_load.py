# To get the dataset from the drive direct link and save it locally.
import requests
from pathlib import Path
import os

dir_name = "../Datasets/"

try:
    os.mkdir(dir_name)
except FileExistsError:
    print(f"The directory '{dir_name}' already exists.")
else:
    print(f"The directory '{dir_name}' was successfully created.")

def download_file(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully and saved at: {save_path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

url = "https://drive.google.com/uc?export=download&id=1E0r5bjf6MRQT07K5An0jphmRAFU82DEf"
save_path = Path("../Datasets/car_info_by_car_dekha.csv.csv")

download_file(url, save_path)