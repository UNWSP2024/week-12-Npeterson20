import tkinter as tk
from tkinter import messagebox

# Services and their prices
services = {
    "Oil Change": 30.00,
    "Lube Job": 20.00,
    "Radiator Flush": 40.00,
    "Transmission Fluid": 100.00,
    "Inspection": 35.00,
    "Muffler Replacement": 200.00,
    "Tire Rotation": 20.00,
}

def calculate_total():
    total = 0
    for service, var in service_vars.items():
        if var.get():
            total += services[service]
    messagebox.showinfo("Total Charges", f"The total is: ${total:.2f}")

# GUI Setup
root = tk.Tk()
root.title("Joe's Automotive")

tk.Label(root, text="Select Services:").grid(row=0, column=0, padx=10, pady=5)

service_vars = {}
row = 1
for service, price in services.items():
    var = tk.BooleanVar()
    tk.Checkbutton(root, text=f"{service} - ${price:.2f}", variable=var).grid(row=row, column=0, sticky='w', padx=10)
    service_vars[service] = var
    row += 1

btn_calculate = tk.Button(root, text="Calculate Total", command=calculate_total)
btn_calculate.grid(row=row, column=0, pady=10)

root.mainloop()
