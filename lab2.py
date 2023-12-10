import os
import json
from tkinter import Tk, Label, Button, filedialog

class OfflineFileManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Offline File Manager")

        self.data = {}
        self.load_data()

        self.label = Label(root, text="Offline File Manager")
        self.label.pack()

        self.button_save = Button(root, text="Save Data", command=self.save_data)
        self.button_save.pack()

        self.button_browse = Button(root, text="Browse", command=self.browse_directory)
        self.button_browse.pack()

    def load_data(self):
        try:
            with open("file_manager_data.json", "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            pass

    def save_data(self):
        with open("file_manager_data.json", "w") as file:
            json.dump(self.data, file)

    def browse_directory(self):
        directory = filedialog.askdirectory(title="Select Directory")
        if directory:
            self.data[directory] = os.listdir(directory)
            print(f"Saved data for directory: {directory}")

if __name__ == "__main__":
    root = Tk()
    app = OfflineFileManager(root)
    root.mainloop()
