import tkinter as tk
from tkinter import messagebox
'''
Sentences to test:-

1- STOP GLOBAL WARMING

2- AYMAN RAMADAN ELGAMAL

3- DR Omnia Ramadan
'''
def send_message():
    sentence = entry.get()
    if sentence:
        Esentence = encrypt(sentence, key)
        Dsentence = decrypt(Esentence, key)
        
        encrypted_label.config(text=f"Encrypted Sentence: {Esentence}")
        decrypted_label.config(text=f"Decrypted Sentence: {Dsentence}")
        
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a sentence!")

def encrypt(text, key):
    Etext = "" #to store the encrypted text
    for char in text:
        if char.isalpha():
            if char.islower():
                # Convert lowercase char to numeric value
                p = ord(char) - ord('a')  
                # Apply the encryption equation
                Echar = chr((p + key) % 26 + ord('a'))  
                Etext += Echar
            elif char.isupper():
                # Convert uppercase char to numeric value 
                p = ord(char) - ord('A')  
                # Apply the encryption equation
                Echar = chr((p + key) % 26 + ord('A'))  
                Etext += Echar
        else:
            Etext += char
    return Etext

def decrypt(text, key):
    Dtext = "" # to store the decrypted text
    for char in text:
        if char.isalpha():
            if char.islower():
                 # Convert lowercase char to its numeric value 
                p = ord(char) - ord('a') 
                # Apply the decryption equation
                Dchar = chr((p - key) % 26 + ord('a'))  
                Dtext += Dchar
            elif char.isupper():
                # Convert uppercase char to its numeric value 
                p = ord(char) - ord('A') 
                # Apply the decryption equation
                Dchar = chr((p - key) % 26 + ord('A')) 
                Dtext += Dchar
        else:
            Dtext += char
    return Dtext

def main():
    global entry, key, encrypted_label, decrypted_label
    key = 11

    root = tk.Tk()
    root.title("Chat")

    label = tk.Label(root, text="Enter your sentence:")
    label.pack()

    entry = tk.Entry(root, width=50)
    entry.pack()

    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack()
    
    encrypted_label = tk.Label(root, text="")
    encrypted_label.pack()
    
    decrypted_label = tk.Label(root, text="")
    decrypted_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
