import os
import zipfile

def zip_current_directory(zip_name="content.zip"):
    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
        for filename in os.listdir("."):
            if os.path.isfile(filename) and (filename != zip_name and filename != 'zip_creator.py'):
                zipf.write(filename)
                print(f"Added: {filename}")

if __name__ == "__main__":
    zip_current_directory()
    print("ZIP-Datei 'content.zip' wurde erstellt.")
