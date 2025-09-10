import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.img_imports import *
from modules.imports import list_folders, click

def save_cropped(cropped, out_path, target_size, horizontal_resize=True):
    if horizontal_resize:
        target_size = (152, cropped.size[1])
        cropped = cropped.resize(target_size, Image.LANCZOS)
    else:
        cropped = cropped.resize(target_size, Image.LANCZOS)
    cropped.save(out_path)
    cropped.close()
    print(f"Saved: {out_path}")

def crop_image_to_5_horizontal(image_path, output_dir=None, horizontal_resize=True):
    H_resize = horizontal_resize
    with Image.open(image_path) as img:
        width, height = img.size
        part_width = width // 5
        target_size = (part_width, height)

        if output_dir is None:
            output_dir = os.path.join(os.path.dirname(image_path), "upload")
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
            #print(f"Generated path: {out_path}")
            if "all_combined_part" in out_path and "resized_all_combined_part" not in out_path:
                out_path = out_path.replace("all_combined_part", "resized_all_combined_part")
                print(f"Processing and saving: {out_path}")
            tasks.append((cropped, out_path, target_size, H_resize))

    with ThreadPoolExecutor() as executor:
        for task in tasks:
            executor.submit(save_cropped, *task)

@click.command()
@click.option("--h-resize", help='Yes/No to resize horizontally into perfect resolution for work.', default=True, type=bool)
@click.option("--base-dir", help='Base directory containing subdirectories with images.')
def main(base_dir=None, h_resize=True):
    folders = []
    if base_dir is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        for folder in list_folders(base_dir):
            folders.append(os.path.join(base_dir, folder))
    else:
        folders = [ base_dir ]

    if len(folders) > 0:
        print(f"Cropping images in {len(folders)} folders")

    image_paths = []
    for folder in folders:
        if not os.path.isdir(folder):
            continue
        files = os.listdir(folder)
        if "resized_all_combined.png" in files:
            image_paths.append(os.path.join(folder, "resized_all_combined.png"))
        else:
            if "all_combined.png" in files:
                image_paths.append(os.path.join(folder, "all_combined.png"))

    print(f"{len(image_paths)} images to process.")
    with ThreadPoolExecutor() as executor:
        for image_path in image_paths:
            print(image_path)
            executor.submit(crop_image_to_5_horizontal, image_path, horizontal_resize=h_resize)

if __name__ == "__main__":
    main()