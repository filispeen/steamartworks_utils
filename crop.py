from modules.img_imports import *

def save_cropped(cropped, out_path, target_size):
    cropped = cropped.resize(target_size, Image.LANCZOS)
    cropped.save(out_path)
    cropped.close()
    print(f"Saved: {out_path}")

def crop_image_to_5_horizontal(image_path, output_dir=None):
    with Image.open(image_path) as img:
        width, height = img.size
        part_width = width // 5
        target_size = (part_width, height)

        if output_dir is None:
            output_dir = os.path.dirname(image_path)
        os.makedirs(output_dir, exist_ok=True)

        tasks = []
        for i in range(5, 0, -1):
            idx = 5 - i
            left = idx * part_width
            right = (idx + 1) * part_width if idx < 4 else width
            cropped = img.crop((left, 0, right, height))
            out_path = os.path.join(
                output_dir,
                f"{os.path.splitext(os.path.basename(image_path))[0]}_part{i}.png"
            )
            tasks.append((cropped, out_path, target_size))

    with ThreadPoolExecutor() as executor:
        executor.map(lambda args: save_cropped(*args), tasks)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    folders = []
    for folder in os.listdir(base_dir):
        folder_path = os.path.join(os.path.join(base_dir, folder))
        if os.path.isdir(folder_path) and folder not in ["upload", ".git", "modules", ".venv"]:
            if "resized_all_combined.png" not in os.listdir(folder_path): folders.append(os.path.join(folder, "all_combined.png"))
            else: folders.append(os.path.join(folder, "resized_all_combined.png"))
    
    with ThreadPoolExecutor() as executor:
        for folder_path in folders:
            executor.submit(crop_image_to_5_horizontal, folder_path)