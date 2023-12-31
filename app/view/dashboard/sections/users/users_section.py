import customtkinter as ctk
import tkinter
import tkinter.messagebox
from ....global_style import GStyle
from ....libraries.professionalCTk import ProCTkTable, ProCTkScrollableFrame
from PIL import Image


class UsersSection(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            fg_color=GStyle.bg,
            bg_color=GStyle.bg
        )
