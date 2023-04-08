from PIL import Image


def start():
    empty = Image.open("photo/empty1.png")
    temp = empty.copy()
    temp.save('photo/temp1.png')


def paste(lx, ly, orientation, length):
    if orientation == "v":
        ry = ly + length
        rx = lx + 1
    else:
        rx = lx + length
        ry = ly + 1
    full = Image.open("photo/full1.png")
    temp = Image.open("photo/temp1.png")
    x, y = full.size
    x, y = x // 10, y // 12
    temp.paste(full.crop((x * lx, y * ly, x * rx, y * ry)), (x * lx, y * ly))
    temp.save('photo/temp1.png')
    full.close()
    temp.close()
