from PIL import Image
from pathlib import Path

images_folder = Path("images/")


def iron_puzzle():
    iron_img = images_folder / "iron-puzzle.png"
    img = Image.open(iron_img)
    pixmap = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r,g,b,a = pixmap[x,y]
            # do stuff

    img.show()

def copper_puzzle():
    copper_img = images_folder / "copper-puzzle.png"
    img = Image.open(copper_img)
    pixmap = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r,g,b,a = pixmap[x,y]
            # do stuff

    img.show()

def west_puzzle():
    west_img = images_folder / "west-puzzle.png"
    img = Image.open(west_img)
    pixmap = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r,g,b,a = pixmap[x,y]
            # do stuff
            
    img.show()

def my_puzzle():
    '''
    This function should open an image, "noisify" it by 
    changing some of the color channels to random numbers
    and doing some other transformations on the 3rd color
    and save the image as my-puzzle.png
    '''
    pass

if __name__ == "__main__":
    # feel free to comment out functions you're not using
    iron_puzzle()
    copper_puzzle()
    west_puzzle()
    my_puzzle()