from imgprocessingfunc import cropit, add_border, drawText, drawTitle
import quotes
from PIL import Image, ImageFont, ImageDraw, ImageOps
import os

imgpath = "images/"
outpath = "out/"
check = os.path.exists(imgpath) and os.path.isdir(imgpath) and os.path.exists(outpath) and os.path.exists(imgpath)
skipped = []

if check:
    ls = os.listdir(imgpath)
    for name in ls:
        # if name != '.DS_Store': Run if you're on Mac. Optional because the exception handling catches .DS_Store either way.
            print(name)
            filename = name.replace('.jpg', '').replace('.JPG', '').replace('.png', '').replace('.PNG', '')
            try:
                print(quotes.quotes[filename])
                img = Image.open(imgpath + name)
                img = cropit(img)
                img = add_border(img)
                drawText(quotes.quotes[filename], img)
                drawTitle(filename.capitalize(), img)
                img.save(outpath + name)
            except:
                print('Error, likely quote not found or image too small for quote, skipping')
                skipped.append(filename)
else:
    print("Path not found")

print('\nSkipped the following:\n')
print(skipped)
