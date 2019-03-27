# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:56:59 2019

@author: Brett
"""

import os,sys
import json
import requests
import glob
from bs4 import BeautifulSoup
from pprint import pprint


def saveImage(url,src,out_folder):
        url = os.path.join(url,src)
        #this creates a path to hold your emojis
        page = requests.get(url)
        #this gets your emojis

        parts = src.split('/')
        name = os.path.join(out_folder,parts[-1])
        #this makes a folder named whatever value out_folder is
        with open(name, 'wb') as f:
            f.write(page.content)
            #saves the emoji into the new file

url = "https://www.webfx.com/tools/emoji-cheat-sheet/"



page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Use beatiful soup to read the page
# then loop through the page with the following


for emoji in soup.find_all("span",{"class":"emoji"}):
    image_path = emoji['data-src']
    print(url+image_path)
    saveImage(url,image_path,"emojilist")
    
    # save the image using requests library
    
