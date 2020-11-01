from PIL import Image, ImageDraw
from pathlib import Path

images_folder = Path("images/")


def decode():
    message_img = images_folder / "fb_secret.png"
    img = Image.open(message_img)
    pixmap = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r,g,b = pixmap[x,y]
            print(r,g,b,end='-')
    print()
    img.show()

           
if __name__ == "__main__":
    decode()