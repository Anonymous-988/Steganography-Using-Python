import tkinter as tk
from tkinter import filedialog
from StegoHandler import ImageLSBSteganography

class ExtractImageUI:
    def __init__(self, root) -> None:
        self.extractImageApp = tk.Toplevel(root)
        self.extractImageApp.title("Image Extracting Tile")

        #initialize Image SteganoHandler Object
        imageStegano = ImageLSBSteganography()

        #Variable list
        steganoImagePath = tk.StringVar()
        extractedSecretImagePath = tk.StringVar()

        steganoImageLabel = tk.Label(self.extractImageApp, text="Select a Stegano image:")
        steganoImageLabel.pack()

        steganoImageButton = tk.Button(self.extractImageApp, text="Browse", command=lambda: steganoImagePath.set(filedialog.askopenfilename()))
        steganoImageButton.pack()

        # Create a button to hide the message in the cover image
        extractButton = tk.Button(self.extractImageApp, text="Extract Image", command=lambda: imageStegano.extractImage(steganoImagePath.get(), extractedSecretImagePath))
        extractButton.pack()

        extractedMessage = tk.Entry(self.extractImageApp, textvariable=extractedSecretImagePath.get(), state='readonly')
        extractedMessage.pack()

        # Exit button
        exit_button = tk.Button(self.extractImageApp, text="Exit", command=self.extractImageApp.withdraw)
        exit_button.pack()
