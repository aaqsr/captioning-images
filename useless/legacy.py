from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def addtext(file, text, output): 
    # takes the file name, the text to be written, the coords in a tuple, and output name
    img = Image.open(file)
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(text, f)   
    if w > img.width:
        lineCount = int(round((w / img.width) + 1))
    print("lineCount: {}".format(lineCount))

    lines = []
    if lineCount > 1:
        lastCut = 0
        isLast = False
        for i in range(0,lineCount):
            if lastCut == 0:
                cut = (len(text) / lineCount) * i
            else:
                cut = lastCut
            if i < lineCount-1:
                nextCut = (len(text) / lineCount) * (i+1)
            else:
                nextCut = len(text)
                isLast = True
            print("cut: {} -> {}".format(cut, nextCut))
            # make sure we don't cut words in half
            if (nextCut == len(text) or text[nextCut] == " "):
                print("may cut")
            else:
                print("may not cut")
                while text[nextCut] != " ":
                    nextCut += 1
                print("new cut: {}".format(nextCut))
            line = text[cut:nextCut].strip()
            # is line still fitting ?
            w, h = draw.textsize(line, font)
            if not isLast and w > img.width:
                print("overshot")
                nextCut -= 1
                while text[nextCut] != " ":
                    nextCut -= 1
                print("new cut: {}".format(nextCut))
            lastCut = nextCut
            lines.append(text[cut:nextCut].strip())
    else:
        lines.append(text)
    print(lines)
    
    for i in range(0, lineCount):
        w, h = draw.textsize(lines[i], font)    
        draw.text((img.width/2 - w/2, 10), lines[i], (255,255,255), font=f)
        img.save(output)   
             
    return



f = ImageFont.truetype("Impact.ttf", 70)

text = "Hello mama what are you upto yeah yeah yeah yeah yeah adjkwaldjwakljdaklwjdawldjawk boop de boop222222 awkdak yeah"

addtext("image.jpg", text, "out.jpg")
