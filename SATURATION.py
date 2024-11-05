from PIL import Image, ImageEnhance, ImageFilter
from utils import show_vertical, show_horizontal, in_file, out_file
import os

#INPUT_DIR = os.path.join('filtros', 'data')
#OUTPUT_DIR = os.path.join('filtros', 'output')

image = Image.open(in_file("dead_nature.jpg"))

saturation = ImageEnhance.Color(image)
contrast = ImageEnhance.Contrast(image)
brightness = ImageEnhance.Brightness(image)
sharpness = ImageEnhance.Sharpness(image)

def duno_filtro(img):
    
    contrast = ImageEnhance.Contrast(img)
    contrastado = contrast.enhance(1.1)
    
    brightness = ImageEnhance.Brightness(contrastado)
    brilho = brightness.enhance(1.1)    
    
    saturation = ImageEnhance.Color(brilho)
    saturada = saturation.enhance(1.3)
    
    
    #brightness = ImageEnhance.Brightness(image)
    #original = Image.open(in_file(im))
    #brilho = brightness.enhance(1.1)
    #saturation = ImageEnhance.Color(original)
    #saturation = ImageEnhance.Color(brilho)
    #saturada = saturation.enhance(2)
    
    #duno_filtro(image)

    # contrate = ImageEnhance.Contrast

    return saturada

if __name__ == "__main__":
    
    image = Image.open(in_file("dead_nature.jpg"))
    Img_sat = duno_filtro(image
                          )
    show_horizontal(image, Img_sat)