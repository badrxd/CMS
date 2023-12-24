import customtkinter as ctk
import tkinter
import tkinter.messagebox
from .global_style import GStyle
from app.core.Data_Handler.GetHomeData import getStatistic
from .components.sidebar import Sidebar
from .components.header import Header
from .components.home import Home

Sections = {
    "Home": Home,
}


class DashboardFrame(ctk.CTkFrame):
    __frames = {}

    def __init__(self, master, userInfo):
        super().__init__(master)

        self.userInfo = userInfo
        self.on_logout = master.show_login
        self.refresh = master.show_dashboard

        """split the width"""
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=50)

        """split the height"""
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=100)

        """create wigets"""
        self.create_sidebar()
        self.create_header()
        self.create_main()

    def create_sidebar(self):
        """create sidebar wigets"""
        self.__frames["Sidebar"] = Sidebar(self)
        self.__frames["Sidebar"].grid(
            column=0, row=0, rowspan=2, sticky="news")

    def create_header(self):
        """create header wigets"""
        self.__frames["Header"] = Header(self)
        self.__frames["Header"].grid(column=1, row=0, sticky="news")

    def create_main(self, section="Home"):
        """create main wigets"""
        self.__frames[section] = Sections[section](self)
        self.__frames[section].grid(column=1, row=1, sticky="news")
        nav = getattr(self.__frames["Sidebar"],
                      "{}_label".format(section.lower()))
        nav.configure(fg_color=GStyle.buttons_hover_color,
                      bg_color=GStyle.buttons_hover_color)
