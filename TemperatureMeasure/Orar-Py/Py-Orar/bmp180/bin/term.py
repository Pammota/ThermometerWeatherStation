import sys
import datetime
import time
import inkyphat
import keyboard	
from PIL import Image, ImageFont, ImageDraw


inkyphat.set_colour("red")
inkyphat.set_border(inkyphat.RED)
inkyphat.set_rotation(180)
font = ImageFont.truetype(inkyphat.fonts.AmaticSCBold, 20)

def writerr(text):
    f = open("mistakes.txt","a")
    f.write(text)
    f.write('\n')
    f.close()

def readerr(filer):
    f= open(filer,"r")
    txt=f.read(5)
    f.close()
    return txt

def reader2(filer):
    f=open(filer,"r")
    txt = f.read(7)
    f.close()
    return float(txt)

def weather():
    f = open("vreme.txt","r")
    txt = f.read()
    f.close()
    return txt

weather_imager ={
    "insorit":"pimoroni_sun.png",
    "partial noros":"pimoroni_cloudsun.png",
    "ninsoare":"pimoroni_snow.png",
    "ninsoare usoara":"pimoroni_snow.png",
    "averse izolate":"pimoroni_rain.png",
    "cer acoperit complet":"pimoroni_cloud.png",
    "ploaie":"pimoroni_rain.png",
    "ploaie usoara":"pimoroni_rain.png",
    "noapte cu aer cetos":"pimoroni_cloudsun.png",
    "lapovita":"pimoroni_snow.png",
    "lapovita usoara":"pimoroni_snow.png",
    "ceata":"pimoroni_cloudsun.png",
    "ploaie puternica":"pimoroni_rain.png",
    "ceata izolat":"pimoroni_cloudsun.png",
    "furtuna":"pimoroni_thunder.png",
    "senin":"pimoroni_sun.png",
    "cer acoperit":"pimoroni_cloud.png"
}


def thermometer(date):
    weekday = date.strftime('%A')
    day = date.strftime('%d')
    month = date.strftime('%B')
    year = date.strftime('%Y')
    hour = date.strftime('%H')

    temp = f"{readerr('temp.txt')} 'C "
    press = f"{round(reader2('press.txt')/100,2)} Pa"
    alt = f"{round(reader2('alt.txt')*1000,2)} m"

    message = f"Temperature: {temp} \nPressure: {press} \n Altitude:{alt}"
    message2 = weekday

    w, h = font.getsize(message2)
    x = (inkyphat.WIDTH / 2) - 95
    y = (inkyphat.HEIGHT / 2.1) - 22
    x2 = (inkyphat.WIDTH/2)-(w/2)
    y2 = (inkyphat.HEIGHT/2) - 55  


    try:
        img = Image.open(weather_imager[weather()])
        inkyphat.set_image(img)
    except KeyError as error:
        img = Image.open("pimoroni.png")
        writerr(weather())

    draw = ImageDraw.Draw(img)

    draw.text((x, y), message, inkyphat.WHITE, font)
    draw.text((x2,y2),message2,inkyphat.WHITE,font)
    inkyphat.set_image(img)
    inkyphat.show()

def screenclr(cycles,colour):

  inkyphat.set_colour(colour)

  colours = (inkyphat.RED, inkyphat.BLACK, inkyphat.WHITE)
  colour_names= (colour, "black", "white")

  for i in range(cycles):
    print("Cleaning cycle %i\n" % (i + 1))
    for j, c in enumerate(colours):
        print("- updating with %s" % colour_names[j])
        inkyphat.set_border(c)
        for x in range(inkyphat.WIDTH):
            for y in range(inkyphat.HEIGHT):
                inkyphat.putpixel((x, y), c)
        inkyphat.show()
        time.sleep(1)
    print("\n")
  print("Cleaning complete!")

ct = 0
while True:
  ct+=1
  x  = datetime.datetime.now()
  if ct%5==0:
    screenclr(1,"red")
  thermometer(x)
  if ct == 1:
    print(f"Process still running, {ct} time and counting.")
  else:
    print(f"Process still running, {ct} times and counting.")
  time.sleep(900)
