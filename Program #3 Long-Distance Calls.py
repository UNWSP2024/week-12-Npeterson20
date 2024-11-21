import tkinter as tk
from tkinter import messagebox

# Rate categories
rates = {
    "Daytime (6:00 AM - 5:59 PM)": 0.02,
    "Evening (6:00 PM - 11:59 PM)": 0.12,
    "Off-Peak (Midnight - 5:59 AM)": 0.05,
}

def calculate_charge():
    try:
        minutes = float(entry_minutes.get())
        rate = rates[rate_var.get()]
        charge = minutes * rate
        messagebox.showinfo("Call Charge", f"The charge for the call is: ${charge:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number of minutes.")

# GUI Setup
root = tk.Tk()
root.title("Long-Distance Calls")

tk.Label(root, text="Select Rate Category:").grid(row=0, column=0, padx=10, pady=5, columnspan=2)

rate_var = tk.StringVar(value=list(rates.keys())[0])  # Default selection
row = 1
for rate, _ in rates.items():
    tk.Radiobutton(root, text=rate, variable=rate_var, value=rate).grid(row=row, column=0, sticky='w', padx=10, columnspan=2)
    row += 1

tk.Label(root, text="Minutes:").grid(row=row, column=0, padx=10, pady=5)
entry_minutes = tk.Entry(root)
entry_minutes.grid(row=row, column=1, padx=10, pady=5)

btn_calculate = tk.Button(root, text="Calculate Charge", command=calculate_charge)
btn_calculate.grid(row=row+1, column=0, columnspan=2, pady=10)

root.mainloop()
