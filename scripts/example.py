import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.img_imports import *

def generate_images(output_dir="example", count=52, width=760, height=1250):
    os.makedirs(output_dir, exist_ok=True)
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()

    for i in range(1, count + 1):
        img = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(img)

        margin = 50
        draw.rectangle(
            [margin, margin, width - margin, height - margin],
            outline="black",
            width=5
        )

        text = f"Image {i}"
        bbox = draw.textbbox((0, 0), text, font=font)  # (x0, y0, x1, y1)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        text_x = (width - text_width) // 2
        text_y = (height - text_height) // 2
        draw.text((text_x, text_y), text, fill="black", font=font)

        img.save(os.path.join(output_dir, f"{i:03}.png"))
        print(f"Created: {i:03}.png")

if __name__ == "__main__":
    generate_images()