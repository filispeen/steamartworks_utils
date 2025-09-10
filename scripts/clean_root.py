import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.img_imports import *

exts = ('.png', '.jpg', '.jpeg', ".gif")
exclude_dirs = ingore_dirs()
base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

if __name__ == "__main__":
    print(f"Cleaning up the root directory: {base_dir}")
    files = os.listdir(base_dir)
    for file in files:
        path = os.path.join(base_dir, file)
        if os.path.isdir(path):
            if file not in exclude_dirs:
                print(f"Removing directory and all its contents: {path}")
                shutil.rmtree(path)
        else: 
            if file.endswith(exts):
                print(f"Removing file: {path}")
                os.remove(path)