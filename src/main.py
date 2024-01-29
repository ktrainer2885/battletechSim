import tkinter as tk
from src.gui.main_menu_bar import create_main_menu_bar
from src.gui.new_simulation_menu import create_new_simulation_menu

def on_new_simulation():
    new_simulation = create_new_simulation_menu()



def main():
    root = tk.Tk()
    root.geometry("400x300")
    root.title("BattleTech Simulator")

    main_menu_bar = create_main_menu_bar(root)
    root.config(menu=main_menu_bar)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    label = tk.Label(root, text="BattleTech Simulator", font=("Helvetica","16"))
    label.grid(row=0, column=0, sticky=(tk.W + tk.E), padx=5, pady=5)

    btn1 = tk.Button(root, text="New Simulation", command=on_new_simulation)
    btn1.grid(row=1, column=0, sticky=(tk.W + tk.E), padx=5, pady=5)

    btn2 = tk.Button(root, text="Load Simulation")
    btn2.grid(row=2, column=0, sticky=(tk.W + tk.E), padx=5, pady=5)

    btn3 = tk.Button(root, text="View Report")
    btn3.grid(row=3, column=0, sticky=(tk.W+tk.E), padx=5, pady=5)

    btn4 = tk.Button(root, text="Quit", command=root.quit)
    btn4.grid(row=4, column=0, sticky=(tk.W+tk.E), padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()