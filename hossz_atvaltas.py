#tkinter importálása a programba
import tkinter as tk
from tkinter import *

# Számolás gomb funkciói
def convert_units():
    try:
        value = float(bemenet.get())
        from_unit = clicked.get()
        to_unit = clicked2.get()

        # Átváltási számolások
        length_factors = {
            "Milliméter": 0.001,
            "Centiméter": 0.01,
            "Méter": 1,
            "Kilométer": 1000
        }

        volume_factors = {
            "Milliliter": 0.001,
            "Centiliter": 0.01,
            "Liter": 1,
            "Köbméter": 1000
        }

        weight_factors = {
            "Gramm": 0.001,
            "Dekagramm": 0.01,
            "Kilogramm": 1,
            "Tonna": 1000
        }

        # Mennyiség váltó típusának kiválasztása
        if selected_converter.get() == "Hossz":
            factors = length_factors
        elif selected_converter.get() == "Térfogat":
            factors = volume_factors
        elif selected_converter.get() == "Tömeg":
            factors = weight_factors
        else:
            raise ValueError("Nem támogatott átváltó típus!")

        # Műveletek
        from_factor = factors[from_unit]
        to_factor = factors[to_unit]
        result = value * (from_factor / to_factor)
    except ValueError:
        print("Adjon meg egy számot!")
        return
#végösszeg kerekítése, nullázása, "readonly" funkció
    result = round(result, 8)
    bevitel.config(state="normal")
    bevitel.delete(0, END)
    bevitel.insert(0, result)
    bevitel.config(state="readonly")

# Frame a különböző átváltókhoz
def update_converter(selected_converter):
    for widget in converter_frame.winfo_children():
        widget.grid_forget()

#bemeneti mezők pozícionálása keretrendszerben
    bemenet.grid(column=0, row=0, padx=10, pady=5)
    bevitel.grid(column=0, row=1, padx=10, pady=5)
    drop.grid(column=1, row=0, padx=10, pady=5)
    drop2.grid(column=1, row=1, padx=10, pady=5)
    calculate_button.grid(column=1, row=2, pady=10)

    if selected_converter == "Hossz":
        options = length_options
    elif selected_converter == "Térfogat":
        options = volume_options
    elif selected_converter == "Tömeg":
        options = weight_options
    else:
        return

    drop["menu"].delete(0, "end")
    drop2["menu"].delete(0, "end")
    for option in options:
        drop["menu"].add_command(label=option, command=tk._setit(clicked, option))
        drop2["menu"].add_command(label=option, command=tk._setit(clicked2, option))
    clicked.set(options[0])
    clicked2.set(options[0])

# Konzolalkalmazás alapjai
root = tk.Tk()
root.minsize(width=500, height=250)
root.title("Átváltó Program")
root.config(padx=40, pady=50, background="white")

# Átváltó lehetőségek
options = ["Válasszon egy átváltót", "Hossz", "Térfogat", "Tömeg"]
selected_converter = StringVar()
selected_converter.set(options[0])

#főoldal alapbeállítása, pozícionálása
main_menu = OptionMenu(root, selected_converter, *options, command=update_converter)
main_menu.grid(row=0, column=0, padx=10, pady=10)

converter_frame = Frame(root)
converter_frame.grid(row=1, column=0, padx=10, pady=10)

bemenet = tk.Entry(converter_frame)
bevitel = tk.Entry(converter_frame)
bevitel.config(state="readonly")

# Mérték lehetőségek
length_options = ["Milliméter", "Centiméter", "Méter", "Kilométer"]
volume_options = ["Milliliter", "Centiliter", "Liter", "Köbméter"]
weight_options = ["Gramm", "Dekagramm", "Kilogramm", "Tonna"]

clicked = StringVar()
clicked.set(length_options[0])  # alapértelmezett mértékegység a legördülő menüben

drop = OptionMenu(converter_frame, clicked, *length_options)
clicked2 = StringVar()
clicked2.set(length_options[0])

drop2 = OptionMenu(converter_frame, clicked2, *length_options)

calculate_button = Button(converter_frame, text="Átszámítás", command=convert_units)

root.mainloop()
