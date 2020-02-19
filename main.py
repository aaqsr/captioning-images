from imgprocessingfunc import cropit, mini_cropit, add_border, drawText, drawTitle
import quotes
from PIL import Image, ImageFont, ImageDraw, ImageOps
import os

p = 'D:\\vscode\pyth image work\images'
skipped = []

if os.path.exists(p) and os.path.isdir(p):
    for name in os.listdir(p):
        if name != '.DS_Store':
            print(name)
            filename = name.replace('.JPG', '').replace('.jpg', '')
            try:
                print(quotes.quotes[filename])
                img = Image.open(
                    "D:\\vscode\pyth image work\images\{}".format(name))
                # img = cropit(img)
                img = mini_cropit(img)
                img = add_border(img)
                drawText(quotes.quotes[filename], img)
                drawTitle(filename, img)
                img.save("out/{}".format(name))
            except:
                print('Error, likely quote not found, skipping')
                skipped.append(filename)
else:
    print("Not a valid path bruh")

print('Skipped the following:\n')
print(skipped)
                
# TODO WHAT IF WE PUT THE TITLE ON THE TOP??
# TODO Fix the title's placement, it's clipping through the quotes. Also fix the quote's placement
