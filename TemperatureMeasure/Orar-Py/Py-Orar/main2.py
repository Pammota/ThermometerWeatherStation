import sys
import datetime
from daysofweek import *
import time
import inkyphat


def uniHour(date):

  weekday = date.strftime('%A')
  day = date.strftime('%d')
  month = date.strftime('%B')
  year = date.strftime('%Y')
  hour = date.strftime('%H')



  with open('class.txt', 'w') as file:
    try:
      inkyphat.set_rotation(180)
      inkyphat.set_colour("red")
      inkyphat.set_border(inkyphat.WHITE)

      from PIL import Image, ImageFont, ImageDraw

      font = ImageFont.truetype(inkyphat.fonts.AmaticSCBold,25)

      message = str(dow[weekday][hour])

      w, h = font.getsize(message)
      x = ((inkyphat.WIDTH-w)/ 2)- 35 
      y = ((inkyphat.HEIGHT) / 2.1)  

      img = Image.open("/home/pi/Desktop/Py-Orar/image1.png")
      inkyphat.set_image(img)

      draw = ImageDraw.Draw(img)    

      draw.text((x, y), message, inkyphat.WHITE, font)
      inkyphat.set_image(img)
      inkyphat.show()
 
      #file.write(dow[weekday][hour])
    except KeyError as e:
      inkyphat.set_rotation(180)
      inkyphat.set_colour("red")
      inkyphat.set_border(inkyphat.WHITE)

      from PIL import Image, ImageFont, ImageDraw

      font = ImageFont.truetype(inkyphat.fonts.AmaticSCBold,25)

      message = "Free"

      w, h = font.getsize(message)
      x = ((inkyphat.WIDTH-w)/ 2)- 35 
      y = ((inkyphat.HEIGHT) / 2.1)  

      img = Image.open("/home/pi/Desktop/Py-Orar/image1.png")
      inkyphat.set_image(img)

      draw = ImageDraw.Draw(img)    

      draw.text((x, y), message, inkyphat.WHITE, font)
      inkyphat.set_image(img)
      inkyphat.show()
      



while True:
  x  = datetime.datetime.now()
  uniHour(x)
  time.sleep(900)