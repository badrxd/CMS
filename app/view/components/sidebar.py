import customtkinter as ctk
import tkinter
import tkinter.messagebox


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(
            master,
            fg_color="#3DF8FE",
            bg_color="#3DF8FE"
        )
        """app name"""
        name_label = ctk.CTkLabel(
            self, text="CMS", font=("Tekton Pro", 22), text_color="white")
        name_label.pack(pady=40, padx=40)

        """home"""
        home_label = ctk.CTkLabel(
            self, text="home", font=("", 16), text_color="white")
        home_label.pack(pady=20, padx=10)

        """cars"""
        cars_label = ctk.CTkLabel(
            self, text="cars", font=("", 16), text_color="white")
        cars_label.pack(pady=20, padx=10)

        """reservations"""
        res_label = ctk.CTkLabel(
            self, text="reservations", font=("", 16), text_color="white")
        res_label.pack(pady=20, padx=10)

        """revenue"""
        res_label = ctk.CTkLabel(
            self, text="revenue", font=("", 16), text_color="white")
        res_label.pack(pady=20, padx=10)

        """customers"""
        res_label = ctk.CTkLabel(
            self, text="customers", font=("", 16), text_color="white")
        res_label.pack(pady=20, padx=10)

        """users"""
        res_label = ctk.CTkLabel(
            self, text="users", font=("", 16), text_color="white")
        res_label.pack(pady=10, padx=10)

        logout_button = ctk.CTkButton(
            self, text="Logout", width=50, fg_color="#3DAF8D", hover_color="#4C917D", command=master.on_logout)
        logout_button.place(relx=0.5, rely=0.95, anchor="s")
