from modules.img_imports import *

exts = ('.png', '.jpg', '.jpeg', ".gif")
exclude_dirs = ingore_dirs()
base_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    files = os.listdir(base_dir)
    for file in files:
        path = os.path.join(base_dir, file)
        if os.path.isdir(path):
            if file not in exclude_dirs:
                shutil.rmtree(path)
        else: 
            if file.endswith(exts):
                os.remove(path)