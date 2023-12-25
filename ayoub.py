from app.view.libraries.professionalCTk import ProCTkTable

import customtkinter as ctk
win = ctk.CTk()
win.geometry("500x500")

win.columnconfigure(0, weight=1)
win.columnconfigure(1, weight=1)
win.columnconfigure(2, weight=1)
win.rowconfigure(0, weight=1)
win.rowconfigure(1, weight=1)
win.rowconfigure(2, weight=1)


new_frame = ctk.CTkFrame(win)

new_frame.grid(column=1, row=1)
new_frame.columnconfigure(0, weight=1)
new_frame.columnconfigure(1, weight=1)
new_frame.columnconfigure(2, weight=1)
new_frame.rowconfigure(0, weight=1)
new_frame.rowconfigure(1, weight=1)
new_frame.rowconfigure(2, weight=1)


b = ctk.CTkFrame(new_frame, width=2, fg_color="red").grid(
    column=0, row=1, sticky="news")

f = ctk.CTkFrame(new_frame).grid(column=1, row=1)

dic = [
    {"name": "omar", "age": 22, "number": 1},
    {"name": "omar", "age": 22, "number": 1},
    {"name": "omar", "age": 22, "number": 1},
    {"name": "omar", "age": 22, "number": 1},
    {"name": "omar", "age": 22, "number": 1},
    {"name": "omar", "age": 22, "number": 1},
    {"name": "omar", "age": 22, "number": 1},
    {"name": "omar", "age": 22, "number": 1},
    {"name": "omar", "age": 22, "number": 1},
    {"name": "omar", "age": 22, "number": 1},
    {"name": "omar", "age": 22, "number": 1}
]


win.mainloop()
