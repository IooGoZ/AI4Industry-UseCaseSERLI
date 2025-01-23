import os
from PIL import Image

def convert_png_to_jpeg(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpg")

            with Image.open(input_path) as img:
                rgb_img = img.convert('RGB')
                rgb_img.save(output_path, 'JPEG')
                print(f"Converti : {input_path} -> {output_path}")




convert_png_to_jpeg(input_folder, output_folder)
print("Conversion terminée.")
