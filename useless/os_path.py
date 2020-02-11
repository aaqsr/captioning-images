import os
p = "/Users/apple/Documents/pyth image work/images"

quotes = {
    'a':'AAAAAAAAAA THIS IS A I THINK AAAAAAA SOME OTHER THINGS AWKDLAKWDAWLKJ DWKLADJWKLA SOS SOAWDAWDAWD AWDAWDWDDWA',
    'b':'Hello world this is b',
    'c': 'OH YES THIS BE C SAJWALKDJAWLKDJAWLKDJAWKLDJAWDK'
}

if os.path.exists(p) and os.path.isdir(p):
    for name in os.listdir(p):
        if name != '.DS_Store':
            print(name)
            filename = name.replace('.jpg', '')
            print(quotes[filename])
            # fullname = p + '/' + name
            # im = Image.open(fullname)
            # namez = name[:-4]
            # d = ImageDraw.Draw(im)
            # f = ImageFont.truetype("OpenSans-Regular.ttf", 30)
            # d.text((4,0), namez, font=f, fill=(255,255,255,255))
            # im.save(fullname)
            # im.show()
            # print(name)
            # print(fullname)
            # print(namez)
else:
    print("Directory not found")