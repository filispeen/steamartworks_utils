from modules.img_imports import *

def list_folders(base_dir):
    folders = []
    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)
        if ".ignore" in folder_path: break
        if os.path.isdir(folder_path) and folder not in ingore_dirs()+["merged"]:
            folders.append(folder)
    return sorted(folders)

def merge_folders(base_dir, output_folder="merged"):
    folders = list_folders(base_dir)
    print(f"Folders to process: {folders}")
    output_path = os.path.join(base_dir, output_folder)
    if os.path.exists(output_path): shutil.rmtree(output_path)
    os.makedirs(output_path, exist_ok=True)
    file_counter = 1

    # Збираємо всі файли з усіх папок у новому порядку
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        print(f"Processing folder: {folder_path}")
        for fname in sorted(os.listdir(folder_path), key=len):
            fpath = os.path.join(folder_path, fname)
            # Виключаємо файли, що містять 'all_combined' у назві
            if os.path.isfile(fpath) and 'all_combined' not in fname:
                ext = os.path.splitext(fname)[1]
                new_name = f"{file_counter:03d}{ext}"
                new_path = os.path.join(output_path, new_name)
                print(f"Copying {fpath} to {new_path}")
                shutil.copy2(fpath, new_path)
                file_counter += 1
        # Перейменовуємо папку після обробки
        new_folder_path = folder_path + ".ignore"
        os.rename(folder_path, new_folder_path)
        print(f"Renamed folder {folder_path} -> {new_folder_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    merge_folders(base_dir)