# Handler Module used to perform Image or Audio Steganography

import numpy as np
from PIL import Image
import datetime
import wave

# Class used tp perform various image LSB Steganography
class ImageLSBSteganography:
    def __init__(self) -> None:
        self.outputFilePath = "./Output/Image/"

    # Function used to Embed Secret Image within an another image
    def embedImage(self, coverImagePath, secretImagePath, fileLabel):
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
                    if cover_array[i, j, channel] != secret_array[i, j, channel]:
                        stego_array[i, j, channel] = (cover_array[i, j, channel] & 0xFE) | (secret_array[i, j, channel] >> 7)

        # Convert the stego array to an image and save it
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"ImageStegano_{timestamp}.png"
        filepath = f"{self.outputFilePath}{filename}"
        stego_image = Image.fromarray(stego_array)
        stego_image.save(filepath)
        fileLabel.set(filepath)
        print(f"Secret Image embedded within the Cover Image: {filename}")

    # Function used to extract Secret Image within an another image
    def extractImage(self, steganoImagePath, fileLabel):
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
                    secret_array[i, j, channel] = secret_bit * 155  # Multiply by 255 to convert 0/1 to 0/255. Used to adjust intensity

        # Convert the secret NumPy array back to an image
        secret_image = Image.fromarray(secret_array.astype(np.uint8))

        # Save the extracted secret image
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"ExtractedImage_{timestamp}.png"
        filepath = f"{self.outputFilePath}{filename}"
        secret_image.save(filepath)
        fileLabel.set(filepath)
        print(f"Secret Image extracted from Stegano Image: {filename}")


    # Function used to embed Secret Message within an image
    def embedMessage(self, coverImagePath, secretMessage, imageLabel):
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
        filename = f"MessageStegano_{timestamp}.png"
        filepath = f"{self.outputFilePath}{filename}"
        stego_image.save(f"{filepath}")
        imageLabel.set(filepath)
        print(f"Secret message embedded in Image: {filename}")

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


class AudioLSBSteganography:
    def __init__(self) -> None:
        self.outputFilePath = "./Output/Audio/"

    def embedMessage(self, coverAudioPath, secretMessage, fileLabel):
        # Open the audio file
        audio = wave.open(coverAudioPath, mode='rb')

        # Read audio frames and convert the secret message to binary
        frames = audio.readframes(audio.getnframes())
        secretMessage = ''.join(format(ord(char), '08b') for char in secretMessage)
        messageLength = len(secretMessage)
        if messageLength > 255:
            raise Exception("Message Length should not be greater 255")
        # Embed secret message in the least significant bit of audio frames
        frames_modified = bytearray(frames)

        frames_modified[-1] = messageLength

        for i in range(messageLength):
            frames_modified[i] = (frames_modified[i] & 254) | int(secretMessage[i])

        # Save the stego image
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"AudioStegano_{timestamp}.wav"
        filepath = f"{self.outputFilePath}{filename}"

        # Create a new wave file to save the modified frames
        audio_steg = wave.open(filepath, 'wb')
        audio_steg.setparams(audio.getparams())
        audio_steg.writeframes(frames_modified)

        # Close the files
        audio.close()
        audio_steg.close()
        resMessage = f"Secret message embedded in Audio: {filename}"
        print(resMessage)
        fileLabel.set(filepath)

    
    def extractMessage(self, stegoAudioPath, messageLabel):
        audio = wave.open(stegoAudioPath, mode='rb')
        frames = audio.readframes(audio.getnframes())

        messageLength = frames[-1]

        extracted_message = ""
        for bit in frames[:messageLength]:
            extracted_message += str(bit & 1)
        
        # Convert the binary message back to text
        extracted_text = ''.join(chr(int(extracted_message[i:i+8], 2)) for i in range(0, len(extracted_message), 8))

        audio.close()
        resMessage = f"Extracted message from Audio: {extracted_text}"
        print(resMessage)
        messageLabel.set(extracted_text)


if __name__ == "__main__":
    print("-- Testing Stegano Handler Moduler --")

    ImageStegObj = ImageLSBSteganography()
    ImageStegObj.extractMessage("./Output/MessageStegano_20231002223200.png")