from modules.img_imports import *

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

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    folders = []
    for folder in os.listdir(base_dir):
        folder_path = os.path.join(os.path.join(base_dir, folder))
        if os.path.isdir(folder_path) and folder not in ["upload", ".git", "modules", ".venv", ".ignore"]:
            folders.append(folder)
    
    with ThreadPoolExecutor() as executor:
        for folder_path in folders:
            executor.submit(process, folder_path)