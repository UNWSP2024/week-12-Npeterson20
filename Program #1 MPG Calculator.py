import tkinter as tk
from tkinter import messagebox

def calculate_mpg():
    try:
        gallons = float(entry_gallons.get())
        miles = float(entry_miles.get())
        mpg = miles / gallons
        messagebox.showinfo("MPG Result", f"Your car's MPG is: {mpg:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for gallons and miles.")

# GUI Setup
root = tk.Tk()
root.title("MPG Calculator")

tk.Label(root, text="Gallons of Gas:").grid(row=0, column=0, padx=10, pady=5)
entry_gallons = tk.Entry(root)
entry_gallons.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Miles Driven:").grid(row=1, column=0, padx=10, pady=5)
entry_miles = tk.Entry(root)
entry_miles.grid(row=1, column=1, padx=10, pady=5)

btn_calculate = tk.Button(root, text="Calculate MPG", command=calculate_mpg)
btn_calculate.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
