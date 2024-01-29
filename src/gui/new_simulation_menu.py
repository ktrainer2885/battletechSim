import tkinter as ttk

new_simulation = None

def show_message():
    print("New has been clicked")
    pass

def quit_program():
    pass

def create_new_simulation_menu():
    global new_simulation
    if new_simulation is not None:
        new_simulation.destroy()
    new_simulation = ttk.Toplevel()
    new_simulation.title("New Simulation")
    new_simulation.geometry("400x300")

    label = ttk.Label(new_simulation, text="New simulation")
    label.grid(row=0, column=0)

    btn1 = ttk.Button(new_simulation, text="Select Force A")
    btn1.grid(row=1, column=0)

    btn2 = ttk.Button(new_simulation, text="Select Force B")
    btn2.grid(row=1, column=1)

    label_force_a = ttk.Label(new_simulation, text="Force A units")
    label_force_a.grid(row=2, column=0)

    label_force_b = ttk.Label(new_simulation, text="Force B Units")
    label_force_b.grid(row=2, column=1)

    btn3 = ttk.Button(new_simulation, text="Start Simulation")
    btn3.grid(row=3, column=0, columnspan=2)
    return new_simulation