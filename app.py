import tkinter as tk
from tkinter import ttk

class TestProgress():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Descargando...')

        self.val=tk.IntVar()
        self.val.set(0)
        self.pbar = ttk.Progressbar(self.root, length=300,
                    maximum=10, variable=self.val)
        self.pbar.pack(padx=20, pady=20)

        tk.Label(self.root, textvariable=self.val,
                 bg="lightblue").pack()

        ## wait 2 seconds & update
        self.root.after(2000, self.advance)
        self.root.mainloop()

    def advance(self):
        value = 0
        for i in range(0, 1):
            print("ggg")
            self.val.set(100)

TP=TestProgress()