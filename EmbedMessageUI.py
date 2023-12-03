import tkinter as tk
from tkinter import filedialog
from StegoHandler import ImageLSBSteganography

class EmbedMessageUI:
    def __init__(self, root) -> None:
        self.embedMessageApp = tk.Toplevel(root)
        self.embedMessageApp.title("Message Embedding Tile")

        #initialize Image SteganoHandler Object
        imageStegano = ImageLSBSteganography()

        #Variable list
        cover_image_path_var = tk.StringVar()
        secret_message_var = tk.StringVar()

        coverImageLabel = tk.Label(self.embedMessageApp, text="Select a cover image:")
        coverImageLabel.pack()

        coverImageButton = tk.Button(self.embedMessageApp, text="Browse", command=lambda: cover_image_path_var.set(filedialog.askopenfilename()))
        coverImageButton.pack()

        # Create a label for the secret message
        messageLabel = tk.Label(self.embedMessageApp, text="Enter the secret message:")
        messageLabel.pack()

        # Create an entry widget for the secret message
        messageEntry = tk.Entry(self.embedMessageApp, textvariable=secret_message_var)
        messageEntry.pack()

        # Create a button to hide the message in the cover image
        hideButton = tk.Button(self.embedMessageApp, text="Hide Message", command=lambda: imageStegano.embedMessage(cover_image_path_var.get(), secret_message_var.get()))
        hideButton.pack()

        # Exit button
        exit_button = tk.Button(self.embedMessageApp, text="Exit", command=self.embedMessageApp.withdraw)
        exit_button.pack()







"""
# TODO: Need to clear this belwo content stored for temporary
"""
# embedMessageApp = tk.Tk()
# embedMessageApp.title("Embed Message Tile")

# #initialize Image SteganoHandler Object
# imageStegano = ImageLSBSteganography()

# #Variable list
# cover_image_path_var = tk.StringVar()
# secret_message_var = tk.StringVar()

# coverImageLabel = tk.Label(embedMessageApp, text="Select a cover image:")
# coverImageLabel.pack()

# coverImageButton = tk.Button(embedMessageApp, text="Browse", command=lambda: cover_image_path_var.set(filedialog.askopenfilename()))
# coverImageButton.pack()

# # Create a label for the secret message
# messageLabel = tk.Label(embedMessageApp, text="Enter the secret message:")
# messageLabel.pack()

# # Create an entry widget for the secret message
# messageEntry = tk.Entry(embedMessageApp, textvariable=secret_message_var)
# messageEntry.pack()

# # Create a button to hide the message in the cover image
# hideButton = tk.Button(embedMessageApp, text="Hide Message", command=lambda: imageStegano.embedMessage(cover_image_path_var.get(), secret_message_var.get()))
# hideButton.pack()

# # Exit button
# exit_button = tk.Button(embedMessageApp, text="Exit", command=embedMessageApp.withdraw)
# exit_button.pack()


# Start the main event loop
# embedMessageApp.mainloop()
