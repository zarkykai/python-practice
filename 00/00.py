from PIL import Image, ImageFont, ImageDraw

image_address = 'qqhead.jpg'
input_num = '6'


def add_num(img, num):
    "输入图像与数字文本"
    w, h = img.size
    font = ImageFont.truetype('arial.ttf', 150)

    canvas = ImageDraw.Draw(img)
    pos = (9 * w / 10, h / 15)
    canvas.text(pos, num, fill=(255, 10, 10), font=font)

    img.show()
    img.save('withnum.png', 'png')
    return img


if __name__ == '__main__':

    image = Image.open(image_address)

    processed_image=add_num(image, input_num)
