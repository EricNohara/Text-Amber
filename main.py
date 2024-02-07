from mms import send_mms_by_email
from config import *
from get_img import choose_rand_img
from check_network import detect_internet_connection
from time import sleep

def main():
    """Do send the message to Amber with a randomly chosen image."""
    sleep(SLEEP_TIME)

    rand_img = choose_rand_img(IMG_DIR)
    print("Sending... ", rand_img, "\n", message)
    img_file_path = f"imgs/{rand_img}"

    send_mms_by_email(number, message, img_file_path, mime_maintype, mime_subtype, provider, sender_credentials)

if __name__ == "__main__":
    """Wait for internect connection, then execute code."""
    detect_internet_connection()
    main()