import tkinter as tk
from tkinter import filedialog
from StegoHandler import AudioLSBSteganography

class ExtractAudioUI:
    def __init__(self, root) -> None:
        self.extractAudioApp = tk.Toplevel(root)
        self.extractAudioApp.title("Audio Extracting Tile")
        self.extractAudioApp.geometry("270x230+400+0")

        #initialize Image SteganoHandler Object
        audioStegano = AudioLSBSteganography()

        #Variable list
        steganoAudioPath = tk.StringVar()
        secretMessage = tk.StringVar()

        # Stego Image Container
        stegoImageContainer = tk.Frame(self.extractAudioApp)
        steganoImageLabel = tk.Label(stegoImageContainer, text="Select a Stegano Audio:", font=('Arial', 12))
        steganoImageLabel.pack(side=tk.LEFT)

        steganoImageButton = tk.Button(stegoImageContainer, text="Browse", font=('Arial', 10), fg= "white", bg= "#0000AA", command=lambda: steganoAudioPath.set(filedialog.askopenfilename()))
        steganoImageButton.pack()
        stegoImageContainer.pack(pady=30)

        # Create a button to hide the message in the cover image
        extractButton = tk.Button(self.extractAudioApp, text="Extract Message", font=('Arial', 10), fg= "white", bg= "#0000AA", command=lambda: audioStegano.extractMessage(steganoAudioPath.get(), secretMessage))
        extractButton.pack(pady=10)

        # extractedMessage = tk.Entry(self.extractAudioApp, textvariable=secretMessage, state='readonly')
        # extractedMessage.pack()

        # Message Container
        messageContainer = tk.Frame(self.extractAudioApp)
        resultMessage = tk.Label(messageContainer, text="Hidden Message: ", font=('Arial', 10),  fg="Black")
        resultMessage.pack(side=tk.LEFT, padx=5)

        extractedMessage = tk.Label(messageContainer, textvariable=secretMessage, font=('Arial', 8),  fg="green")
        extractedMessage.pack()

        messageContainer.pack(pady=(0,10))

        # Exit button
        exit_button = tk.Button(self.extractAudioApp, text="Exit", font=('Arial', 10), fg="white", bg="red", command=self.extractAudioApp.withdraw)
        exit_button.pack(pady=(20,0))