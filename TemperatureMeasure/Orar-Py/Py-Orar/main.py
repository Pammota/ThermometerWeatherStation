import sys
import datetime
from daysofweek import *
import time
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw

inkyphat = InkyPHAT("red")
inkyphat.set_border(inkyphat.WHITE)

font = ImageFont.truetype(inkyphat.fonts.AmaticSCBold, 22)

def uniHour(date):

  weekday = date.strftime('%A')
  day = date.strftime('%d')
  month = date.strftime('%B')
  year = date.strftime('%Y')
  hour = date.strftime('%H')

  
  try: 
    message = dow[weekday][hour]

    w, h = font.getsize(message)
    x = (inkyphat.WIDTH / 2) - (w / 2)
    y = (inkyphat.HEIGHT / 2) - (h / 2)

    img = Image.open("/home/pi/Desktop/Py-Orar/image1.png")
    inkyphat.set_image(img)

    draw = ImageDraw.Draw(img)

    draw.text((x, y), message, inkyphat.RED, font)
    inkyphat.set_image(img)
    inkyphat.show()
    
  except KeyError:
    message = "Free"

    w, h = font.getsize(message)
    x = (inkyphat.WIDTH / 2) - (w / 2)
    y = (inkyphat.HEIGHT / 2) - (h / 2)

    img = Image.open("/home/pi/Desktop/Py-Orar/image1.png")
    inkyphat.set_image(img)

    draw = ImageDraw.Draw(img)

    draw.text((x, y), message, inkyphat.RED, font)
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
  uniHour(x)
  print(f"Process still running, {ct} times and counting.")
  if ct%4==0:
    screenclr(2,"red")
  time.sleep(900)