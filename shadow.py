import customtkinter as ctk
win = ctk.CTk()
win.geometry("500x500")


def gradient(master, color1, inc=2, rows=1, columns=100, size=2):
    c_inc = inc
    color = int(color1[1:], 16)
    global_frame = ctk.CTkFrame(master)

    if rows <= 1:
        global_frame.rowconfigure(0, weight=1)
        for i in range(columns):
            global_frame.columnconfigure(i, weight=1)
        for i in range(columns):
            hexacolor = hex(color)[2:]
            while len(hexacolor) < 6:
                hexacolor = "0{}".format(hexacolor)
            _frame = ctk.CTkFrame(
                global_frame, fg_color=f"#{str(hexacolor)}", bg_color=f"#{str(hexacolor)}", width=size)
            color += c_inc
            _frame.grid(row=0, column=i, sticky="news")
    else:
        global_frame.columnconfigure(0, weight=1)
        for i in range(rows):
            global_frame.rowconfigure(i, weight=1)
        for i in range(rows):
            hexacolor = hex(color)[2:]
            while len(hexacolor) < 6:
                hexacolor = "0{}".format(hexacolor)
            _frame = ctk.CTkFrame(
                global_frame, fg_color=f"#{str(hexacolor)}", bg_color=f"#{str(hexacolor)}", width=size)
            color += c_inc
            _frame.grid(row=i, column=0)

    return global_frame


win.columnconfigure(0, weight=1)
win.rowconfigure(0, weight=1)

gradient(win, "#010000", columns=250, inc=1,
         size=15).grid(row=0, column=0, rowspan=1, sticky="news")

win.mainloop()
