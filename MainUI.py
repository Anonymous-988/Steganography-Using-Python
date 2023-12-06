import tkinter as tk
from tkinter import font

from EmbedMessageUI import EmbedMessageUI
from ExtractMessageUI import ExtractMessageUI

from EmbedImageUI import EmbedImageUI
from ExtractImageUI import ExtractImageUI

"""
MainApp class is used to initialize the root tkinter app.
This is not meant to inherit by subclasses.
"""
class MainApp:
    """
    Class constructor to initialize app elements
    """
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Steganography Application")
        self.root.geometry('400x500')

        # Container for Title
        self.initTitleContainer()

        # Container for buttons
        self.initButtonContainer()

        # Container for frames
        self.initFrameContainer()

        self.root.mainloop()



    """
    Function to initialize App Title and description elements
    """
    def initTitleContainer(self):
        titleContainer = tk.LabelFrame(self.root, bd=2, relief=tk.SOLID)
        titleContainer.pack()

        titleLabel = tk.Label(titleContainer, text= "Steganography App", font = font.Font(family="arial",size= 22, underline= True))
        titleLabel.pack(padx=50)

        messageStr1 = "Explore hidden secrets within images. \nConceal messages securely with our Steganography app!"
        messageLabel1 =  tk.Label(titleContainer, text= messageStr1, font = font.Font(family="arial",size= 8))
        messageLabel1.pack(pady = (20,5))



    """
    Function to initialize Buttons to navigate between App frames
    """
    def initButtonContainer(self):
        button_container = tk.Frame(self.root)
        button_container.pack(pady=10)

        # Buttons to switch between frames
        button1 = tk.Button(button_container, text="Message", font= font.Font(family="arial",size= 15), command=lambda: self.switchFrames(self.messageFrame, [self.imageFrame, self.audioFrame]))
        button1.pack(side=tk.LEFT, padx=10)
        button2 = tk.Button(button_container, text="Image", font= font.Font(family="arial",size= 15), command=lambda: self.switchFrames(self.imageFrame, [self.messageFrame, self.audioFrame]))
        button2.pack(side=tk.LEFT, padx=10)
        button3 = tk.Button(button_container, text="Audio", font= font.Font(family="arial",size= 15), command=lambda: self.switchFrames(self.audioFrame, [self.messageFrame, self.imageFrame]))
        button3.pack(side=tk.LEFT, padx=10)



    """
    Function to initialize frames to implement App logic
    """
    def initFrameContainer(self):
        frame_container = tk.Frame(self.root)
        frame_container.pack(fill=tk.BOTH)

        # Initialize Message Frame
        self.messageFrame = self.initMessageFrame(frame_container)
        self.messageFrame.pack(fill=tk.BOTH, expand=True)

        # Initialize Image Frame
        self.imageFrame = self.initImageFrame(frame_container)
        self.imageFrame.pack_forget()  # Hide frame initially

        # Initialize Audio Frame
        self.audioFrame = self.initAudioFrame(frame_container)
        self.audioFrame.pack_forget()  # Hide frame initially


    def initMessageFrame(self, container):
        frame = tk.Frame(container, height=300, width=200, bd=2, relief=tk.SUNKEN)
        titleLable = tk.Label(frame, text="Message Embedding", font= font.Font(family="arial",size= 15, underline=True))
        titleLable.pack(pady=20)

        descriptionStr = """LGB Image Steganography is a technique that conceals 
        data within the least significant bits (LSBs) of the red, green, and 
        blue channels of an image. This method alters the LSBs of pixel values, 
        allowing for hidden message to be embedded without significantly 
        altering the image's visual appearance. It uses the RGB channels' least 
        significant bits to store additional data, enabling covert communication 
        or data hiding within image files. Use Below buttons to implement the same."""
        despLabel = tk.Label(frame, text=descriptionStr, font= font.Font(family="arial",size= 8))
        despLabel.pack(padx=(0, 20))

        embedButton = tk.Button(frame, text= "Embed Message", font= font.Font(family="arial",size= 15), bg="blue", fg="white", command= lambda: self.callEmbedMessageUI())
        embedButton.pack(pady=20)

        extractButton = tk.Button(frame, text= "Extract Message", font= font.Font(family="arial",size= 15), bg="red", fg="white", command= lambda: self.callExtractMessageUI())
        extractButton.pack(pady=(0,20))

        return frame
    
    def initImageFrame(self, container):
        frame = tk.Frame(container, height=300, width=200, bd=2, relief=tk.SUNKEN)
        titleLable = tk.Label(frame, text="Image Embedding", font= font.Font(family="arial",size= 15, underline=True))
        titleLable.pack(pady=20)

        # TODO: Need to update proper description for the Image Frame
        descriptionStr = """LGB Image Steganography is a technique that conceals 
        data within the least significant bits (LSBs) of the red, green, and 
        blue channels of an image. This method alters the LSBs of pixel values, 
        allowing for hidden message to be embedded without significantly 
        altering the image's visual appearance. It uses the RGB channels' least 
        significant bits to store additional data, enabling covert communication 
        or data hiding within image files. Use Below buttons to implement the same."""
        despLabel = tk.Label(frame, text=descriptionStr, font= font.Font(family="arial",size= 8))
        despLabel.pack(padx=(0, 20))

        embedButton = tk.Button(frame, text= "Embed Image", font= font.Font(family="arial",size= 15), bg="blue", fg="white", command= lambda: self.callEmbedImageUI())
        embedButton.pack(pady=20)

        extractButton = tk.Button(frame, text= "Extract Image", font= font.Font(family="arial",size= 15), bg="red", fg="white", command= lambda: self.callExtractImageUI())
        extractButton.pack(pady=(0,20))

        return frame
    
    # TODO: Need to implement Valid Audio Frame Currently just a template
    def initAudioFrame(self, container):
        frame = tk.Frame(container, height=300, width=200, bd=2, relief=tk.SUNKEN)
        titleLable = tk.Label(frame, text="Audio Embedding", font= font.Font(family="arial",size= 15, underline=True))
        titleLable.pack(pady=20)

        descriptionStr = """Still Under Development
        Work in Progress !!!!"""
        despLabel = tk.Label(frame, text=descriptionStr, font= font.Font(family="arial",size= 8))
        despLabel.pack(padx=(0, 20))

        embedButton = tk.Button(frame, text= "Embed Message", font= font.Font(family="arial",size= 15), bg="blue", fg="white", command= lambda: self.callEmbedImageUI())
        embedButton.pack(pady=20)

        extractButton = tk.Button(frame, text= "Extract Message", font= font.Font(family="arial",size= 15), bg="red", fg="white", command= lambda: self.callExtractImageUI())
        extractButton.pack(pady=(0,20))

        return frame


    """
    Function to switch frames
    """
    def switchFrames(self, frame, frameList):
        for obj in frameList:
            obj.pack_forget()
        frame.pack(fill=tk.BOTH, expand=True)

    def callEmbedMessageUI(self):
        embedMessageApp = EmbedMessageUI(self.root)

    def callExtractMessageUI(self):
        extractMessageApp = ExtractMessageUI(self.root)

    def callEmbedImageUI(self):
        embedImageApp = EmbedImageUI(self.root)

    def callExtractImageUI(self):
        extractImageApp = ExtractImageUI(self.root)