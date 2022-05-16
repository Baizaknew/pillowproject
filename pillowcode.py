from PIL import Image, ImageDraw, ImageFont
import os

folder_path = 'img'
new_folder = 'b_w_img'
img_files = [item for item in os.listdir(folder_path)]


def crop_img(img_path: str):
    path = os.path.join(folder_path, img_path)
    new_path = os.path.join(new_folder, img_path[:-4])

    image = Image.open(path)
    draw = ImageDraw.Draw(image)
    text = 'watermark'
    font = ImageFont.truetype('Ubuntu-R.ttf', 36)
    text_width, text_height = draw.textsize(text, font)

    width, height = image.size
    new_width = 1080
    new_height = 1080

    left = (width - new_width) / 2
    top = (height - new_height) / 2
    right = (width + new_width) / 2
    bottom = (height + new_height) / 2

    x = width - text_width - 10
    y = height - text_height - 10

    draw.text((x, y), text, font=font)
    image = image.convert('L').crop((left, top, right, bottom))
    image.save(f'{new_path}_black_&_white.jpg')


for image in img_files:
    crop_img(image)