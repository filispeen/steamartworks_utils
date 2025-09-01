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
    image_path = fr"{os.path.dirname(os.path.abspath(__file__))}\resized_all_combined.png"
    crop_image_to_5_horizontal(image_path)
