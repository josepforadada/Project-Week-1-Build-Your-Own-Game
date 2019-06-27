from tkinter import filedialog          # this is a module to can open dialogues.
from PIL import Image                   # this is a module for image manipulation.

class what_to_do:

    def ask_user_encrypt_or_decrypt():


        user_answer = input("What you want to do, encrypt or decrypt? (E or D): ")
        print(type(user_answer))
        if str = user_answer:
        message = input("Type message: ")
        return user_answer, message

    def ask_for_the_picture():

        path = filedialog.askopenfilename(filetypes = (("jpeg files","*.jpg"),("all files","*.*"))) # select a file from the library and return the path.
        return path

    def image_to_values(path):

        img = Image.open(path)          # to work with the image, first is necessary to open it (basically is loaded)
        img_RGB = img.convert('RGB')    # to use a color picker have to be sure to transform image to color profile to RGB
        imgSmall = img_RGB.resize((20,20),resample=Image.BILINEAR)   # transform image to 16*16 pixels
        print(imgSmall.getpixel((0, 0)))    # to get the value in a RGB tuple (R,G,B)

        return

    def encrypt(message):
        return
    def decrypt(message):
        return
    def show_conversion():
        print("else")
        return

