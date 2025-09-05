from modules.img_imports import *
from modules.imports import ingore_dirs, click

def compress_file(iFile, oFile):
   os.system(f"ffmpeg -y -v quiet -stats -i {iFile} -q:v 0 {oFile}")

@click.command()
@click.option('--base-dir', help='Base directory containing subdirectories with images.')
def main(base_dir=None):
    if base_dir is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        folders = []
    else:
        folders = [ base_dir ]

    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)
        if ".ignore" in folder_path: break
        if os.path.isdir(folder_path) and folder not in ingore_dirs():
            folders.append(folder_path)
    
    with ThreadPoolExecutor() as executor:
        for folder in folders:
            if "upload" not in os.listdir(folder): os.makedirs(os.path.join(folder, "upload"))
            for file in os.listdir(folder):
                if "resized_all_combined_" in file and file.endswith('.png'):
                    iFile = os.path.join(folder, file)
                    oFile = os.path.join(folder, os.path.join("upload", file.replace(".png", ".jpg")))
                    executor.submit(compress_file, iFile, oFile)

if __name__ == "__main__":
    main() 