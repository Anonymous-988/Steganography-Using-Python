import tkinter as tk
from tkinter import filedialog
from StegoHandler import ImageLSBSteganography

class ExtractMessageUI:
    def __init__(self, root) -> None:
        self.extractMessageApp = tk.Toplevel(root)
        self.extractMessageApp.title("Message Extracting Tile")

        #initialize Image SteganoHandler Object
        imageStegano = ImageLSBSteganography()

        #Variable list
        steganoImagePath = tk.StringVar()
        secretMessage = tk.StringVar()

        steganoImageLabel = tk.Label(self.extractMessageApp, text="Select a Stegano image:")
        steganoImageLabel.pack()

        steganoImageButton = tk.Button(self.extractMessageApp, text="Browse", command=lambda: steganoImagePath.set(filedialog.askopenfilename()))
        steganoImageButton.pack()

        # Create a button to hide the message in the cover image
        hideButton = tk.Button(self.extractMessageApp, text="Extract Message", command=lambda: imageStegano.extractMessage(steganoImagePath.get(), secretMessage))
        hideButton.pack()

        extractedMessage = tk.Entry(self.extractMessageApp, textvariable=secretMessage, state='readonly')
        extractedMessage.pack()

        # Exit button
        exit_button = tk.Button(self.extractMessageApp, text="Exit", command=self.extractMessageApp.withdraw)
        exit_button.pack()







"""
# TODO: Need to clear the below content stored for temporary access
"""
# extractMessageApp = tk.Tk()
# extractMessageApp.title("Steganography Application")

# #initialize Image SteganoHandler Object
# imageStegano = ImageLSBSteganography()

# #Variable list
# steganoImagePath = tk.StringVar()
# secretMessage = tk.StringVar()

# steganoImageLabel = tk.Label(extractMessageApp, text="Select a Stegano image:")
# steganoImageLabel.pack()

# steganoImageButton = tk.Button(extractMessageApp, text="Browse", command=lambda: steganoImagePath.set(filedialog.askopenfilename()))
# steganoImageButton.pack()

# # Create a button to hide the message in the cover image
# hideButton = tk.Button(extractMessageApp, text="Extract Message", command=lambda: imageStegano.extractMessage(steganoImagePath.get(), secretMessage))
# hideButton.pack()

# extractedMessage = tk.Entry(extractMessageApp, textvariable=secretMessage, state='readonly')
# extractedMessage.pack()

# # Exit button
# exit_button = tk.Button(extractMessageApp, text="Exit", command=extractMessageApp.withdraw)
# exit_button.pack()

# Start the main event loop
# extractMessageApp.mainloop()