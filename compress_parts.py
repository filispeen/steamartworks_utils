from modules.img_imports import *

def compress_file(iFile, oFile):
   os.system(f"ffmpeg -y -v quiet -stats -i {iFile} -q:v 0 {oFile}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    folders = []
    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)
        if os.path.isdir(folder_path) and folder not in [".git", "modules", ".venv"]:
            folders.append(folder_path)
    
    with ThreadPoolExecutor() as executor:
        for folder in folders:
            if "upload" not in os.listdir(folder): os.makedirs(os.path.join(folder, "upload"))
            for file in os.listdir(folder):
                if "resized_all_combined_" in file and file.endswith('.png'):
                    iFile = os.path.join(folder, file)
                    oFile = os.path.join(folder, os.path.join("upload", file.replace(".png", ".jpg")))
                    executor.submit(compress_file, iFile, oFile)            