import customtkinter as ctk
from .....global_style import GStyle
from .....libraries.professionalCTk import ProCTkTable, ProCTkScrollableFrame
from PIL import Image


class SingleCar(ctk.CTkFrame):
    def __init__(self, master, manager):
        super().__init__(
            master,
            fg_color=GStyle.bg,
            bg_color=GStyle.bg
        )
        ctk.CTkLabel(self, text='single car info').pack()
