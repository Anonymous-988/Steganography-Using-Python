# Handler Module used to perform Image or Audio Steganography

import numpy as np
from PIL import Image
import datetime

# Class used tp perform various image LSB Steganography
class ImageLSBSteganography:
    # Function used to Embed Secret Image within an another image
    def embedImage(self, coverImagePath, secretImagePath):
        # Load the cover image
        cover_image = Image.open(coverImagePath)
        cover_array = np.array(cover_image)

        # Load the secret image
        secret_image = Image.open(secretImagePath)
        secret_array = np.array(secret_image)

        # Ensure both images have the same dimensions
        if cover_array.shape != secret_array.shape:
            raise ValueError("Cover and secret images must have the same dimensions.")

        # Embed the secret image into the cover image
        stego_array = np.copy(cover_array)  # Create a copy of the cover image
        for i in range(cover_array.shape[0]):
            for j in range(cover_array.shape[1]):
                for channel in range(3):  # Iterate over RGB channels
                    stego_array[i, j, channel] = (cover_array[i, j, channel] & 0xFE) | (secret_array[i, j, channel] >> 7)

        # Convert the stego array to an image and save it
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        stego_image = Image.fromarray(stego_array)
        stego_image.save(f'./Output/stego_image_{timestamp}.png')
        print(f"Secret Image embedded within the Cover Image: stego_image_{timestamp}.png")

    # Function used to extract Secret Image within an another image
    def extractImage(self, steganoImagePath):
        # Load the stego image
        stego_image = Image.open(steganoImagePath)

        # Convert the stego image to a NumPy array
        stego_array = np.array(stego_image)

        # Create an empty NumPy array to store the extracted secret image
        secret_array = np.zeros_like(stego_array)

        # Iterate through each pixel in the stego image and extract the LSB
        for i in range(stego_array.shape[0]):
            for j in range(stego_array.shape[1]):
                for channel in range(3):  # Iterate over RGB channels
                    # Extract the LSB by bitwise AND with 1
                    secret_bit = stego_array[i, j, channel] & 1
                    # Set the corresponding bit in the secret image
                    secret_array[i, j, channel] = secret_bit * 155  # Multiply by 255 to convert 0/1 to 0/255

        # Convert the secret NumPy array back to an image
        secret_image = Image.fromarray(secret_array.astype(np.uint8))

        # Save the extracted secret image
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        secret_image.save(f'./Output/extracted_secret_image_{timestamp}.png')
        print(f"Secret Image extracted from cover Image: extracted_secret_image_{timestamp}.png")


    # Function used to embed Secret Message within an image
    def embedMessage(self, coverImagePath, secretMessage):
        # Open the cover image
        cover_image = Image.open(coverImagePath)
        cover_array = np.array(cover_image)

        # Ensure the secret message can fit within the image
        max_message_length = (cover_array.shape[0] * cover_array.shape[1] * 3) // 8
        if len(secretMessage) > max_message_length:
            raise ValueError("Secret message is too long to embed in the image.")

        # Convert the secret message to binary
        secretMessageLength = len(secretMessage)
        binary_secret_message = ''.join(format(ord(char), '08b') for char in secretMessage)

        # Create an empty NumPy array for the stego image
        stego_array = np.copy(cover_array)

        # Save message length in last Pixel Channel
        stego_array[-1, -1, -1] = secretMessageLength

        # Embed the secret message into the LSBs of the cover image
        message_index = 0
        for i in range(cover_array.shape[0]):
            for j in range(cover_array.shape[1]):
                for channel in range(3):  # Iterate over RGB channels
                    if message_index < len(binary_secret_message):
                        stego_array[i, j, channel] = (cover_array[i, j, channel] & 0xFE) | int(binary_secret_message[message_index])
                        message_index += 1

        # Convert the stego NumPy array back to an image
        stego_image = Image.fromarray(stego_array.astype(np.uint8))

        # Save the stego image
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        stego_image.save(f"./Output/MessageStegano_{timestamp}.png")
        print(f"Secret message embedded in Image: MessageStegano_{timestamp}.png")

    # Function used to extract Secret Message within an image
    def extractMessage(self, steganoImagePath, messageLabel):
        # Open the stego image
        stego_image = Image.open(steganoImagePath)
        stego_array = np.array(stego_image)

        # Extract the secret message from the LSBs of the stego image
        secretMessageLength = stego_array[-1,-1,-1] * 8

        # Iterating over color channels to discover extract message bits from LSB of each pixel
        binary_secret_message = ""
        messageIndex = 0
        for i in range(stego_array.shape[0]):
            for j in range(stego_array.shape[1]):
                for channel in range(3):  # Iterate over RGB channels
                    if(messageIndex >= secretMessageLength):
                        break
                    binary_secret_message += str(stego_array[i, j, channel] & 1)
                    messageIndex += 1

        # Convert the binary secret message back to a string
        secretMessage = ''.join(chr(int(binary_secret_message[i:i+8], 2)) for i in range(0, len(binary_secret_message), 8))
        print(f"Hidden secret message was {secretMessage}")
        messageLabel.set(secretMessage)


if __name__ == "__main__":
    print("-- Testing Stegano Handler Moduler --")
    # Tried Implementing Image2Image LSB Steganography
    # ImageStegObj = ImageLSBSteganography()
    # ImageStegObj.embedImage("./Input/input2.jpg", "./Input/input4.jpg")
    # ImageStegObj.extractImage("./Output/stego_image_20231002215312.png")

    ImageStegObj = ImageLSBSteganography()
    # ImageStegObj.embedMessage("./Input/input2.jpg", "Hasta La Vista, Baby!!")
    ImageStegObj.extractMessage("./Output/MessageStegano_20231002223200.png")