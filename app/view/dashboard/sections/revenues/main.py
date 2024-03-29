import customtkinter as ctk
import tkinter
import tkinter.messagebox
from ....global_style import GStyle
from ....libraries.professionalCTk import ProCTkTable, ProCTkScrollableFrame
from PIL import Image


class RevenuesSection(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            fg_color=GStyle.bg,
            bg_color=GStyle.bg
        )

    def display(self):
        self.grid(column=1, row=1, sticky="news")

        # def on_key_press(event):
        #     print("you pressed {}".format(event.key))
        #     key_press_handler(event, canvas, toolbar)

        # canvas.mpl_connect("key_press_event", on_key_press)
