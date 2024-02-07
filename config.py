from datetime import date

# number = "3149396381"   # Replace with your phone number.
number = "6363179533"
provider = "AT&T"       # Replace with correct phone provider, match with keys in dictionary provided in providers.py file.
sender_credentials = ("eric.noharaleclair@gmail.com", "ujct wmrm kbjl pgun")       # Replace with your sender credentials.("email", "password")

# SENDING MMS
mime_maintype = "image"     # Replace with correct mime maintype of downloaded media.
mime_subtype = "jpg"        # Replace with correct mime subtype of downloaded media.
message = "Good morning Amber! I love you sosososo much <3 I hope you have a great day! Heres a cute (or spicy) pic of us to start off your day :)"

# get_img vars
IMG_DIR = r"C:\Users\Eric\Desktop\_project_starter_\Text Amber\imgs"
IMG_EXTENSION = "jpg"

SLEEP_TIME = 5