from PIL import Image,ImageDraw,ImageFont
import random
#from auto_fest import get_fest
import importlib




def superimpose(path,name):
    print("Generating text")
    module = importlib.import_module('text', package=None)
    image=Image.open(path)
    w,h=image.size
    var=random.randint(0, 11)
    draw=ImageDraw.Draw(image)

    text=module.fest[name][var-2][0][0]
   
    text1=module.fest[name][var-2][1][0]
    text2=module.fest[name][var-2][2][0]
    text3=module.fest[name][var-2][3][0]

    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 20)

    t_w,t_h=draw.textsize(text,font)
    t_w1,t_h1=draw.textsize(text1,font)
    t_w2,t_h2=draw.textsize(text2,font)
    t_w3,t_h3=draw.textsize(text3,font)

    margin=20

    x=w-t_w-margin
    y=h-t_h-margin
    w, h = draw.textsize(text)
    #draw.text(((w-t_w)/2,(h-t_h)/2), text, fill="black")
    draw.text((150,210),text,(255,255,255),font=font)
    draw.text((150+(t_w-t_w1)/2,240),text1,(255,255,255),font=font)
    draw.text((150+(t_w1-t_w2)/2,270),text2,(255,255,255),font=font)
    draw.text((150+(t_w2-t_w3)/2,300),text3,(255,255,255),font=font)
    #draw.text([(x,y)],text,font)

    image.save("./card.jpg")
