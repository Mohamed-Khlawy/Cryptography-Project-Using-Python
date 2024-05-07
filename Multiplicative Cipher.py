import tkinter as tk
from tkinter import filedialog, messagebox
import os.path
#---------------------------------------------------------------------------------------

# The key and alphabet length should be coprime
def are_coprime(a, b):
  # Handle negative inputs (coprime definition applies to positive integers)
  if a <= 0 or b <= 0:
    return False

  # Efficiently calculate the greatest common divisor (GCD) using the Euclidean algorithm
  while b != 0:
    a, b = b, a % b
  return a == 1  # If GCD is 1, then a and b are coprime
#---------------------------------------------------------------------------------------

# Multiplicative Cipher Encryption Function
def Multiplicative_Cipher_Encryption(message, key):
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    if are_coprime(key, 26):
        cipher = ""

        for char in message:
            if char in upper_alphabet:
                curr_index = upper_alphabet.index(char)
                new_index = (curr_index * key) % len(upper_alphabet)
                new_char = upper_alphabet[new_index]
                
                cipher += new_char

            elif char in lower_alphabet:
                curr_index = lower_alphabet.index(char)
                new_index = (curr_index * key) % len(lower_alphabet)
                new_char = lower_alphabet[new_index]
                
                cipher += new_char

            else:
                cipher += char

        return cipher
    
    else:
        error_message = "Error, The key and alphabet length aren't coprime"
        return error_message
#---------------------------------------------------------------------------------------
# Multiplicative Cipher Decryption Using Maketrans

def Create_Corresponding_Alphabet(key):
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    corr_upper_alphabet = ""
    corr_lower_alphabet = ""

    for char in upper_alphabet:
        curr_index = upper_alphabet.index(char)
        new_index = (curr_index * key) % len(upper_alphabet)

        corr_upper_alphabet += upper_alphabet[new_index]
        corr_lower_alphabet = corr_upper_alphabet.lower()

    return corr_upper_alphabet, corr_lower_alphabet
#----------------------------------------------------------
def Multiplicative_Cipher_Decryption(cipher, key):
    if are_coprime(key, 26):
        corr_upper_alphabet, corr_lower_alphabet = Create_Corresponding_Alphabet(key)

        all_corresponding = corr_upper_alphabet + corr_lower_alphabet

        Multiplicative_Trans = str.maketrans(all_corresponding, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

        message = cipher.translate(Multiplicative_Trans)

        return message
        
    else:
        error_message = "Error, The key and alphabet length aren't coprime"
        return error_message
#---------------------------------------------------------------------------------------

# Multiplicative Cipher Main page components and function
def process_text(input_text, mode, key):
    if mode == 'encrypt':
        return Multiplicative_Cipher_Encryption(input_text, key)
    elif mode == 'decrypt':
        return Multiplicative_Cipher_Decryption(input_text, key)
    else:
        return "Invalid mode"

def process_file(filename, mode, key):
    with open(filename, 'r') as file:
        text = file.read()
        return process_text(text, mode, key)

def browse_file():
    filename = filedialog.askopenfilename()
    entry_file.delete(0, tk.END)
    entry_file.insert(0, filename)

def on_process():
    if var_input.get() == "file":
        filename = entry_file.get()
        mode = var_mode.get()
        key = int(entry_key.get())
        if mode == 'encrypt':
            processed_text = process_file(filename, mode, key)
        else:
            processed_text = process_file(filename, mode, key)
    elif var_input.get() == "text":
        mode = var_mode.get()
        input_text = input_text_widget.get('1.0', tk.END)
        key = int(entry_key.get())
        if mode == 'encrypt':
            processed_text = process_text(input_text, mode, key)
        else:
            processed_text = process_text(input_text, mode, key)
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, processed_text)
    btn_save.config(state= "normal")
      
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
root.title("Multiplicative Cipher")
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
entry_key = tk.Entry(root, width=10)
entry_key.grid(row=4, column=1, padx=5, pady=5)

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