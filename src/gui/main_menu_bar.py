import tkinter as tk

def show_message():
    print("New has been clicked")
    pass

def quit_program():
    quit()
    pass

def create_main_menu_bar(root):
    main_menu_bar = tk.Menu(root)
    root.config(menu=main_menu_bar)
    file_menu = tk.Menu(main_menu_bar)
    main_menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=show_message)
    file_menu.add_command(label="Quit", command=quit_program)
    return main_menu_bar

