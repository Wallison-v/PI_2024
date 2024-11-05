import os
from PIL import Image, ImageFont, ImageDraw
from utils import show_vertical, show_horizontal, in_file, out_file


def openimage(filename):
    return Image.open(os.path.join("filtros/data/", filename))

def negative(img:Image)->Image:
    """Retorna uma nova imagem correspondente ao negativo de img"""
    
    negated = Image.new(img.mode, img.size, "red")
    w, h = negated.size
    for i in range(w):
        for j in range(h):
            if img.mode == "RGB":
                r, g, b = img.getpixel((i,j))
                negated.putpixel((i,j), (255-r, 255-g, 255-b))
            elif img.mode == "RGBA":
                r, g, b, a = img.getpixel((i,j))
                negated.putpixel((i,j), (255-r, 255-g, 255-b, a))
            else:
                # silent failure
                pass
    return negated

if __name__ == '__main__':
    
    img = openimage("dead_nature.jpg")
    neg = negative(img)

    show_horizontal(img, neg)
    