import json
import requests
from PIL import Image, ImageFont, ImageDraw, ImageOps
import textwrap

from requests.api import head

def getHistory(username):
    Font = ImageFont.truetype('font.ttf', 70)
    mode = 'RGB'
    color = (54, 57, 62)

    resp = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
    uuid = resp.json()["id"]

    print(username+f"'s UUID ist {uuid}")

    #get head
    head = Image.open(requests.get("https://crafatar.com/avatars/"+uuid, stream=True).raw)


    resp = requests.get(f"https://api.mojang.com/user/profiles/{uuid}/names")
    name = json.loads(resp.text)
    names = []
    for x in range(len(name)):
        names.append((name[x])['name'])

    #names.reverse()

    #Blue Line
    size = (10, len(names)*128+128)
    line = Image.new(mode, size, (44, 238, 239))
    
    print(names)
    size = (1024, len(names)*128+128)
    im = Image.new(mode, size, color)
    I1 = ImageDraw.Draw(im)
    for x in range(len(names)):
        I1.text((28, x*101+150), str(x + 1)+" "+names[x],font=Font, fill=(255, 255, 255))


    head = head.resize((256, 256), resample=4, box=None)
    im.paste(head, (768-22, 25))
    im.paste(line, (0, 0))
    nrc = Image.open("nrc.PNG")
    im.paste(nrc, (30, len(names)*128+45))
    

    im.save("result.png")
    head.save("head2.png")
    filename = 'result.png'
    return im
