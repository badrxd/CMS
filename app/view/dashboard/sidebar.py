import customtkinter as ctk
from PIL import Image
import tkinter
import tkinter.messagebox
from ..global_style import GStyle
from PIL import Image


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(
            master,
            fg_color=GStyle.sidebar_bg,
            bg_color=GStyle.sidebar_bg,
        )
        self.master = master

        """create an image object"""
        # image = ctk.CTkImage(light_image=Image.open(
        #     "/home/omarnem/omar/CMS/resources/icons/CMSlogo.png"), size=(100, 100))

        # """add the image to a wiget"""
        # name_label = ctk.CTkLabel(
        #     self, text="", image=image)
        # name_label.grid(row=0, column=0)

        """home"""
        icon = ctk.CTkImage(light_image=Image.open(
            "resources/icons/sidebar/home.png"), size=(30, 30))
        self.home_label = ctk.CTkButton(self,
                                        text="",
                                        image=icon,
                                        width=10,
                                        anchor="center",
                                        font=(GStyle.font_family,
                                              GStyle.meduim),
                                        text_color=GStyle.sidebar_font_color,
                                        bg_color=GStyle.sidebar_bg,
                                        fg_color=GStyle.sidebar_bg,
                                        hover_color=GStyle.buttons_hover_color,
                                        corner_radius=6,
                                        command=self.home_section
                                        )

        # self.home_label.grid(row=1, column=0, sticky="new")
        self.home_label.pack(pady=5)

        """cars"""
        icon = ctk.CTkImage(light_image=Image.open(
            "resources/icons/sidebar/cars.png"), size=(30, 30))
        self.carssection_label = ctk.CTkButton(self,
                                               text="",
                                               image=icon,
                                               width=10,
                                               anchor="w",
                                               font=(GStyle.font_family,
                                                     GStyle.meduim),
                                               text_color=GStyle.sidebar_font_color,
                                               bg_color=GStyle.sidebar_bg,
                                               fg_color=GStyle.sidebar_bg,
                                               hover_color=GStyle.buttons_hover_color,
                                               corner_radius=6,
                                               command=self.cars_section)

        # self.carssection_label.grid(row=2, column=0, sticky="new")
        self.carssection_label.pack(pady=5)

        """reservations"""
        icon = ctk.CTkImage(light_image=Image.open(
            "resources/icons/sidebar/reservations.png"), size=(30, 30))
        self.reservationssection_label = ctk.CTkButton(self,
                                                       image=icon,
                                                       text="",
                                                       width=10,
                                                       anchor="w",
                                                       font=(GStyle.font_family,
                                                             GStyle.meduim),
                                                       text_color=GStyle.sidebar_font_color,
                                                       bg_color=GStyle.sidebar_bg,
                                                       fg_color=GStyle.sidebar_bg,
                                                       hover_color=GStyle.buttons_hover_color,
                                                       corner_radius=6,
                                                       command=self.reservations_section)

        self.reservationssection_label.pack(pady=5)

        """revenue"""
        icon = ctk.CTkImage(light_image=Image.open(
            "resources/icons/sidebar/revenues.png"), size=(30, 30))
        self.revenuessection_label = ctk.CTkButton(self,
                                                   image=icon,
                                                   text="",
                                                   anchor="w",
                                                   width=10,
                                                   font=(GStyle.font_family,
                                                         GStyle.meduim),
                                                   text_color=GStyle.sidebar_font_color,
                                                   bg_color=GStyle.sidebar_bg,
                                                   fg_color=GStyle.sidebar_bg,
                                                   hover_color=GStyle.buttons_hover_color,
                                                   corner_radius=6,
                                                   command=self.revenues_section)

        self.revenuessection_label.pack(pady=5)

        """customers"""
        icon = ctk.CTkImage(light_image=Image.open(
            "resources/icons/sidebar/customers.png"), size=(30, 30))
        self.customerssection_label = ctk.CTkButton(self,
                                                    image=icon,
                                                    text="",
                                                    anchor="w",
                                                    width=10,
                                                    font=(GStyle.font_family,
                                                          GStyle.meduim),
                                                    text_color=GStyle.sidebar_font_color,
                                                    bg_color=GStyle.sidebar_bg,
                                                    fg_color=GStyle.sidebar_bg,
                                                    hover_color=GStyle.buttons_hover_color,
                                                    corner_radius=6,
                                                    command=self.customers_section)

        # self.customerssection_label.grid(row=5, column=0, sticky="new")
        self.customerssection_label.pack(pady=5)

        if self.master.userInfo["role"] == "admin":
            """users"""
            icon = ctk.CTkImage(light_image=Image.open(
                "resources/icons/sidebar/users.png"), size=(30, 30))
            self.userssection_label = ctk.CTkButton(self,
                                                    image=icon,
                                                    text="",
                                                    anchor="w",
                                                    width=10,
                                                    font=(GStyle.font_family,
                                                          GStyle.meduim),
                                                    text_color=GStyle.sidebar_font_color,
                                                    bg_color=GStyle.sidebar_bg,
                                                    fg_color=GStyle.sidebar_bg,
                                                    hover_color=GStyle.buttons_hover_color,
                                                    corner_radius=6,
                                                    command=self.users_section)

            # self.userssection_label.grid(row=6, column=0, sticky="new")
            self.userssection_label.pack(pady=5)

        """logout button"""
        icon = ctk.CTkImage(light_image=Image.open(
            "resources/icons/sidebar/logout.png"), size=(30, 30))
        self.logout_label = ctk.CTkButton(self,
                                          image=icon,
                                          text="",
                                          anchor="w",
                                          width=10,
                                          font=(GStyle.font_family,
                                                GStyle.meduim),
                                          text_color=GStyle.sidebar_font_color,
                                          bg_color=GStyle.sidebar_bg,
                                          fg_color=GStyle.sidebar_bg,
                                          hover_color=GStyle.buttons_hover_color,
                                          corner_radius=6,
                                          command=self.log_out)

        # self.userssection_label.grid(row=6, column=0, sticky="new")
        self.logout_label.pack(pady=5)

        """create a border right"""
        ctk.CTkFrame(self, height=1000, width=1, border_color=GStyle.frames_border, border_width=1,
                     fg_color=GStyle.frames_border,
                     bg_color=GStyle.frames_border).place(relx=1, rely=0.5, anchor="e")

    def home_section(self):
        self.master.main.create_main("Home")

    def users_section(self):
        self.master.main.create_main("UsersSection")

    def customers_section(self):
        self.master.main.create_main("CustomersSection")

    def cars_section(self):
        self.master.main.create_main("CarsSection")

    def revenues_section(self):
        self.master.main.create_main("RevenuesSection")

    def reservations_section(self):
        self.master.main.create_main("ReservationsSection")

    def log_out(self):
        del self.master.main.frames["current"]
        self.master.on_logout()
