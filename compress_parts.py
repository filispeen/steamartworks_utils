from modules.img_imports import *

def compress_file(f):
    out_file = f.replace('.png', '.jpg')
    if "upload" not in os.listdir("."): os.makedirs("upload")
    os.system(f"ffmpeg -y -i {f} -q:v 0 upload\{out_file}")

if __name__ == "__main__":
    files = [
        f for f in os.listdir('.')
        if "resized_all_combined_" in f and f.endswith('.png') and not f.endswith('_c.png')
    ]
    print(files)
    with ThreadPoolExecutor() as executor:
        executor.map(compress_file, files)