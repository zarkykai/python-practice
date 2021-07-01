from PIL import Image, ImageFont, ImageDraw


def add_num(img,num):
    "输入图像与数字文本"
    w,h=img.size
    font = ImageFont.truetype('arial.ttf', 150)
    draw = ImageDraw.Draw(img)
    draw.text((9 * w / 10, h / 15), num, fill=(255, 10, 10), font=font)
    img.show()
    img.save('withnum.png', 'png')
    return



if __name__ == '__main__':

    image=Image.open('qqhead.jpg')
    #input_num=str(6)
    add_num(image,'6')