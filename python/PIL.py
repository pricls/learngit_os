# -*- coding:UTF-8 -*-
from PIL import Image
# 打开一个jpg图像文件，注意路径:
im = Image.open('/home/master/图片/R1.jpg')
# 获得图像尺寸:
w,h = im.size
print('Original image size: %sx%s' % (w,h))
# 缩放到50%:
im.thumbnail((w//2,h//2))
print('Resize image to: %sx%s' %(w//2,h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('./workimage/thumbnail.jpg','jpeg')

#模糊效果 (ImageFilter=图像滤镜)
from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意路径:
im = Image.open('/home/master/图片/R1.jpg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR) #(BLUR=模糊)
im2.save('./workimage/blur.jpg', 'jpeg')

#绘图方法
#生成字母验证码图片：
from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random #随机

# 随机字母:
def ranChar():
	return chr(random.randint(65,90))
# 随机颜色1:
def rndColor():
	return (random.randint(32,127),random.randint(64,255),random.randint(64,255))

# 随机颜色2:
def rndColor2():
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB',(width, height),(255,255,255))
# 创建Font对象:
font = ImageFont.truetype('/usr/share/fonts/gnu-free/FreeMonoOblique.ttf',36)
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=rndColor())
# 输出文字:
for t in range(4):
	draw.text((60 * t + 10, 10),ranChar(),font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('./workimage/code.jpg','jpeg')
