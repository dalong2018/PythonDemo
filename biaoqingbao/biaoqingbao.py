# Author:wangxz


from PIL import Image, ImageDraw, ImageFont
# img = Image.open("D:/biaoqingbao/11.jpg")
# jgz =Image.open("D:/biaoqingbao/a24.jpg")
# img.paste(jgz,(73,42))
# img.show()

img = Image.open("D:/biaoqingbao/11.jpg")
draw = ImageDraw.Draw(img)
ttfront = ImageFont.truetype('simhei.ttf', 30)
draw.text((225, 450),"梅西做测试！",fill=(0,0,0), font=ttfront)
img.show()
img.save("D:/biaoqingbao/m88.jpg")
