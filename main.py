def zdh1():
    from PIL import Image

    img = Image.open('horse.jpg')
    img.show()

    print(img.size)
    print(img.format)
    print(img.mode)

def zdh2_1():
    from PIL import Image

    img = Image.open('horse.jpg')
    img.thumbnail((828/3, 1022/3))
    img.save('mini_horse.jpg')
    img.show()
    print(img.size)

def zdh2_2():
    from PIL import Image

    img = Image.open('horse.jpg')
    r_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    r_img.save('mirror_horse.jpg')
    r_img.show()


def zdh2_3():
    from PIL import Image

    img = Image.open('horse.jpg')
    r_img = img.rotate(180)
    r_img.save('180_horse.jpg')
    r_img.show()

def zdh3():
    from PIL import Image, ImageFilter

    img1 = Image.open('1.jpg')
    img2 = Image.open('2.jpg')
    img3 = Image.open('3.jpg')
    img4 = Image.open('4.jpg')
    img5 = Image.open('5.jpg')

    r_img1 = img1.filter(ImageFilter.EMBOSS)
    r_img1.show()
    r_img1.save('min1.jpg')
    r_img2 = img2.filter(ImageFilter.EMBOSS)
    r_img2.show()
    r_img1.save('min2.jpg')
    r_img3 = img3.filter(ImageFilter.EMBOSS)
    r_img3.show()
    r_img1.save('min3.jpg')
    r_img4 = img4.filter(ImageFilter.EMBOSS)
    r_img4.show()
    r_img1.save('min4.jpg')
    r_img5 = img5.filter(ImageFilter.EMBOSS)
    r_img5.show()
    r_img1.save('min5.jpg')


def zdh4():
    from PIL import Image, ImageDraw, ImageFont
    img = Image.open('bm.jpg')
    width, height = img.size
    draw = ImageDraw.Draw(img)
    text = 'AF'
    font  = ImageFont.truetype('arial.ttf', 60)
    textwidth, textheight = draw.textsize(text, font)
    margin = 10
    x = width - textwidth - margin
    y = height - textheight -  margin
    draw.text((x, y), text, font=font)
    img.show()
    img.save('wm.jpg')







zdh1()
zdh2_1()
zdh2_2()
zdh2_3()
zdh3()
zdh4()

