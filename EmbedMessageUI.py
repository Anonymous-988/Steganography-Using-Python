import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from StegoHandler import ImageLSBSteganography

class EmbedMessageUI:
    def __init__(self, root) -> None:
        self.embedMessageApp = tk.Toplevel(root)
        self.embedMessageApp.title("Message Embedding Tile")
        self.embedMessageApp.geometry("350x300+400+0")

        #initialize Image SteganoHandler Object
        imageStegano = ImageLSBSteganography()

        #Variable list
        cover_image_path_var = tk.StringVar()
        secret_message_var = tk.StringVar()
        stegano_image_path_var = tk.StringVar()

        # Cover Image Container
        coverImageContainer = tk.Frame(self.embedMessageApp)

        coverImageLabel = tk.Label(coverImageContainer, text="Select a cover image:", font=('Arial', 12))
        coverImageLabel.pack(side=tk.LEFT)

        coverImageButton = tk.Button(coverImageContainer, text="Browse", font=('Arial', 10), fg= "white", bg= "#0000AA", command=lambda: self.loadCoverImage(cover_image_path_var, coverImageCanvas))
        coverImageButton.pack(side=tk.LEFT)

        coverImageContainer.pack()


        #Cover Image Canvas
        coverImageCanvas = tk.Canvas(self.embedMessageApp, width = 200, height = 100, bd=1, relief=tk.SUNKEN)
        coverImageCanvas.pack()

        # Message Container
        secretMessageContainer = tk.Frame(self.embedMessageApp)

        # Create a label for the secret message
        messageLabel = tk.Label(secretMessageContainer, text="Enter the secret message:", font=('Arial', 12))
        messageLabel.pack(side=tk.LEFT)

        # Create an entry widget for the secret message
        messageEntry = tk.Entry(secretMessageContainer, textvariable=secret_message_var)
        messageEntry.pack()

        secretMessageContainer.pack(pady=5)

        # Create a button to hide the message in the cover image
        hideButton = tk.Button(self.embedMessageApp, text="Hide Message", font=('Arial', 10), fg= "white", bg= "#0000AA", command=lambda: imageStegano.embedMessage(cover_image_path_var.get(), secret_message_var.get(), stegano_image_path_var))
        hideButton.pack()

        # Label for Result
        resultLabel = tk.Label(self.embedMessageApp, textvariable=stegano_image_path_var, font=('Arial', 8), fg="green")
        resultLabel.pack()

        # Exit button
        exit_button = tk.Button(self.embedMessageApp, text="Exit", font=('Arial', 10), fg="white", bg="red", command=self.embedMessageApp.withdraw)
        exit_button.pack(pady=10)    

    def loadCoverImage(self, imagePath, canvas):
        imagePath.set(filedialog.askopenfilename())
        img = Image.open(imagePath.get())
        img = img.resize((200, 100))
        img = ImageTk.PhotoImage(img)
        canvas.create_image(0,0, anchor=tk.NW, image=img)
        self.embedMessageApp.mainloop()