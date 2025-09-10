import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.img_imports import *
from modules.imports import *

def combine_images_vertically(folder_path, output_name="all_combined.png"):
    extensions = ('.png', '.jpg', '.jpeg')

    images = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith(extensions) and os.path.splitext(f)[0]
    ]
    images.sort(key=lambda x: int(os.path.splitext(x)[0]))

    if not images:
        print(f"No valid images found in {folder_path}")
        return

    image_objs = [Image.open(os.path.join(folder_path, img)) for img in images]
    target_width = max(im.width for im in image_objs)

    resized_images = []
    for im in image_objs:
        if im.width != target_width:
            new_height = int(im.height * (target_width / im.width))
            im = im.resize((target_width, new_height), Image.LANCZOS)
        resized_images.append(im)

    widths, heights = zip(*(img.size for img in resized_images))
    total_height = sum(heights)
    max_width = max(widths)

    combined = Image.new('RGB', (max_width, total_height))
    y_offset = 0
    for img in resized_images:
        combined.paste(img, (0, y_offset))
        y_offset += img.height

    output_path = os.path.join(folder_path, output_name)
    combined.save(output_path)
    print(f"Combined image saved to {output_path}")

@click.command()
@click.option('--base-dir', help='Base directory containing subdirectories with images.')
def main(base_dir=None):
    if base_dir is None:
        base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
        folders = list_folders(base_dir)
    else:
        folders = [ base_dir ]

    print(f"Combining images in {len(folders)} folders")

    with ThreadPoolExecutor() as executor:
        for folder_path in folders:
            executor.submit(combine_images_vertically, folder_path)

if __name__ == "__main__":
    main()