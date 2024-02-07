from mms import send_mms_by_email
from config import *
from get_img import choose_rand_img
from check_network import detect_internet_connection

def main():
    """Do send the message to Amber with a randomly chosen image."""
    message = "Good morning Amber! I love you sosososo much <3 I hope you have a great day! Heres a cute (or spicy) pic of us to start off your day :)"

    rand_img = choose_rand_img(IMG_DIR)
    print("Sending... ", rand_img, "\n", message)

    img_file_path = f"imgs/{rand_img}"

    send_mms_by_email(number, message, img_file_path, mime_maintype, mime_subtype, provider, sender_credentials)

if __name__ == "__main__":
    detect_internet_connection()
    main()