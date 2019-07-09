# Author:wangxz

from PIL import Image
img = Image.open('D:/ning.jpg')
new_img= img.resize((295, 413),Image.ANTIALIAS) # w代表宽度，h代表高度，最后一个参数指   定采用的算法
new_img.save('D:/newimg.jpg',quality=100)