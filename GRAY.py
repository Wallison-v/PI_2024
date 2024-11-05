from PIL import Image
from utils import in_file, out_file, show_horizontal

def media_grayscale(colored):
    w, h = colored.size
    img = Image.new("RGB", (w, h))

    for x in range(w):
        for y in range(h):
            pxl = colored.getpixel((x,y))
            # média das coordenadas RGB
            lum = (pxl[0] + pxl[1] + pxl[2])//3
            img.putpixel((x,y), (lum, lum, lum))
    return img

def grayscale(colored):
    w, h = colored.size
    img = Image.new("RGB", (w, h))

    for x in range(w):
        for y in range(h):
            pxl = colored.getpixel((x,y))
            # média ponderada das coordenadas RGB
            lum = int(0.3*pxl[0] + 0.59*pxl[1] + 0.11*pxl[2])
            img.putpixel((x,y), (lum, lum, lum))

    return img
            

if __name__ == "__main__":
    img = Image.open(in_file("noite_estrelada.jpg"))
    print(img.getpixel((100, 100)))
    # print(img.getpixel((500, 300)))
    # print(img.getpixel((300, 180)))

    # pb_baloes = grayscale(baloes)
    # pb_baloes.save(out_file("pb_baloes2.jpg"))
    pb_nature = media_grayscale(img)

    pb_nature2 = grayscale(img)

    show_horizontal(img, pb_nature)

    show_horizontal(img, pb_nature2)

    #pb_nature.save(out_file("noite_estrelada2.jpeg"))
    #grayscale(img).save(out_file("dead_nature.jpg"))