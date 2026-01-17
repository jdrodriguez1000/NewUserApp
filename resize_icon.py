from PIL import Image
import os

def resize_icon():
    base_path = os.path.dirname(__file__)
    input_path = os.path.join(base_path, "assets", "icon.png")
    output_path_png = os.path.join(base_path, "assets", "icon_small.png")
    output_path_ico = os.path.join(base_path, "assets", "icon.ico")
    
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found")
        return

    try:
        with Image.open(input_path) as img:
            # Resize to standard icon size (64x64)
            img_resized = img.resize((64, 64), Image.Resampling.LANCZOS)
            img_resized.save(output_path_png, "PNG")
            
            # Save as ICO (supports multiple sizes, but 64x64 is fine)
            img.save(output_path_ico, format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
            print(f"Successfully created: {output_path_png} and {output_path_ico}")
    except Exception as e:
        print(f"Error resizing icon: {e}")

if __name__ == "__main__":
    resize_icon()
