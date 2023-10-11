## For trial and error purposes

import os
import cv2
import sys
import math
import numpy as np
import itertools
from PIL import Image

class LSB():
    #encoding part :
    def encode_image(self,img, msg):
        length = len(msg)
        if length > 255:
            print("text too long! (don't exeed 255 characters)")
            return False
        encoded = img.copy()
        width, height = img.size
        index = 0
        for row in range(height):
            for col in range(width):
                if img.mode != 'RGB':
                    r, g, b ,a = img.getpixel((col, row))
                elif img.mode == 'RGB':
                    r, g, b = img.getpixel((col, row))
                # first value is length of msg
                if row == 0 and col == 0 and index < length:
                    asc = length
                elif index <= length:
                    c = msg[index -1]
                    asc = ord(c)
                else:
                    asc = b
                encoded.putpixel((col, row), (r, g , asc))
                index += 1
        return encoded

    #decoding part :
    def decode_image(self,img):
        width, height = img.size
        msg = ""
        index = 0
        for row in range(height):
            for col in range(width):
                if img.mode != 'RGB':
                    r, g, b ,a = img.getpixel((col, row))
                elif img.mode == 'RGB':
                    r, g, b = img.getpixel((col, row))  
                # first pixel r value is length of message
                if row == 0 and col == 0:
                    length = b
                elif index <= length:
                    msg += chr(b)
                index += 1
        lsb_decoded_image_file = "lsb_" + Input_file
        #img.save(lsb_decoded_image_file)
        ##print("Decoded image was saved!")
        print(msg)
        return msg
    

Input_file = "./Input/input3.png"
lsb_img = Image.open(Input_file)
print()
msg = "My Name is Sumant"
msg_len = len(msg)
#print(msg_len)
if msg_len > 255:
    print("Message should not be more than 255 characters ")
    sys.exit()

# print(lsb_img.getpixel((0,0)))

encoded = lsb_img.copy()
width, height = lsb_img.size

r,g,b,a = 0,0,0,0
if lsb_img.mode != 'RGB':
    r, g, b ,a = lsb_img.getpixel((width-1, height-1))
elif lsb_img.mode == 'RGB':
    r, g, b = lsb_img.getpixel((width-1, height-1))
lsb_img.putpixel((width-1, height-1), (r,g,msg_len))
print(lsb_img.getpixel((width-1, height-1)))
msg_index = 0

for row in range(height):
    for col in range(width):

        if lsb_img.mode != 'RGB':
            r, g, b ,a = lsb_img.getpixel((col, row))
        elif lsb_img.mode == 'RGB':
            r, g, b = lsb_img.getpixel((col, row))
        if msg_index < msg_len:
            c = msg[msg_index]
            asc = ord(c)
            # print(asc)
        else:
            break
        encoded.putpixel((col, row), (r, g , asc))
        msg_index += 1



encoded.save("./Output/input3.png")

decode_file = "./Output/input3.png"
decode_img = Image.open(decode_file)
org_msg = ""
r, g, b = decode_img.getpixel((width-1, height-1))
org_msg_len = b
print(decode_img.getpixel((width-1, height-1)))
print(org_msg_len)
msg_index = 0
width, height = decode_img.size

for row in range(height):
    for col in range(width):
        if msg_index < org_msg_len:
            r, g, b = decode_img.getpixel((col, row))
            # print(b)
            org_msg += chr(b)
        else:
            break
        msg_index +=1

print(len(org_msg))

