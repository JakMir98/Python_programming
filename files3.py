#!/usr/bin/python
#from Pil import Image
from PIL import Image, ImageDraw
import glob

for i in range(0, 4):
    img = Image.new('RGB', (200, 200), color='red')
    d = ImageDraw.Draw(img)
    d.text((60, 60), "Hello World " + str(i), fill=(255, 255, 0))
    img.save('pil_red'+str(i)+'.jpg')


for file in glob.glob("*.jpg"):
    im = Image.open(file)
    rgb_im = im.convert('RGB')
    rgb_im.save(file.replace("jpg", "png"), quality=95)
