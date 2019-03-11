
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:25:45 2019

@author: Brett
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def img_to_ascii(**kwargs):
    """ 
    The ascii character set we use to replace pixels. 
    The grayscale pixel values are 0-255.
    0 - 25 = '#' (darkest character)
    250-255 = '.' (lightest character)
    """
   
    """
    the Font name i chose is K26ToyBlocks123
    
    """
    
    
  
    width = kwargs.get('width',200)
    path = kwargs.get('path',None)

    im = Image.open(path)

    im = resize(im,width)

    w,h = im.size

    print(w,h)

    #im = im.convert("L") # convert to grayscale



    
    # Open a new image using 'RGBA' (a colored image with alpha channel for transparency)
    #              color_type      (w,h)     (r,g,b,a) 
    #                   \           /            /
    #                    \         /            /
    newImg = Image.new('RGBA', (w*30,h*30), (255,255,255,255))
    # Open a TTF file and specify the font size
    fnt = ImageFont.truetype('K26ToyBlocks123.ttf', 30)

    # get a drawing context for your new image
    drawOnMe = ImageDraw.Draw(newImg)
    nx = 30
    ny=30

    for x in range (w):
        for y in range (h):
           p = im.getpixel((x,y))
           # draw font on new image at some x,y thats shifted based on font size
           #x = new_x and new y, ch = my character to write, and p = a color tuple from orignal image 
           #ch= ascii_chars[p//25]
           
           drawOnMe.text((ny,nx), 'W' , font=fnt, fill=p)
           nx+=30
           if y == h-1:
               ny += 30
               nx=30
           

    ## You would loop through your old image and write on the newImg with the 
    ## lines of code below:
    # add a character to some xy 
    #         location   character  ttf-font   color-tuple
    #            \         /        /            /
    #             \       /        /            /
   
    
    # Display your new image with all the stuff `drawOnMe` placed on it
    newImg.show()
    
    # Save the image.
    newImg.save('DestinyBlocks.png')   #where it saves the output.


    

def resize(img,width):
    """
    This resizes the img while maintining aspect ratio. Keep in 
    mind that not all images scale to ascii perfectly because of the
    large discrepancy between line height line width (characters are 
    closer together horizontally then vertically)
    """
    
    wpercent = float(width / float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((width ,hsize), Image.ANTIALIAS)

    return img


if __name__=='__main__':
    path = 'Destiny1.jpg'    #where it reads in the input.
    #path = '/Users/griffin/Dropbox/Scripts-random/image_projects/AsciiArt/original_images/superman.jpg'
    #path = '/Users/griffin/Dropbox/Scripts-random/image_projects/AsciiArt/original_images/vans-logo.png'
    Ascii = img_to_ascii(path=path,width=200)
