from imgprocessingfunc import cropit, add_border, drawText, drawTitle
import quotes
from PIL import Image, ImageFont, ImageDraw, ImageOps
import os

p = "/Users/apple/Documents/pyth image work/images"
skipped = []

if os.path.exists(p) and os.path.isdir(p):
    for name in os.listdir(p):
        if name != '.DS_Store':
            print(name)
            filename = name.replace('.jpg', '')
            try:
                print(quotes.quotes[filename])
                img = Image.open(
                    "/Users/apple/Documents/pyth image work/images/{}".format(name))
                img = cropit(img)
                img = add_border(img)
                drawText(quotes.quotes[filename], img)
                drawTitle(filename, img)
                img.save("out/{}".format(name))
            except:
                print('Error, likely quote not found, skipping')
                skipped.append(filename)

print('Skipped the following:\n')
print(skipped)
                
# TODO WHAT IF WE PUT THE TITLE ON THE TOP??
# TODO Fix the title's placement, it's clipping through the quotes. Also fix the quote's placement
