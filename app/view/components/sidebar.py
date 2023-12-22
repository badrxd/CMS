import customtkinter as ctk
from PIL import Image
import tkinter
import tkinter.messagebox
from ..global_style import GStyle


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(
            master,
            fg_color=GStyle.sidebar_bg,
            bg_color=GStyle.sidebar_bg
        )
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=5)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=20)

        """create an image object"""
        # image = ctk.CTkImage(light_image=Image.open(
        #     "/home/omarnem/omar/CMS/resources/icons/CMSlogo.png"), size=(100, 100))

        # """add the image to a wiget"""
        # name_label = ctk.CTkLabel(
        #     self, text="", image=image)
        # name_label.grid(row=0, column=0)

        """home"""
        self.home_label = ctk.CTkButton(
            self, text="home", anchor="w", font=(GStyle.font_family, GStyle.meduim), text_color=GStyle.head_font_color, bg_color=GStyle.sidebar_bg, fg_color=GStyle.sidebar_bg, hover_color=GStyle.header_bg, corner_radius=0)
        # home_label.pack(pady=20, padx=0)
        self.home_label.grid(row=1, column=0, sticky="new")

        """cars"""
        self.car_label = ctk.CTkButton(
            self, text="cars", anchor="w", font=(GStyle.font_family, GStyle.meduim), text_color=GStyle.head_font_color, bg_color=GStyle.sidebar_bg, fg_color=GStyle.sidebar_bg, hover_color=GStyle.header_bg, corner_radius=0)
        # cars_label.pack(pady=20, padx=0)
        self.car_label.grid(row=2, column=0, sticky="new")

        """reservations"""
        self.reservation_label = ctk.CTkButton(
            self, text="reservations", anchor="w", font=(GStyle.font_family, GStyle.meduim), text_color=GStyle.head_font_color, bg_color=GStyle.sidebar_bg, fg_color=GStyle.sidebar_bg, hover_color=GStyle.header_bg, corner_radius=0)
        # res_label.pack(pady=20, padx=0)
        self.reservation_label.grid(row=3, column=0, sticky="new")

        """revenue"""
        self.revenue_label = ctk.CTkButton(
            self, text="revenue", anchor="w", font=(GStyle.font_family, GStyle.meduim), text_color=GStyle.head_font_color, bg_color=GStyle.sidebar_bg, fg_color=GStyle.sidebar_bg, hover_color=GStyle.header_bg, corner_radius=0)
        # revenue_label.pack(pady=20, padx=0)
        self.revenue_label.grid(row=4, column=0, sticky="new")

        """customers"""
        self.customer_label = ctk.CTkButton(
            self, text="customers", anchor="w", font=(GStyle.font_family, GStyle.meduim), text_color=GStyle.head_font_color, bg_color=GStyle.sidebar_bg, fg_color=GStyle.sidebar_bg, hover_color=GStyle.header_bg, corner_radius=0)
        # customers_label.pack(pady=20, padx=0)
        self.customer_label.grid(row=5, column=0, sticky="new")

        """users"""
        self.user_label = ctk.CTkButton(
            self, text="users", anchor="w", font=(GStyle.font_family, GStyle.meduim), text_color=GStyle.head_font_color, bg_color=GStyle.sidebar_bg, fg_color=GStyle.sidebar_bg, hover_color=GStyle.header_bg, corner_radius=0)
        # users_label.pack(pady=10, padx=0)
        self.user_label.grid(row=6, column=0, sticky="new")

        logout_button = ctk.CTkButton(
            self, text="Logout", width=50, fg_color=GStyle.buttons_bg, hover_color=GStyle.buttons_hover_color, command=master.on_logout)
        logout_button.place(relx=0.5, rely=0.95, anchor="s")
