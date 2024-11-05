# Apresentação de filtros
from PIL import Image, ImageFilter
from math import sqrt
import os
from utils import show_vertical, show_horizontal, in_file, out_file

# Caminho relativo das pastas de entrada e saída de imagens
INPUT_DIR = os.path.join('filtros', 'data')
OUTPUT_DIR = os.path.join('filtros', 'output')

def show_box_blur(filename, r):
    '''Aplica um filtro BoxBlur à imagem, exibe e salva o resultado'''

    original = Image.open(in_file(filename))
    filtered = original.filter(ImageFilter.BoxBlur(r))

    #Mostrar as imagens lado a lado
    show_horizontal(original, filtered)
    filtered.save(
        out_file(
            '{}_boxblur_{}.jpg'.format(filename[:filename.index('.')], r)
        )
    )

if __name__ == "__main__":
    # Experimente outras imagens e tamanhos de filtros
    show_box_blur('noite_estrelada.jpg', 10)