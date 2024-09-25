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
print("Project Importance (Urgent, High, Medium, Low):")

projectImportance = input("--> ")
print("Due Date: ")

dueDate = input("--> ")
print("Number of Prints on Plate: ")

printQuantity = input("--> ")
print("Ordering Person: ")

projectTeacher = input("--> ")
print("What is the price of the part")

printPrice = float(input("-> "))  # Convert input to float immediately
print("Estimated time to print: ")

print("How many colors will be used? (1-4)")
colorPrice = float(input("-> "))  # Convert input to float immediately

print("How long will it take to print (in mins)")
timePrice = float(input("-> "))  # Convert input to float immediately

print("Color of filament: ")
projectColor = input("--> ")

print("Notes: ")
projectNotes = input("--> ")

print("EXAMPLE PRINT")
print(projectName)
print("Importance: " + projectImportance)
print("Due Date: " + dueDate)
print("Number of Prints: " + printQuantity)
print("Ordering Teacher: " + projectTeacher)
print("Color of filament: " + projectColor)
print("Notes: " + projectNotes)

print("Is this correct? (y/n)")
correct = input("--> ")

if correct == "y":
    # Calculate costs
    finalPrintPrice = printPrice * 85
    finalColorPrice = colorPrice * 2
    finalTimePrice = timePrice / 8

    goldCost = finalPrintPrice + finalColorPrice + finalTimePrice

    # Round the total cost to 1 decimal place using the built-in round function
    roundGoldCost = round(goldCost, 1)

    # Output the result
    print(f"This print will cost {roundGoldCost} gold.")
    print("Printing...")
    current_time = time.strftime('%I:%M:%S %p')
    current_Date = time.strftime('%a %b %d %Y')

    # Printing to the thermal printer
    printer.bold = True
    printer.size = adafruit_thermal_printer.SIZE_LARGE
    printer.print("Print Estimate")
    printer.feed(1)
    
    printer.size = adafruit_thermal_printer.SIZE_SMALL
    printer.print("Importance: " + projectImportance)
    printer.print("Due Date: " + dueDate)
    printer.print("Number of Prints: " + printQuantity)
    
    printer.bold = False
    printer.feed(1)
    printer.print("Ordering Person: " + projectTeacher)
    printer.print(f"Estimated time to print: {timePrice}")
    printer.print("Color of filament: " + projectColor)
    printer.feed(1)
    
    printer.feed(1)
    printer.print(f"TOTAL ESTIMATED GOLD: {roundGoldCost}")
    printer.feed(1)
    printer.print(f"Real World Cost: ${printPrice}")
    printer.print(f"Cost For Colors: {finalColorPrice}")
    printer.feed(1)
    printer.print(f"Cost for Time: {finalTimePrice}")

    printer.print("Notes: ")
    printer.print(projectNotes)
    printer.feed(1)
    printer.print("Ticket Created: ")
    printer.print(current_time)
    printer.print(current_Date)
    printer.feed(3)
else:
    print("Restarting...")
    exit()

print("Would you like to print bill of sale now (y/n)")
correct = input("--> ")

if correct == "y":
    printer.bold = True
    printer.size = adafruit_thermal_printer.SIZE_LARGE
    printer.print("Bill of Sale")
    printer.feed(1)
    printer.size = adafruit_thermal_printer.SIZE_LARGE
    printer.print("Browntown Carriage and Shipwrights")
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
    printer.feed(4)
