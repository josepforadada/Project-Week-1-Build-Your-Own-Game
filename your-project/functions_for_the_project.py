from tkinter import filedialog          # this is a module to can open dialogues.
from PIL import Image                   # this is a module for image manipulation.
options = ["e", "E", "d", "D"]


class what_to_do:

    def ask_user_encrypt_or_decrypt():

        times = 0
        user_answer = input("What you want to do, encrypt or decrypt? (E or D): ")

        if user_answer in options:
            message = input("Type message: ")
            return (user_answer, message, "1")

        elif user_answer not in options:
            while times <= 2:
                user_answer = input("\nPlease, what you want to do, encrypt or decrypt? (%d times remaining, E or D): " % (3-times))
                times += 1
                if user_answer in options:
                    message = input("Type message: ")
                    return (user_answer, message, "1")
            return ("0", "0", "0")

        message = input("Type message: ")
        return (user_answer, message, "1")


    def ask_for_the_picture():

        path = filedialog.askopenfilename(filetypes = (("jpeg files","*.jpg"),("all files","*.*"))) # select a file from the library and return the path.
        return path

    def image_to_values(path):

        img = Image.open(path)                              # to work with the image, first is necessary to open it (basically is loaded)
        img_RGB = img.convert('RGB')                        # to use a color picker have to be sure to transform image to color profile to RGB
        pixel_mosaic_size = 4                               # change this value to modify the complexity of the mosaic
        imgSmall = img_RGB.resize((pixel_mosaic_size,pixel_mosaic_size),resample=Image.BILINEAR)   # transform image to 16*16 pixels

        list_of_tuples_of_pixels = []
        list_of_sum_of_RGB_values = []
        for pixelsV in range(pixel_mosaic_size):            # loop through vertical pixels
            for pixelsH in range(pixel_mosaic_size):        # loop through vertical pixels

                list_of_tuples_of_pixels.append(imgSmall.getpixel((pixelsV, pixelsH)))

        for RGB_tuple in list_of_tuples_of_pixels:
            list_of_sum_of_RGB_values.append(sum(RGB_tuple))

        return list_of_sum_of_RGB_values

    def encrypt_or_decrypt(image_passed,):

        return
    def decrypt(message):
        return
    def show_conversion():
        print("else")
        return

