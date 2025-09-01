from modules.img_imports import *

def delete_file(f):
    try:
        os.remove(f)
        print(f"Deleted: {f}")
    except Exception as e:
        print(f"Error deleting {f}: {e}")

if __name__ == "__main__":
    exts = ('.png', '.jpg', '.jpeg')
    script_name = os.path.basename(__file__)
    files = [f for f in os.listdir('.') if f.endswith(exts) and f != script_name]
    with ThreadPoolExecutor() as executor:
        executor.map(delete_file, files)