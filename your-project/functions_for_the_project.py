from tkinter import filedialog as fd        # this is a module to can open dialogues.
from PIL import Image                   # this is a module for image manipulation.
import math
options = ["e", "E", "d", "D"]
ascii_unicode = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïð'
#ascii_unicode = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
call_letter = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J"}
call_number = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9}
pixel_mosaic_size = 40

class what_to_do:

    def ask_user_encrypt_or_decrypt():

        times = 0
        user_answer = input("\nWhat you want to do, encrypt or decrypt? (E or D): ")

        if user_answer in options:
            message = input("\n\tType message: ")
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

        path = fd.askopenfilename(filetypes = (("jpeg files","*.jpg"),("all files","*.*"))) # select a file from the library and return the path.
        return path

    def image_to_values(path):

        img = Image.open(path)                              # to work with the image, first is necessary to open it (basically is loaded)
        img_RGB = img.convert('RGB')                        # to use a color picker have to be sure to transform image to color profile to RGB
                               # change this value to modify the complexity of the mosaic
        imgSmall = img_RGB.resize((pixel_mosaic_size,pixel_mosaic_size),resample=Image.BILINEAR)   # transform image to 16*16 pixels

        list_of_tuples_of_pixels = []
        list_of_sum_of_RGB_values = []
        for pixelsV in range(pixel_mosaic_size):            # loop through vertical pixels
            for pixelsH in range(pixel_mosaic_size):        # loop through vertical pixels

                list_of_tuples_of_pixels.append(imgSmall.getpixel((pixelsV, pixelsH)))

        for RGB_tuple in list_of_tuples_of_pixels:
            list_of_sum_of_RGB_values.append(sum(RGB_tuple))

        return list_of_sum_of_RGB_values

    def encrypt_or_decrypt(messsage_passed, hash_of_pixels,val):
        list_unicode = (list(ascii_unicode))
        #print(len(list_unicode))
        message = (list(messsage_passed))
        #print(hash_of_pixels)
        #(print(message))
        len_hash = len(hash_of_pixels)
        value_added = []
        message_list = []
        loop = 0

        print(hash_of_pixels)
        if val == "E" or val == "e":
            for caracters in message:

                val = list_unicode.index(caracters)
                pixel_val = hash_of_pixels[message.index(caracters)]
                num_val_color = val + pixel_val


                turns = math.floor(num_val_color / len(ascii_unicode))
                position = num_val_color % len(ascii_unicode)
                caracter_final =  list_unicode[position]


                message_list.append(caracter_final + call_letter.get(turns))

        else:
            for caracters in message:
                if (message.index(caracters) % 2) == 0 or message.index(caracters) == 0:

                    var = (message.index(caracters) + 1)
                    var_str = str(message[var])
                    val1 = call_number.get(var_str)
                    print("val1 - " + str(val1))
                    val2 = ascii_unicode.index(caracters)
                    print("val2 - " + str(val2))
                    count = 0

                    hash_division = hash_of_pixels[message.index(caracters)]

                    print("hash division " + str(hash_division))
                    len_ascii = (len(ascii_unicode)*int(val1) + int(val2))-(hash_of_pixels[message.index(caracters)])

                    print(ascii_unicode[int(len_ascii)])

        return message_list

    def show_final_message(final_message):

        print("\n"+"".join(final_message))
        return

