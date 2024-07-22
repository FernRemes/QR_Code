import qrcode as qr
import re
import sys

def validate_url(url):
    # Basic URL validation
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def generate_qr_code(url, filename):
    if validate_url(url):
        img = qr.make(url)
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


        if user_input != 'y' and user_input != 'n' and len(user_input) > 1:
            print("Invalid input. Please enter y or n.")

        elif user_input.lower() == 'y':
            return True
        else:
            print("Goodbye!")
            return False

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
