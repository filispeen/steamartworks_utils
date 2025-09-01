from modules.img_imports import *

Image.MAX_IMAGE_PIXELS = None

target = fr"{os.path.dirname(os.path.abspath(__file__))}\all_combined.png"
target_height = 65000 # max jpg resolution

def save_resized(img, path):
    img.save(path)
    print(f"Saved resized image as {path} ({img.width}x{img.height})")

if os.path.exists(target):
    img = Image.open(target)
    w, h = img.size
    
    new_h = target_height
    new_w = int(w * (new_h / h))
    
    resized_img = img.resize((new_w, new_h), Image.LANCZOS)
    out_path = f"resized_{target}"
    
    with ThreadPoolExecutor() as executor:
        executor.submit(save_resized, resized_img, out_path)
else:
    print(f"File {target} not found.")
