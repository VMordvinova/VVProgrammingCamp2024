from PIL import Image
import os
import qr_code_generator

def combine_images(link: str, qr_code_file, plain_card_file, new_card_file):

    qr_code_generator.create_qrcode(link, qr_code_file)

    img_back = Image.open(plain_card_file)
    img_front = Image.open(qr_code_file)

    new_image = Image.new('RGBA', img_back.size)
    new_image.paste(img_back, (0,0))


    scale = 0.5 #can be any number bigger than ZERO. usually 0.5.


    size = img_front.size[1]/img_front.size[0]
    width= img_back.size[0]*scale
    height = width * size

    img_front = img_front.resize((int(width), int(height))) 
    img_front_position = (int((img_back.size[0]/2 - img_front.size[0]/2)), int((img_back.size[1]/2 - img_front.size[1]/2))) #center image
    new_image.paste(img_front, img_front_position) 
    new_image.save(new_card_file) 
    new_image.show() 

link = "https://mytr-koops.itch.io/"  #link from the internet

img_front = "birdy.png"  #SAVED image from the code folder

img_back = "VirtualFront.png" #SAVED image of the card

img_make = "FrontBirdCard.png"  #NEW image that will be created

combine_images(link, img_front, img_back, img_make) 
