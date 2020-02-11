from PIL import Image, ImageFont, ImageDraw, ImageOps


quotefont = ImageFont.truetype("Arial.ttf", 50)


def add_border(input_img):
    """Gives the image a nice white border which is bigger at the bottom and smaller in all other sides. (To configure the border size, change the left, top, right and bottom variables in this function.)
    
    Arguments:
        input_img {PIL image} -- The image you want to add a border to.
    
    Returns:
        PIL image -- The edited image with the border.
    """
    left = 50
    top = left
    right = left
    bottom = 300
    border = (left, top, right, bottom)
    bimg = ImageOps.expand(input_img, border=border, fill='White')
    return bimg


def cropit(im):
    width, height = im.size
    right = width
    left = 0  # will span the entire length of the image
    top = 300
    bottom = height - top
    im1 = im.crop((left, top, right, bottom))
    return im1


def drawTextWithOutline(text, x, y, font, img):
    draw = ImageDraw.Draw(img)
    # draw.text((x-2, y-2), text,(0,0,0),font=font)
    # draw.text((x+2, y-2), text,(0,0,0),font=font)
    # draw.text((x+2, y+2), text,(0,0,0),font=font)
    # draw.text((x-2, y+2), text,(0,0,0),font=font)
    draw.text((x, y), text, (0, 0, 0), font=font)
    return


def drawText(text, img):
    # text = text.upper()
    draw = ImageDraw.Draw(img)
    # measure the size the text will take
    w, h = draw.textsize(text, quotefont)

    lineCount = 1
    if w > img.width:
        lineCount = int(round((w / img.width) + 1))

    print("lineCount: {}".format(lineCount))

    lines = []
    if lineCount > 1:

        lastCut = 0
        isLast = False
        for i in range(0, lineCount):
            if lastCut == 0:
                cut = (len(text) / lineCount) * i
            else:
                cut = lastCut

            if i < lineCount-1:
                nextCut = round((len(text) / lineCount) * (i+1))
            else:
                nextCut = len(text)
                isLast = True

            # nextCut = int(nextCut)

            print("cut: {} -> {}".format(cut, nextCut))

            # make sure we don't cut words in half
            if nextCut == len(text) or text[nextCut] == " ":
                print("may cut")
            else:
                print("may not cut")
                while text[nextCut] != " ":
                    nextCut += 1
                print("new cut: {}".format(nextCut))

            line = text[int(cut):int(nextCut)].strip()

            # is line still fitting ?
            w, h = draw.textsize(line, quotefont)
            if not isLast and w > img.width:
                print("overshot")
                nextCut -= 1
                # text[50]
                while text[nextCut] != " ":
                    nextCut -= 1
                print("new cut: {}".format(nextCut))

            lastCut = nextCut
            lines.append(text[int(cut):int(nextCut)].strip())

    else:
        lines.append(text)

    print(lines)

    lastY = -h
    # if pos == "bottom":
    lastY = img.height - h * (lineCount+1) - 60

    for i in range(0, lineCount):
        w, h = draw.textsize(lines[i], quotefont)
        x = img.width/2 - w/2
        y = lastY + h
        # x = 1000
        # y = 1000
        lastY = y
        drawTextWithOutline(lines[i], x, y, quotefont, img)


def drawTitle(name, img):
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(name, ImageFont.truetype(
        "SFNSDisplayCondensed-Semibold.otf", 60))
    drawTextWithOutline(name, img.width/2 - w/2, img.height-260,
                        ImageFont.truetype("/Supplemental/Futura.ttc", 60), img)
