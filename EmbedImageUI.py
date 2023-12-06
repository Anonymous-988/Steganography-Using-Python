import tkinter as tk
from tkinter import filedialog
from StegoHandler import ImageLSBSteganography

class EmbedImageUI:
    def __init__(self, root) -> None:
        self.embedImageApp = tk.Toplevel(root)
        self.embedImageApp.title("Image Embedding Tile")

        #initialize Image SteganoHandler Object
        imageStegano = ImageLSBSteganography()

        #Variable list
        cover_image_path = tk.StringVar()
        secret_image_path = tk.StringVar()
        stegano_image_path = tk.StringVar()

        coverImageLabel = tk.Label(self.embedImageApp, text="Select a cover image:")
        coverImageLabel.pack()

        coverImageButton = tk.Button(self.embedImageApp, text="Browse", command=lambda: cover_image_path.set(filedialog.askopenfilename()))
        coverImageButton.pack()

        # Create a label for the secret message
        messageLabel = tk.Label(self.embedImageApp, text="Select a secret image:")
        messageLabel.pack()

        secretImageButton = tk.Button(self.embedImageApp, text="Browse", command=lambda: secret_image_path.set(filedialog.askopenfilename()))
        secretImageButton.pack()

        # Create a button to hide the message in the cover image
        hideButton = tk.Button(self.embedImageApp, text="Hide Image", command=lambda: imageStegano.embedImage(cover_image_path.get(), secret_image_path.get(), stegano_image_path))
        hideButton.pack()

        # Exit button
        exit_button = tk.Button(self.embedImageApp, text="Exit", command=self.embedImageApp.withdraw)
        exit_button.pack()