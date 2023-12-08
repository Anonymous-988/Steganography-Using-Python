import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from StegoHandler import ImageLSBSteganography

class ExtractMessageUI:
    def __init__(self, root) -> None:
        self.extractMessageApp = tk.Toplevel(root)
        self.extractMessageApp.title("Message Extracting Tile")
        self.extractMessageApp.geometry("300x250+400+0")

        #initialize Image SteganoHandler Object
        imageStegano = ImageLSBSteganography()

        #Variable list
        steganoImagePath = tk.StringVar()
        secretMessage = tk.StringVar()

        #Stegano Image Container
        steganoImageContainer = tk.Frame(self.extractMessageApp)

        steganoImageLabel = tk.Label(steganoImageContainer, text="Select a Stegano image:", font=('Arial', 12))
        steganoImageLabel.pack(side=tk.LEFT)

        steganoImageButton = tk.Button(steganoImageContainer, text="Browse", font=('Arial', 10), fg= "white", bg= "#0000AA", command=lambda: self.loadCoverImage(steganoImagePath, steganoCanvas))
        steganoImageButton.pack()

        steganoImageContainer.pack()

        #Cover Image Canvas
        steganoCanvas = tk.Canvas(self.extractMessageApp, width = 200, height = 100, bd=1, relief=tk.SUNKEN)
        steganoCanvas.pack()

        # Create a button to hide the message in the cover image
        extractButton = tk.Button(self.extractMessageApp, text="Extract Message", font=('Arial', 10), fg= "white", bg= "#0000AA", command=lambda: imageStegano.extractMessage(steganoImagePath.get(), secretMessage))
        extractButton.pack()

        # Message Container
        messageContainer = tk.Frame(self.extractMessageApp)
        resultMessage = tk.Label(messageContainer, text="Hidden Message: ", font=('Arial', 10),  fg="Black")
        resultMessage.pack(side=tk.LEFT, padx=5)

        extractedMessage = tk.Label(messageContainer, textvariable=secretMessage, font=('Arial', 8),  fg="green")
        extractedMessage.pack()

        messageContainer.pack(pady=10)

        # Exit button
        exit_button = tk.Button(self.extractMessageApp, text="Exit", font=('Arial', 10), fg="white", bg="red", command=self.extractMessageApp.withdraw)
        exit_button.pack()

    def loadCoverImage(self, imagePath, canvas):
        imagePath.set(filedialog.askopenfilename())
        img = Image.open(imagePath.get())
        img = img.resize((200, 100))
        img = ImageTk.PhotoImage(img)
        canvas.create_image(0,0, anchor=tk.NW, image=img)
        self.extractMessageApp.mainloop()







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