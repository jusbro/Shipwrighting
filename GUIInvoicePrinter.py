import tkinter as tk
from tkinter import messagebox
import serial
import adafruit_thermal_printer
import random

# -----------------------------
# PRINTER SETUP
# -----------------------------
uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)
printer = ThermalPrinter(uart)

# -----------------------------
# SLOGANS
# -----------------------------
slogans = [
    "Masters of Carriage and Craft, Purveyors of the Finest Works",
    "By Hand and Hammer, We Forge Thy Journey",
    "For Vessels of Land and Sea, Crafted with Diligence and Care",
    "From Timber to Iron, Conveyance to Sail, We Build for Every Voyage",
    "In Service of Thy Travel, Built Strong and True",
    "Where Craft and Precision Meet for Thy Grandest Journeys",
    "For Ye Who Seek Quality in Carriage and Vessel Alike",
    "Bound by Tradition, Forged for Adventure",
    "From Shore to Road, Our Craft Be Thy Steadfast Companion",
    "Honoring the Craft, Building for the Bold"
]

# -----------------------------
# PRINT FUNCTION
# -----------------------------
def print_bill():
    project_name = project_entry.get()
    purchaser_name = purchaser_entry.get()
    gold_cost = cost_entry.get()

    if not project_name or not purchaser_name or not gold_cost:
        messagebox.showerror("Error", "All fields must be filled out.")
        return

    try:
        float(gold_cost)  # validate number
    except ValueError:
        messagebox.showerror("Error", "Gold cost must be a number.")
        return

    # Printing
    printer.bold = True
    printer.double_height = True
    printer.size = adafruit_thermal_printer.SIZE_LARGE
    printer.print("Bill of Sale")
    printer.feed(1)

    printer.size = adafruit_thermal_printer.SIZE_MEDIUM
    printer.print("Browntown Carriage & Shipwrights")
    printer.feed(1)

    printer.size = adafruit_thermal_printer.SIZE_SMALL
    printer.print(random.choice(slogans))
    printer.feed(2)

    printer.bold = True
    printer.print(f"Project: {project_name}")
    printer.feed(1)
    printer.print(f"Final Price in Gold: {gold_cost}")
    printer.feed(1)
    printer.print("Procurer: " + purchaser_name)
    printer.feed(1)
    printer.print("x___________________")
    printer.feed(3)
    printer.print("Purveyor: Sir Brown, Master of Transportation")
    printer.feed(1)
    printer.print("x___________________")
    printer.feed(2)

    printer.print("Let it be known by this present document, that this writ serveth")
    printer.print("as a Bill of Sale and Covenant betwixt the Procurer and the")
    printer.print("Purveyor, for the exchange of the agreed upon sum of gold.")
    printer.feed(1)

    printer.print_barcode('123456789012', printer.UPC_A)
    printer.feed(4)

    messagebox.showinfo("Success", "Bill of Sale Printed Successfully.")

# -----------------------------
# GUI SETUP
# -----------------------------
root = tk.Tk()
root.title("Gold Cost Estimate Management System")
root.geometry("400x300")

tk.Label(root, text="Gold Cost Estimate Management System", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Name of Project:").pack()
project_entry = tk.Entry(root, width=40)
project_entry.pack(pady=5)

tk.Label(root, text="Name of Purchaser:").pack()
purchaser_entry = tk.Entry(root, width=40)
purchaser_entry.pack(pady=5)

tk.Label(root, text="Price of Part (Gold):").pack()
cost_entry = tk.Entry(root, width=40)
cost_entry.pack(pady=5)

print_button = tk.Button(root, text="Print Bill of Sale", command=print_bill)
print_button.pack(pady=20)

root.mainloop()
