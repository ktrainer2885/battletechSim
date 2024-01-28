""" THis is the main file for the battletech simulator.
It shoul run the basic gui and connect to the rest of the libraries for the program
"""
import tkinter as tk
from src.gui.main_menu_bar import create_main_menu_bar

def main():
    root = tk.Tk()
    main_menu_bar = create_main_menu_bar(root)
    root.config(menu=main_menu_bar)
    root.geometry("800x600")
    root.title("BattleTech Simulator")
    label = tk.Label(root, text="BattleTech")
    label.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
