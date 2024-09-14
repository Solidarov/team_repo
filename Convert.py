from PIL import Image
import os

input_folder = 'dds_input'
output_folder = 'png_output'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file_name in os.listdir(input_folder):
    if file_name.endswith('.dds'):
        img = Image.open(os.path.join(input_folder, file_name))
        img.save(os.path.join(output_folder, file_name.replace('.dds', '.png')))