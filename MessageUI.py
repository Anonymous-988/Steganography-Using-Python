import tkinter as tk

class EmbedMessageApp:
    def __init__(self, master):
        self.master = master
        self.embed_window = tk.Toplevel(master)
        self.embed_window.title("Embed Message")

        self.embed_button = tk.Button(self.embed_window, text="Embed", command=self.embed_message)
        self.embed_button.pack()

        self.exitBtn = tk.Button(self.embed_window, text="Exit", command=self.embed_window.destroy)
        self.exitBtn.pack()

        self.embed_window.protocol("WM_DELETE_WINDOW", self.on_close)

    def embed_message(self):
        # Your embedding functionality here
        pass

    def on_close(self):
        self.embed_window.destroy()
        self.master.embed_app = None  # Resetting the instance

class ExtractMessageApp:
    def __init__(self, master):
        self.master = master
        self.extract_window = tk.Toplevel(master)
        self.extract_window.title("Extract Message")

        self.extract_button = tk.Button(self.extract_window, text="Extract", command=self.extract_message)
        self.extract_button.pack()

        self.exitBtn = tk.Button(self.extract_window, text="Exit", command=self.extract_window.destroy)
        self.exitBtn.pack()

        self.extract_window.protocol("WM_DELETE_WINDOW", self.on_close)

    def extract_message(self):
        # Your extraction functionality here
        pass

    def on_close(self):
        self.extract_window.destroy()
        self.master.extract_app = None  # Resetting the instance

def runEmbedMessageApp():
    if not messageApp.embed_app:
        messageApp.embed_app = EmbedMessageApp(messageApp)

def runExtractMessageApp():
    if not messageApp.extract_app:
        messageApp.extract_app = ExtractMessageApp(messageApp)

messageApp = tk.Tk()
messageApp.title("Steganography Application")
messageApp.embed_app = None
messageApp.extract_app = None

embed_button = tk.Button(messageApp, text="Embed Message", command=runEmbedMessageApp)
embed_button.pack()

extract_button = tk.Button(messageApp, text="Extract Message", command=runExtractMessageApp)
extract_button.pack()

messageApp.mainloop()
