from modules.img_imports import *

def combine_images_vertically(folder_path, output_name="all_combined.png"):
    extensions = ('.png', '.jpg', '.jpeg')

    images = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith(extensions) and os.path.splitext(f)[0]
    ]
    images.sort(key=lambda x: int(os.path.splitext(x)[0]))

    print(images)
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

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    folders = []
    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)
        if os.path.isdir(folder_path) :
            for dir_to_ignore in ingore_dirs():
                if folder == dir_to_ignore:
                    break
            print(f"Adding folder for process: {folder}")
            folders.append(folder)

    with ThreadPoolExecutor() as executor:
        for folder_path in folders:
            executor.submit(combine_images_vertically, folder_path)
