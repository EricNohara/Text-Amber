import os
import random
from config import *

all_imgs = list()

def choose_rand_img(directory="."):
    for img in os.listdir(directory):
        ext = img.split(".")[len(img.split(".")) - 1]
        if (ext in IMG_EXTENSION):
            all_imgs.append(img)
    choice = random.randint(0, len(all_imgs) - 1)
    chosenImage = all_imgs[choice]
    return chosenImage