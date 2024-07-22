import qrcode
import re
from PIL import Image
import webcolors as wbc

def validate_url(url):
    # Basic URL validation
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def is_valid_color(color_name):
    try:
        wbc.name_to_rgb(color_name)
        return True
    except ValueError:
        return False
def front_color_input():
    while True:
        front_color = input("Please enter a color for the front of the QR code (Recommended: 'black'): ").strip().lower()
        if is_valid_color(front_color):
            return front_color
        else:
            print("Invalid color. Please enter a valid color name.")

def back_color_input():
    while True:
        back_color = input("Please enter a color for the back of the QR code (Recommended: 'white'): ").strip().lower()
        if is_valid_color(back_color):
            return back_color
        else: 
            print("Invalid color. Please enter a valid color name.")

def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
                    version = 1, 
                    error_correction = qrcode.constants.ERROR_CORRECT_H, 
                    box_size = 10, 
                    border = 2
                )
    
    if validate_url(url):
        qr.add_data(url)
        qr.make(fit = True)
        color1 = front_color_input()
        color2 = back_color_input()
        img = qr.make_image(fill_color = color1, back_color = color2 )
        filename = filename + '.png'
        img.save(filename)
        print(f"QR code saved as {filename}")
        return 1
    else:
        print("Invalid URL. Please enter a valid URL.")
        return 0
    
def evaluate_new_user_response():
    user_input = ""
    while True:
        user_input = input("Do you wish to generate a new qr code? (y/n): ").strip().lower()

        if user_input == 'y':
            return True
        elif user_input == 'n':
            print("Goodbye!")
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def qr_code_creator():
    run = True
    while run:
        link_input = input("Please enter your link: ")
        filename = input("Please enter name of qrcode you wish to name it: ")
        result = generate_qr_code(link_input, filename)

        if result == 1:
            run = evaluate_new_user_response()
        else:
            print("Please try again with a valid URL.")

if __name__ == "__main__":
    qr_code_creator()