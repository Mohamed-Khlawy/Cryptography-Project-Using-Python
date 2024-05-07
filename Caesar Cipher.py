import tkinter as tk
from tkinter import filedialog, messagebox
import os.path

def encrypt(text, shift):
    shift = int(shift)  # Convert shift to integer
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift=None):
    if shift is None or shift == '':
        # Decrypt using all possible shifts (0 to 25)
        decrypted_texts = []
        for shift in range(26):
            decrypted_text = ""
            for char in text:
                if char.isupper():
                    decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
                elif char.islower():
                    decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
                else:
                    decrypted_text += char
            decrypted_texts.append(decrypted_text)
        return decrypted_texts
    else:
        # Decrypt using the specified shift value
        try:
            shift = int(shift)
            decrypted_text = ""
            for char in text:
                if char.isupper():
                    decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
                elif char.islower():
                    decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
                else:
                    decrypted_text += char
            return decrypted_text
        except ValueError:
            return "Invalid shift value for decryption."

def process_text(input_text, mode, shift=None):
    if mode == 'encrypt':
        return encrypt(input_text, shift)
    elif mode == 'decrypt':
        return decrypt(input_text, shift)
    else:
        return "Invalid mode"

def process_file(filename, mode, shift=None):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            return process_text(text, mode, shift)
    except FileNotFoundError:
        return "File not found"

def browse_file():
    filename = filedialog.askopenfilename()
    entry_file.delete(0, tk.END)
    entry_file.insert(0, filename)

def on_process():
    mode = var_mode.get()
    if var_input.get() == "file":
        filename = entry_file.get()
        shift = entry_shift.get()
        processed_text = process_file(filename, mode, shift)
    elif var_input.get() == "text":
        input_text = input_text_widget.get('1.0', tk.END)
        shift = entry_shift.get()
        processed_text = process_text(input_text, mode, shift)

    result_text.delete('1.0', tk.END)
    if mode == 'decrypt':
        if isinstance(processed_text, list):
            for text in processed_text:
                result_text.insert(tk.END, text + "\n")
        else:
            result_text.insert(tk.END, processed_text)
    else:
        result_text.insert(tk.END, processed_text)
    
    # Enable the Save button after processing is complete
    btn_save.config(state="normal")

def save():
    text = result_text.get("1.0", tk.END)
    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    
    # Check if user selected a filename
    if filename:
        with open(filename, "w") as file:
            file.write(text)
        # Get the filename without the path (just the last part)
        real_filename = os.path.basename(filename)
        message = f"Result saved successfully to ({real_filename})"
        # Show message box
        messagebox.showinfo(title="Successful Saving", message=message)

# Sky blue color definition
SKY_BLUE = "#87CEEB"

# Create main window
root = tk.Tk()
root.title("Caesar Cipher")
root.configure(bg=SKY_BLUE)  # Set the background color of the main window

# Input Selection
label_input = tk.Label(root, text="Select Input Type:", bg=SKY_BLUE)
label_input.grid(row=0, column=0, padx=5, pady=5)
var_input = tk.StringVar(root, "file")

def update_input():
    if var_input.get() == "file":
        entry_file.config(state="normal")
        input_text_widget.config(state="disabled")
        btn_browse.config(state="normal")
    elif var_input.get() == "text":
        entry_file.config(state="disabled")
        entry_file.delete(0, tk.END)
        input_text_widget.config(state="normal")
        btn_browse.config(state="disabled")

radio_file = tk.Radiobutton(root, text="File", variable=var_input, value="file", command=update_input, bg=SKY_BLUE)
radio_file.grid(row=0, column=1, padx=5, pady=5)
radio_text = tk.Radiobutton(root, text="Text", variable=var_input, value="text", command=update_input, bg=SKY_BLUE)
radio_text.grid(row=0, column=2, padx=5, pady=5)

# File Selection
label_file = tk.Label(root, text="Select File:", bg=SKY_BLUE)
label_file.grid(row=1, column=0, padx=5, pady=5)
entry_file = tk.Entry(root, width=40, state="disabled")
entry_file.grid(row=1, column=1, padx=5, pady=5)
btn_browse = tk.Button(root, text="Browse", command=browse_file, state="disabled", bg=SKY_BLUE)
btn_browse.grid(row=1, column=2, padx=5, pady=5)

# Input Text
label_input_text = tk.Label(root, text="Input Text:", bg=SKY_BLUE)
label_input_text.grid(row=2, column=0, padx=5, pady=5)
input_text_widget = tk.Text(root, height=5, width=40, state="disabled")
input_text_widget.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

# Mode Selection
label_mode = tk.Label(root, text="Select Mode:", bg=SKY_BLUE)
label_mode.grid(row=3, column=0, padx=5, pady=5)
var_mode = tk.StringVar(root, "encrypt")
radio_encrypt = tk.Radiobutton(root, text="Encrypt", variable=var_mode, value="encrypt", bg=SKY_BLUE)
radio_encrypt.grid(row=3, column=1, padx=5, pady=5)
radio_decrypt = tk.Radiobutton(root, text="Decrypt", variable=var_mode, value="decrypt", bg=SKY_BLUE)
radio_decrypt.grid(row=3, column=2, padx=5, pady=5)

# key Selection
label_key = tk.Label(root, text="Enter Key:", bg=SKY_BLUE)
label_key.grid(row=4, column=0, padx=5, pady=5)
entry_shift = tk.Entry(root, width=10)
entry_shift.grid(row=4, column=1, padx=5, pady=5)

# Process Button
btn_process = tk.Button(root, text="Process", command=on_process, bg=SKY_BLUE)
btn_process.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Save Button
btn_save = tk.Button(root, text = "Save", command=save, state= "disabled", bg=SKY_BLUE)
btn_save.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

# Result Display
result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()