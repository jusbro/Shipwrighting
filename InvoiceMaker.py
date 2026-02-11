import serial
uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
import adafruit_thermal_printer
import time
import random

ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)

printer = ThermalPrinter(uart)

print("Gold Cost Estimate Management System")
print("Version 1.0")
print()
print("Name of project: ")
projectName = input("--> ")

print("Name of purchaser: ")
projectTeacher = input("--> ")

print("What is the price of the part")
roundGoldCost = input("-->")


print("Would you like to print bill of sale now (y/n)")
correct = input("--> ")

if correct == "y":
    printer.bold = True
    printer.double_height = True
    printer.size = adafruit_thermal_printer.SIZE_LARGE
    printer.print("Bill of Sale")
    printer.feed(1)
    printer.size = adafruit_thermal_printer.SIZE_MEDIUM
    printer.print("Browntown Carriage & Shipwrights")
    printer.feed(1)
    printer.size = adafruit_thermal_printer.SIZE_SMALL
    slogan_num = random.randint(0,10)
    if slogan_num == "1":
        printer.print("Masters of Carriage and Craft, Purveyors of the Finest Works")
    if slogan_num == "2":
        printer.print("By Hand and Hammer, We Forge Thy Journey")
    if slogan_num == "3":
        printer.print("For Vessels of Land and Sea, Crafted with Diligence and Care")
    if slogan_num == "4":
        printer.print("From Timber to Iron, Conveyance to Sail, We Build for Every Voyage")
    if slogan_num == "5":
        printer.print("In Service of Thy Travel, Built Strong and True")
    if slogan_num == "6":
        printer.print("Where Craft and Precision Meet for Thy Grandest Journeys")
    if slogan_num == "7":
        printer.print("For Ye Who Seek Quality in Carriage and Vessel Alike")
    if slogan_num == "8":
        printer.print("Bound by Tradition, Forged for Adventure")
    if slogan_num == "9":
        printer.print("From Shore to Road, Our Craft Be Thy Steadfast Companion")
    if slogan_num == "10":
        printer.print("Honoring the Craft, Building for the Bold")
    printer.bold = True
    printer.feed(2)
    printer.print(f"Final Price in Gold: {roundGoldCost}")
    printer.feed(1)
    printer.print("Procurer: "+ projectTeacher)
    printer.feed(1)
    printer.print("x___________________")
    printer.feed(3)
    printer.print("Purveyor: Sir  Brown, Master of Transporation")
    printer.feed(1)
    printer.print("x___________________")
    printer.feed(3)
    printer.print("Let it be known by this present document, that this writ serveth as a Bill of Sale and Covenant betwixt the Procurer and the Purveyor, to wit, for the exchange of the agreed upon sum of gold herein aforelisted")
    printer.feed(1)
    printer.print_barcode('67', printer.UPC_A)
    printer.feed(4)
