import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from StegoHandler import ImageLSBSteganography

class ExtractImageUI:
    def __init__(self, root) -> None:
        self.extractImageApp = tk.Toplevel(root)
        self.extractImageApp.title("Image Extracting Tile")
        self.extractImageApp.geometry("300x350+400+0")

        #initialize Image SteganoHandler Object
        imageStegano = ImageLSBSteganography()

        #Variable list
        steganoImagePath = tk.StringVar()
        extractedSecretImagePath = tk.StringVar()

        # Stego Image Container
        steganoImageContainer = tk.Frame(self.extractImageApp)
        steganoImageLabel = tk.Label(steganoImageContainer, text="Select a Stegano image:", font=('Arial', 12))
        steganoImageLabel.pack(side=tk.LEFT)

        steganoImageButton = tk.Button(steganoImageContainer, text="Browse", font=('Arial', 10), fg= "white", bg= "#0000AA", command=lambda: self.loadCoverImage(steganoImagePath, steganoCanvas))
        steganoImageButton.pack()
        steganoImageContainer.pack(pady=(0, 5))

        # Stegano Image Canvas
        steganoCanvas = tk.Canvas(self.extractImageApp, width = 200, height = 100, bd=1, relief=tk.SUNKEN)
        steganoCanvas.pack()

        # Create a button to hide the message in the cover image
        extractButton = tk.Button(self.extractImageApp, text="Extract Image", font=('Arial', 10), fg= "white", bg= "#0000AA", command=lambda: self.getExtractedImage(imageStegano, steganoImagePath, extractedSecretImagePath, extractedImageCanvas))
        extractButton.pack(pady=10)

        # Extracted Image Canvas
        extractedImageCanvas = tk.Canvas(self.extractImageApp, width = 200, height = 100, bd=1, relief=tk.SUNKEN)
        extractedImageCanvas.pack()

        # Exit button
        exit_button = tk.Button(self.extractImageApp, text="Exit", font=('Arial', 10), fg="white", bg="red", command=self.extractImageApp.withdraw)
        exit_button.pack(pady=20)

    def getExtractedImage(self, imageStegano, steganoImagePath, extractedSecretImagePath, canvas):
        imageStegano.extractImage(steganoImagePath.get(), extractedSecretImagePath)
        img = Image.open(extractedSecretImagePath.get())
        img = img.resize((200, 100))
        img = ImageTk.PhotoImage(img)
        canvasItem = canvas.create_image(0,0, anchor=tk.NW, image=img)
        # canvas.itemconfig(canvasItem, image=img)
        self.extractImageApp.mainloop()
    
    def loadCoverImage(self, imagePath, canvas):
        imagePath.set(filedialog.askopenfilename())
        img = Image.open(imagePath.get())
        img = img.resize((200, 100))
        img = ImageTk.PhotoImage(img)
        canvasItem = canvas.create_image(0,0, anchor=tk.NW, image=img)
        # canvas.itemconfig(canvasItem, image=img)
        self.extractImageApp.mainloop()
