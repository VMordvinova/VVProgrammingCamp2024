import qrcode #pip install qrcode
import os

def create_qrcode(link: str, filename: str):
    if(os.path.exists(filename) == False):
        print("Creating a New File!")
        
        features = qrcode.QRCode(version=1, box_size = 40, border = 3)
        features.add_data('')
        features.make(fit=True)

        generate_image = qrcode.make(link)
        generate_image.save(filename)
        return True
    else:
        print("File Already Exists...")
        return False
    
create_qrcode("https://carleton.ca/vv/summercamps/", "QR1.png")