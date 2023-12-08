import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from StegoHandler import ImageLSBSteganography

class EmbedImageUI:
    def __init__(self, root) -> None:
        self.embedImageApp = tk.Toplevel(root)
        self.embedImageApp.title("Image Embedding Tile")
        self.embedImageApp.geometry("300x400+400+0")

        #initialize Image SteganoHandler Object
        imageStegano = ImageLSBSteganography()

        #Variable list
        cover_image_path = tk.StringVar()
        secret_image_path = tk.StringVar()
        stegano_image_path = tk.StringVar()

        # Cover Image Container 
        coverImageContainer = tk.Frame(self.embedImageApp)
        coverImageLabel = tk.Label(coverImageContainer, text="Select a cover image:", font=('Arial', 12))
        coverImageLabel.pack(side=tk.LEFT)

        coverImageButton = tk.Button(coverImageContainer, text="Browse", font=('Arial', 10), fg= "white", bg= "#0000AA", command=lambda: self.loadCoverImage(cover_image_path, coverImageCanvas))
        coverImageButton.pack()
        coverImageContainer.pack(pady=(0,5))

        # Cover Image Canvas
        coverImageCanvas = tk.Canvas(self.embedImageApp, width = 200, height = 100, bd=1, relief=tk.SUNKEN)
        coverImageCanvas.pack()

        # Stego Image Container
        stegoImageContainer = tk.Frame(self.embedImageApp)
        stegoLabel = tk.Label(stegoImageContainer, text="Select a secret image:", font=('Arial', 12))
        stegoLabel.pack(side=tk.LEFT)

        secretImageButton = tk.Button(stegoImageContainer, text="Browse", font=('Arial', 10), fg= "white", bg= "#0000AA", command=lambda: self.loadCoverImage(secret_image_path, stegoImageCanvas))
        secretImageButton.pack()
        stegoImageContainer.pack(pady=5)

        # Stego Image Canvas
        stegoImageCanvas = tk.Canvas(self.embedImageApp, width = 200, height = 100, bd=1, relief=tk.SUNKEN)
        stegoImageCanvas.pack()

        # Create a button to hide the message in the cover image
        hideButton = tk.Button(self.embedImageApp, text="Hide Image", font=('Arial', 10), fg= "white", bg= "#0000AA", command=lambda: imageStegano.embedImage(cover_image_path.get(), secret_image_path.get(), stegano_image_path))
        hideButton.pack(pady=(10,0))

        # Label for Result
        resultLabel = tk.Label(self.embedImageApp, textvariable=stegano_image_path, font=('Arial', 8), fg="green")
        resultLabel.pack()

        # Exit button
        exit_button = tk.Button(self.embedImageApp, text="Exit", font=('Arial', 10), fg="white", bg="red", command=self.embedImageApp.withdraw)
        exit_button.pack(pady=10)

    def loadCoverImage(self, imagePath, canvas):
        imagePath.set(filedialog.askopenfilename())
        img = Image.open(imagePath.get())
        img = img.resize((200, 100))
        img = ImageTk.PhotoImage(img)
        canvasItem = canvas.create_image(0,0, anchor=tk.NW, image=img)
        # canvas.itemconfig(canvasItem, image=img)
        self.embedImageApp.mainloop()