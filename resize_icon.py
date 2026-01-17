from PIL import Image
import os

def resize_icon():
    base_path = os.path.dirname(__file__)
    input_path = os.path.join(base_path, "assets", "icon.png")
    output_path = os.path.join(base_path, "assets", "icon_small.png")
    
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found")
        return

    try:
        with Image.open(input_path) as img:
            # Resize to standard icon size (64x64)
            img = img.resize((64, 64), Image.Resampling.LANCZOS)
            img.save(output_path, "PNG")
            print(f"Successfully created: {output_path}")
    except Exception as e:
        print(f"Error resizing icon: {e}")

if __name__ == "__main__":
    resize_icon()
