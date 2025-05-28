from PIL import Image, ImageDraw

def picture(file_name, widht, hight, sky_color="#87CEEB", ocean_color="#017B92", boat_color="#874535", sail_color="#FFFFFF", sun_color="#FFCF40"):
    im = Image.new('RGB', (widht, hight), sky_color)
    draw = ImageDraw.Draw(im)

    draw.rectangle(((0, hight*0.8), (widht, hight)), ocean_color)

    draw.ellipse(((widht*0.8, -(hight*0.2)), (widht*1.2, hight*0.2)), sun_color)

    x1, x2, x3, x4 = widht*0.3, widht*0.25, widht*0.75, widht*0.7
    y1, y2, y3, y4 = hight*0.85, hight*0.65, hight*0.65, hight*0.85
    draw.polygon(((x1, y1), (x2, y2), (x3, y3), (x4, y4)), boat_color)

    draw.rectangle(((widht*0.49, hight*0.3), (widht*0.51, hight*0.65)), boat_color)

    x1, x2, x3 = widht*0.51, widht*0.66, widht*0.51
    y1, y2, y3 = hight*0.3, hight*0.45, hight*0.6
    draw.polygon(((x1, y1), (x2, y2), (x3, y3)), sail_color)
    im.save(file_name)


picture("test.bmp", 1000, 800)