import os
import tkinter as tk
from tkinter import font

from .components.custom_entry import CustomEntry 


class MainWindow(tk.Tk):
    WINDOW_WIDTH = 450
    WINDOW_HEIGHT = 200

    BASE_DIR = os.path.dirname(__file__)
    FONT_PATH = os.path.join(BASE_DIR, "fonts", "Lato-Regular.ttf")

    def __init__(self):
        super().__init__()

        # SETTINGS WINDOW
        self.title("Freetube")
        self.geometry(self.evauluate_geometry(self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        custom_font = font.Font(family="family_lato", name="Lato", font=self.FONT_PATH)
        self.option_add("*Font", custom_font)

        # COMPONENTS WINDOW
        self.entry_url = CustomEntry(
            self,
            width=50,
            placeholder="Ingresa la url de video aqui."
        )
        self.entry_url.pack(padx=5, pady=15)

        self.button_url = tk.Button(self, text="prueba", command=self.get_video)
        self.button_url.pack()
    
    def get_video(self):
        return self.entry_url.get()
    

    
    def evauluate_geometry(self, window_width:int, window_height:int):
        # get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # get window dimensions
        position_x = int((screen_width - window_width) / 2)
        position_y = int((screen_height - window_height) / 2)-20

        return f"{window_width}x{window_height}+{position_x}+{position_y}"
