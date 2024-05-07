import tkinter as tk
from tkinter import messagebox
import subprocess
from subprocess import call
import os

# Function to open a new page when a button is clicked
def open_linked_page(filename):
    """Runs a Python file based on the button click."""
    if filename.endswith(".py"):
        # Construct the full path with .py extension
        full_path = os.path.join(os.getcwd(), filename)
        try:
            # Use subprocess to execute the Python script
            subprocess.run(["python", full_path])
        except FileNotFoundError:
            print(f"File '{filename}' not found. Please check the path.")
    else:
        print(f"Please provide a filename with the '.py' extension.")

# Sky blue color definition
SKY_BLUE = "#87CEEB"

# Create the main window
root = tk.Tk()
root.title("Cryptography Project")

# Set window size to a large value (adjust as needed)
root.geometry("1000x600")

# Create a frame to center the content
content_frame = tk.Frame(root, bg=SKY_BLUE)
content_frame.pack(fill="both", expand=True)

# Project title label (large font size)
title_label = tk.Label(content_frame, text="White Team Cryptography Project", font=("Arial", 24, "bold"), bg=SKY_BLUE)
title_label.pack(pady=20)

# Project description paragraph
description_label = tk.Label(content_frame, text=f"""Welcome to our Cryptography Project\nHere you will be able to use these algorithms:\n(Caesar Cipher, Multiplicative Cipher, Rot 13, One Time Padding)\nYou will be able to Encrypt and Decrypt any text you want using these algorithms. \nYou also can take your text from a file on your device.\nFinally, you will be able to save your results of Encryption or Decryption in a file on your device for later using.\nGo on bro and start your journey in Encryption and Decryption!!""", justify="center",font=("Arial", 13),bg=SKY_BLUE)
description_label.pack(pady=10)

# Inner frame for bottom section (two columns)
bottom_frame = tk.Frame(content_frame, bg=SKY_BLUE)
bottom_frame.pack(fill="both", expand=True)

# Left frame for team and advisors (listboxes or labels)
left_frame = tk.Frame(bottom_frame, bg=SKY_BLUE)
left_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=125)  # Grid layout
# left_frame.pack(side="left", fill="y", expand=True)

# Sample team and advisor labels (replace with listboxes if preferred)
team_label = tk.Label(left_frame, text=f"Team Members:\nMohamed Abdelrahman Elkhlawy\nReem Ashraf Mohamed", font=("Arial", 16, "bold"), bg=SKY_BLUE)
team_label.pack(pady=10)
advisor_label = tk.Label(left_frame, text=f"Project Advisors:\nDr. Mohamed Abdel Hameed\nEng. Samar Mahmoud", font=("Arial", 16, "bold"), bg=SKY_BLUE)
advisor_label.pack(pady=10)

# Right frame for buttons
right_frame = tk.Frame(bottom_frame, bg=SKY_BLUE)
right_frame.grid(row=0, column=25, sticky="nsew", padx=350, pady=110)  # Grid layout
# right_frame.pack(side="right", fill="both", expand=True)

# Button definitions (modify button text and command as needed)
button1 = tk.Button(right_frame, text="Caesar Cipher", command=lambda: open_linked_page("Caesar Cipher.py"), bg=SKY_BLUE, font=("Arial", 14))
button1.pack(pady=10, padx=10)

button2 = tk.Button(right_frame, text="Multiplicative Cipher", command=lambda: open_linked_page("Multiplicative Cipher.py"), bg=SKY_BLUE, font=("Arial", 14))
button2.pack(pady=10, padx=10)

button3 = tk.Button(right_frame, text="ROT 13", command=lambda: open_linked_page("ROT 13.py"), bg=SKY_BLUE, font=("Arial", 14))
button3.pack(pady=10, padx=10)

button4 = tk.Button(right_frame, text="One Time Padding", command=lambda: open_linked_page("One Time Padding.py"), bg=SKY_BLUE, font=("Arial", 14))
button4.pack(pady=10, padx=10)

# Ensure content scales with window size
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)


# Run the main loop
root.mainloop()