from PIL import Image

img = Image.open('p_23_01.jpg')
pixels = list(img.getdata()) # это функция преобразует в список он дает доступ к пикселям
Pixels = len(pixels)

r, g, b = 0, 0, 0

for pixel in pixels:
    r += pixel[0]
    g += pixel[1]
    b += pixel[2]

print(r // Pixels, g // Pixels, b // Pixels)

