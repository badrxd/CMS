import tkinter
import customtkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


root = customtkinter.CTk()
root.title("Embedding in Tk")

fig = Figure(figsize=(5, 4),
             dpi=100,
             facecolor="red",
             edgecolor="red",
             )
t = np.arange(0, 3, 0.01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


root.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.
