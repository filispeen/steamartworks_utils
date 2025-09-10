import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.img_imports import *
from modules.imports import list_folders, click

Image.MAX_IMAGE_PIXELS = None

target_height = 65000 # max jpg resolution

def save_resized(img, path):
    img.save(path)
    print(f"Saved resized image as {path} ({img.width}x{img.height})")

def process(target):
    target=os.path.join(target, "all_combined.png")
    if os.path.exists(target):
        img = Image.open(target)
        w, h = img.size
        
        new_h = target_height
        new_w = int(w * (new_h / h))
        
        resized_img = img.resize((new_w, new_h), Image.LANCZOS)
        out_path = target.replace("all_combined", "resized_all_combined")

        with ThreadPoolExecutor() as executor:
            executor.submit(save_resized, resized_img, out_path)
    else:
        print(f"File {target} not found.")

@click.command()
@click.option('--base-dir', help='Base directory containing subdirectories with images.')
def main(base_dir=None):
    if base_dir is None:
        base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
        folders = list_folders(base_dir)
    else:
        folders = [ base_dir ]

    if len(folders) > 0:
        print(f"Resizing images parts in {len(folders)} folders")
    
    with ThreadPoolExecutor() as executor:
        for folder_path in folders:
            executor.submit(process, folder_path)

if __name__ == "__main__":
    main()