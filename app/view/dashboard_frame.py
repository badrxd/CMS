import customtkinter as ctk
import tkinter
import tkinter.messagebox

from app.core.Data_Handler.statistic import getStatistic

from .components.sidebar import Sidebar
from .components.header import Header


class DashboardFrame(ctk.CTkFrame):
    userId = ""
    __frames = {}

    def __init__(self, master, on_logout, userInfo):
        self.height = master.height
        self.width = master.width

        super().__init__(master, height=self.height,
                         width=self.width)
        self.userInfo = userInfo
        self.on_logout = on_logout
        self.create_header()
        self.create_sidebar()
        # logout_button = ctk.CTkButton(
        #     self, text="Logout", width=50, command=self.on_logout)
        # logout_button.pack()

    def create_sidebar(self):
        self.__frames["Sidebar"] = Sidebar(self)
        self.__frames["Sidebar"].place(x=0, y=0)

    def create_header(self):
        self.__frames["Header"] = Header(self)
        self.__frames["Header"].place(x=0, y=0)
