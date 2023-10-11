import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

# Function to hide a message within an image
def hide_message_in_image():
    cover_image_path = cover_image_path_var.get()
    secret_message = secret_message_var.get()
    output_image_path = output_image_path_var.get()

    cover_image = Image.open(cover_image_path)
    cover_array = np.array(cover_image)

    # Ensure the secret message length doesn't exceed 255 characters
    if len(secret_message) > 255:
        result_label.config(text="Message is too long! Maximum length: 255 characters")
        return

    # Convert the secret message length to a single byte
    message_length = len(secret_message).to_bytes(1, byteorder='big')

    binary_secret_message = ''.join(format(ord(char), '08b') for char in secret_message)

    stego_array = np.copy(cover_array)

    # Embed the message length in the last color channel
    stego_array[-1, -1, -1] = int.from_bytes(message_length, byteorder='big')

    message_index = 0
    for i in range(cover_array.shape[0]):
        for j in range(cover_array.shape[1]):
            for channel in range(3):
                if message_index < len(binary_secret_message):
                    stego_array[i, j, channel] = (cover_array[i, j, channel] & 0xFE) | int(binary_secret_message[message_index])
                    message_index += 1

    stego_image = Image.fromarray(stego_array.astype(np.uint8))
    stego_image.save(output_image_path, format='PNG')
    result_label.config(text="Secret message hidden successfully!")

# Function to extract the hidden message from an image
def extract_message_from_image():
    stego_image_path = stego_image_path_var.get()

    stego_image = Image.open(stego_image_path)
    stego_array = np.array(stego_image)

    # Extract the message length from the last color channel
    message_length = stego_array[-1, -1, -1]

    binary_secret_message = ""
    for i in range(stego_array.shape[0]):
        for j in range(stego_array.shape[1]):
            for channel in range(3):
                bit = stego_array[i, j, channel] & 1
                binary_secret_message += str(bit)

    # Extract the hidden message based on the specified length
    extracted_message = ""
    for i in range(0, message_length):
        byte = binary_secret_message[i * 8:(i + 1) * 8]
        extracted_message += chr(int(byte, 2))

    extracted_message_var.set(extracted_message)

# Create the main application window
app = tk.Tk()
app.title("Steganography Application")

# Variables to store file paths and message
cover_image_path_var = tk.StringVar()
stego_image_path_var = tk.StringVar()
secret_message_var = tk.StringVar()
output_image_path_var = tk.StringVar()
extracted_message_var = tk.StringVar()

# Create a label for the cover image path
cover_label = tk.Label(app, text="Select a cover image:")
cover_label.pack()

# Create an entry widget for the cover image path
cover_entry = tk.Entry(app, textvariable=cover_image_path_var)
cover_entry.pack()

# Create a button to browse for the cover image
cover_browse_button = tk.Button(app, text="Browse", command=lambda: cover_image_path_var.set(filedialog.askopenfilename()))
cover_browse_button.pack()

# Create a label for the secret message
message_label = tk.Label(app, text="Enter the secret message:")
message_label.pack()

# Create an entry widget for the secret message
message_entry = tk.Entry(app, textvariable=secret_message_var)
message_entry.pack()

# Create a label for the stego image path
stego_label = tk.Label(app, text="Stego image path:")
stego_label.pack()

# Create an entry widget for the stego image path
stego_entry = tk.Entry(app, textvariable=stego_image_path_var)
stego_entry.pack()

# Create a button to browse for the stego image
stego_browse_button = tk.Button(app, text="Browse", command=lambda: stego_image_path_var.set(filedialog.askopenfilename()))
stego_browse_button.pack()

# Create a label for the result
result_label = tk.Label(app, text="")
result_label.pack()

# Create a button to hide the message in the cover image
hide_button = tk.Button(app, text="Hide Message", command=hide_message_in_image)
hide_button.pack()

# Create a label for the extracted message
extracted_message_label = tk.Label(app, text="Extracted Message:")
extracted_message_label.pack()

# Create an entry widget for the extracted message
extracted_message_entry = tk.Entry(app, textvariable=extracted_message_var, state='readonly')
extracted_message_entry.pack()

# Create a button to extract the message from the stego image
extract_button = tk.Button(app, text="Extract Message", command=extract_message_from_image)
extract_button.pack()

# Start the main event loop
app.mainloop()