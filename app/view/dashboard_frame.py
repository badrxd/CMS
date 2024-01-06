import customtkinter as ctk
import tkinter
import tkinter.messagebox
from .global_style import GStyle
from app.core.Data_Handler.GetHomeData import getStatistic
from .dashboard.sidebar import Sidebar
from .dashboard.header import Header
from .dashboard.sections.home.main import Home
from .dashboard.sections.users.main import UsersSection
from .dashboard.sections.customers.main import CustomersSection
from .dashboard.sections.revenues.main import RevenuesSection
from .dashboard.sections.reservations.main import ReservationsSection
from .dashboard.sections.cars.main import CarsSection
from .dashboard.main import Main

Sections = {
    "Home": Home,
    "UsersSection": UsersSection,
    "CustomersSection": CustomersSection,
    "RevenuesSection": RevenuesSection,
    "ReservationsSection": ReservationsSection,
    "CarsSection": CarsSection,
}


class DashboardFrame(ctk.CTkFrame):
    frames = {}

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
        self.frames["Sidebar"] = Sidebar(self)
        self.frames["Sidebar"].grid(
            column=0, row=0, rowspan=2, sticky="news")

    def create_header(self):
        """create header wigets"""
        self.frames["Header"] = Header(self)
        self.frames["Header"].grid(column=1, row=0, sticky="news")

    def create_main(self):
        self.main = Main(self)
