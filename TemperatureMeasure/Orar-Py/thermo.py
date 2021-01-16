import sys
import datetime
import time
import inkyphat
from bmp180 import bmp180
import keyboard	
from PIL import Image, ImageFont, ImageDraw

bpm = bmp180 import bmp180

inkyphat.set_colour("red")
inkyphat.set_border(inkyphat.WHITE)
inkyphat.set_rotation(180)
font = ImageFont.truetype(inkyphat.fonts.AmaticSCBold, 16)

def thermometer():
    weekday = date.strftime('%A')
    day = date.strftime('%d')
    month = date.strftime('%B')
    year = date.strftime('%Y')
    hour = date.strftime('%H')

    temp = str(bmp.get_temp())
    press = str(bmp.get_pressure())
    alt = str(bmp.get_altitude())

    message = f("Today is {weekday} \nTemperature: {temp} \nPressure: {press} \n Altitude:{alt}")

    w, h = font.getsize(message)
    x = (inkyphat.WIDTH / 2) - 95
    y = (inkyphat.HEIGHT / 2.1)

    img = Image.open("/home/pi/Desktop/Py-Orar/image1.png")
    inkyphat.set_image(img)

    draw = ImageDraw.Draw(img)

    draw.text((x, y), message, inkyphat.WHITE, font)
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
  uniHour(x)
  if ct == 1:
    print(f"Process still running, {ct} time and counting.")
  else:
    print(f"Process still running, {ct} times and counting.")
  time.sleep(900)
