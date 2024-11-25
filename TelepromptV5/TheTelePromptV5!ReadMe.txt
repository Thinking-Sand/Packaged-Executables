TheTelePromptV5! 
Up Arrow Key scrolls up.
Down Arrow key scrolls down.
Left Arrow key reduces font size.
Right Arrow key increases font size. 
Space Auto Scolls down, and also resets script.

One click to run, Windows .exe Free manual teleprompt!


conda create -n NAME python=3.11

Change NAME to what ever you want your venv named.

Hit Y and then Enter to begin env setup.

conda activate NAME








import tkinter as tk
from tkinter import font

class Teleprompter:
    def __init__(self, root):
        self.root = root
        self.root.title("Teleprompter")
        self.root.geometry("800x1000")
        self.root.configure(bg='black')

        self.text = tk.Text(root, wrap='word', bg='black', fg='white', font=('Arial', 20))
        self.text.pack(expand=True, fill='both')

        self.scroll_speed = 100
        self.is_scrolling = False

        # Load your script here
        script = "Your script goes here. " * 100
        self.text.insert('1.0', script)

        # Key bindings
        self.root.bind('<Up>', self.manual_scroll_up)
        self.root.bind('<Down>', self.manual_scroll_down)
        self.root.bind('<Right>', self.increase_font_size)
        self.root.bind('<Left>', self.decrease_font_size)
        self.root.bind('<space>', self.toggle_scroll)

        self.auto_scroll()

    def increase_font_size(self, event=None):
        current_font = font.Font(font=self.text['font'])
        new_size = min(200, current_font.actual()['size'] + 10)  # Increase font size significantly
        self.text.config(font=('Arial', new_size))

    def decrease_font_size(self, event=None):
        current_font = font.Font(font=self.text['font'])
        new_size = max(10, current_font.actual()['size'] - 10)  # Decrease font size significantly
        self.text.config(font=('Arial', new_size))

    def toggle_scroll(self, event=None):
        self.is_scrolling = not self.is_scrolling

    def manual_scroll_up(self, event=None):
        self.text.yview_scroll(-1, 'units')

    def manual_scroll_down(self, event=None):
        self.text.yview_scroll(1, 'units')

    def auto_scroll(self):
        if self.is_scrolling:
            self.text.yview_scroll(1, 'units')
        self.root.after(self.scroll_speed, self.auto_scroll)

if __name__ == "__main__":
    root = tk.Tk()
    app = Teleprompter(root)
    root.mainloop()







Save code as: teleprompter.py

pip install pyinstaller

pyinstaller --onefile --windowed teleprompter.py

Simple and Done. 


Created by Zechariah P. 
No License. Use how ever you see fit















