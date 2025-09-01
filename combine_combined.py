from modules.img_imports import *

def open_image(img_path):
    return Image.open(img_path)

def rename_combined_image(folder_path, new_name="combined_2x.png"):
    old_name = "combined_upscayl_2x_upscayl-standard-4x.png"
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed {old_name} to {new_name} in {folder_path}")
    else:
        print(f"{old_name} not found in {folder_path}")

def combine_all_combined_images(base_dir, output_name="all_combined.png"):
    folders = [
        folder for folder in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, folder))
    ]
    folders.sort()

    combined_images = []
    for folder in folders:
        rename_combined_image(os.path.join(base_dir, folder))
        img_path = os.path.join(base_dir, folder, "combined_2x.png")
        if os.path.exists(img_path):
            combined_images.append(img_path)

    with ThreadPoolExecutor() as executor:
        image_objs = list(executor.map(open_image, combined_images))
    widths, heights = zip(*(img.size for img in image_objs))

    total_height = sum(heights)
    max_width = max(widths)

    combined = Image.new('RGB', (max_width, total_height))
    y_offset = 0
    for img in image_objs:
        combined.paste(img, (0, y_offset))
        y_offset += img.height

    out_path = os.path.join(base_dir, output_name)
    combined.save(out_path)
    print(f"Combined image saved to {out_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    rename_combined_image(base_dir)
    combine_all_combined_images(base_dir)