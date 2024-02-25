import tkinter as tk


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    km_label_out.config(text=km)


window = tk.Tk()
window.title("Miles to KM Converter")
window.config(padx=20, pady=20)

is_equal_to = tk.Label(text="is_equal_to")
is_equal_to.grid(row=1, column=0)

miles_input = tk.Entry(width=10)
miles_input.grid(row=0, column=1)
km_label_out = tk.Label(text=0)
km_label_out.grid(row=1, column=1)
button_calculate = tk.Button(text="Calculate", command=miles_to_km)
button_calculate.grid(row=2, column=1)

miles_label = tk.Label(text="Miles")
miles_label.grid(row=0, column=2)
km_label = tk.Label(text="KM")
km_label.grid(row=1, column=2)

window.mainloop()
