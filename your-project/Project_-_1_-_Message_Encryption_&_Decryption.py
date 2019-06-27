'''

PROJECT - 1 - Message Encryption & Decryption

1. Title and program description
2. Prompt for encryption or decryption
3. Prompt the user for the message he wants to envrypt / decrypt
4. Prompt the user for the picture used to encrypt (GUI prompt)
5. Save variables for message and path
6. Square crop, pixelate (max mosaic 64x64) and save the picture.
7. Get values for each pixel in the image and convert it to list
8. Sum The RGB values to get a number
9. Iterate each letter of the message by index, depending with the relative pixel index
10. Create a string again and print the message encrypted /decrypred

FUNCTIONS:

def ask_user_encrypt_or_decrypt:
def ask_for_the picture:
def image_to_values()
def encrypt:
def decrypt:

'''

from functions_for_the_project import what_to_do                                # import all functions needed

user_answer, message = what_to_do.ask_user_encrypt_or_decrypt()                 # ask user messsage

user_picture = what_to_do.ask_for_the_picture()                                 # ask user image hash

image_hash_generator = what_to_do.image_to_values()                             # convert image to a list

if user_answer is Encrypt:

    CONVERSION = what_to_do.encrypt(CONVERSION)                                 # encrypt message
else:
    CONVERSION = what_to_do.decrypt(CONVERSION)                                 # decrypt

what_to_do.show_conversion()                                                    # show result
