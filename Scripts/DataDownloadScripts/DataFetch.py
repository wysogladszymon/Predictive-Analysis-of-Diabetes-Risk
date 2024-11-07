import os
import zipfile
import subprocess

def download_dataset(folder_name = "Data/InputData/"):
  zip_file_name = "pima-indians-diabetes-database.zip"
  file_name = "diabetes.csv"
  if not os.path.exists(folder_name + file_name):
    if not os.path.exists(folder_name):
      os.makedirs(folder_name)
      print(f"Folder '{folder_name}' created.")

    if not os.path.exists(zip_file_name):
      subprocess.run(["kaggle", "datasets", "download", "-d", "uciml/pima-indians-diabetes-database", "-p", folder_name], check=True)

    with zipfile.ZipFile(folder_name + zip_file_name, 'r') as zip_ref:
      zip_ref.extractall(folder_name)

    os.remove(folder_name + zip_file_name)
    print("Data fetched successfully.")
  else:
    print(f"File '{file_name}' already exists.")

download_dataset()
