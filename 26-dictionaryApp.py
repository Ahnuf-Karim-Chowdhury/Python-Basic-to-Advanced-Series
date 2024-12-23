import tkinter as tk
from tkinter import messagebox
import requests

class DictionaryApp:
    def __init__(self, master):
        self.master = master
        master.title("Dictionary App")

        self.label = tk.Label(master, text="Enter a word:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.lookup_button = tk.Button(master, text="Look Up", command=self.lookup_word)
        self.lookup_button.pack()

        self.meaning_label = tk.Label(master, text="", wraplength=300)
        self.meaning_label.pack()

    def lookup_word(self):
        word = self.entry.get().strip()
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

        if response.status_code == 200:
            data = response.json()
            meanings = data[0]['meanings']
            meanings_text = ""
            for meaning in meanings:
                definitions = meaning['definitions']
                meanings_text += f"{meaning['partOfSpeech']}: "
                meanings_text += ", ".join([definition['definition'] for definition in definitions]) + "\n"
            self.meaning_label.config(text=meanings_text)
        else:
            messagebox.showinfo("Not Found", f"The word '{word}' was not found in the dictionary.")

# Create the main window
root = tk.Tk()
app = DictionaryApp(root)

# Start the GUI event loop
root.mainloop()
