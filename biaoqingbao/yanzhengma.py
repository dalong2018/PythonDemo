# Author:wangxz

from PIL import Image

infile = 'D:\\biaoqingbao\\11.jpg'
outfile = 'D:\\biaoqingbao\\m11.jpg'
im = Image.open (infile)
(x, y) = im.size  # read image size
x_s = 80  # define standard width
y_s = 100  # calc height based on standard width
out = im.resize ((x_s, y_s), Image.ANTIALIAS)  # resize image with high-quality
out.save (outfile)

print('original size: ', x, y)
print('adjust size: ', x_s, y_s)