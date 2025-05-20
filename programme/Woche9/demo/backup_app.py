import os
import zipfile

def create_zip_file():
    zip_name = "backup.zip"
    current_dir = os.getcwd()
    with zipfile.ZipFile(zip_name, 'w') as zip_file:
        for file in os.listdir(current_dir):
            file_path = os.path.join(current_dir, file)
            if os.path.isfile(file_path) and file != zip_name:
                zip_file.write(file_path, arcname=file)

def main():
    create_zip_file()

main()