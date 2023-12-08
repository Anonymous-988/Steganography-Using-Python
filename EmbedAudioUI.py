import tkinter as tk
from tkinter import filedialog
from StegoHandler import AudioLSBSteganography

class EmbedAudioUI:
    def __init__(self, root) -> None:
        self.embedAudioApp = tk.Toplevel(root)
        self.embedAudioApp.title("Audio Embedding Tile")
        self.embedAudioApp.geometry("270x220+400+0")

        #initialize Image SteganoHandler Object
        audioStegano = AudioLSBSteganography()

        #Variable list
        cover_audio_path = tk.StringVar()
        secret_message_var = tk.StringVar()
        result_message = tk.StringVar()

        # Cover Audio Container
        coverAudioContainer = tk.Frame(self.embedAudioApp)
        coverAudioLabel = tk.Label(coverAudioContainer, text="Select a cover Audio:", font=('Arial', 12))
        coverAudioLabel.pack(side=tk.LEFT)

        coverAudioButton = tk.Button(coverAudioContainer, text="Browse", font=('Arial', 10), fg= "white", bg= "#0000AA", command=lambda: cover_audio_path.set(filedialog.askopenfilename()))
        coverAudioButton.pack()
        coverAudioContainer.pack(pady=(10,20))

        # Create a label for the secret message
        messageLabel = tk.Label(self.embedAudioApp, text="Enter the secret message:", font=('Arial', 12))
        messageLabel.pack()

        # Create an entry widget for the secret message
        messageEntry = tk.Entry(self.embedAudioApp, width= 34, textvariable=secret_message_var)
        messageEntry.pack()

        # Create a button to hide the message in the cover image
        hideButton = tk.Button(self.embedAudioApp, text="Hide Message", font=('Arial', 10), fg= "white", bg= "#0000AA", command=lambda: audioStegano.embedMessage(cover_audio_path.get(), secret_message_var.get(), result_message))
        hideButton.pack(pady=(20,0))

        # Label for Result
        resultLabel = tk.Label(self.embedAudioApp, textvariable=result_message, font=('Arial', 8), fg="green")
        resultLabel.pack()

        # Exit button
        exit_button = tk.Button(self.embedAudioApp, text="Exit", font=('Arial', 10), fg="white", bg="red", command=self.embedAudioApp.withdraw)
        exit_button.pack(pady=10)

    # def updateEmbedMessage(self, audioPath):