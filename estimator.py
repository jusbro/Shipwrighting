#Software for make glorious estimates of interdepartmental Shipcrafting
#Version 0.9 9/25/2024
#This program allows the estimated gold costs of 3D printed ships, carts, artwork, etc. 
#It is designed to be run in a terminal instance of Python3
#Please feel free to submit any bugs or concerns to the trashcan

#Import CSV for database management
import csv

#Import datetime for date stamping in database
from datetime import datetime

#Create or initialize the CSV file that stores the data of the projects
database_file_name = "estimates_database.csv"

#Begin collecting data about the project
print("Purchaser's First Name:")
buy_first_name = input("-> ")

print("Purchaser's Last Name:")
buy_last_name = input("-> ")

print("What objects are being printed, include quantity for each type of item")
build_notes = input("->")

print("What is the real-world cost of this print:")
real_world_cost = float(input("-> "))

#Collect print time and convert to minutes
while True:
    try:
        print("How long will this print take:")
        hours_print =   int(input("   (HOURS ex '1')-> "))
        minutes_print = int(input("(MINUTES ex '36')-> "))
    except:
        print("Invalid number, please use whole numbers")
    try:
        converted_time_print_minutes = (hours_print * 60) + minutes_print
        break
    except:
        print("time conversion failed, please try again!")
print(f"Converted time in minutes: {converted_time_print_minutes}")

print("\nHow Many Colors are requested:")
num_color_choice = int(input("->"))

print("How many of the colors are 'premium':")
num_premium_filament = int(input("->"))

print("What colors are being used:")
colors_list = input("->")

#determine if a requested 4x surcharge for ships is applicable
while True:
    print("\nDoes this print contain a ship?")
    ship_choice = input("(y/n) ->")
    if ship_choice == "y":
        ship_surcharge = True
        break
    elif ship_choice == "n":
        ship_surcharge = False
        break
    print("Invalid selection, please use 'y' or 'n'")

#calculate a supply and demand multiplier. This is applied as a % that is either added or subtracted (+4 would add a 40% tax essentially)
print("\n\nSupply and Demand Multiplier:")
print("whole-number scale between -4 to +4:")
print("This adjusts base and time costs")
print("-4 is maximum reduction and +4 is maximum upcharge")
supp_demand_multiplier_input = int(input(" -> "))

#Calculate an estimate cost in gold
#Equation is based on the real-world cost of the print, the time of the print (in mins), and number of colors selected
calc_print_price = real_world_cost * 85
calc_time_price = converted_time_print_minutes / 8
calc_prem_fila_price = num_premium_filament * 80
calc_num_fila_colors_price = num_color_choice * 10

calc_final_estimate = calc_print_price + calc_time_price + calc_prem_fila_price + calc_num_fila_colors_price

#calculate a ship surcharge if applicable 
if ship_surcharge == True:
    calc_ship_surcharge = calc_final_estimate * 4
    calc_final_estimate = calc_final_estimate + calc_ship_surcharge
else:
    calc_ship_surcharge = 0

#calculate supply and demand multiplier total
#part 1: calculate percentage
calc_supp_demand_perc = supp_demand_multiplier_input / 10
#part 2: Apply percentage to find total surcharge
calc_supp_demand_perc = calc_supp_demand_perc * calc_final_estimate
#part 3: Add surcharge to final cost
calc_final_estimate = calc_final_estimate + calc_supp_demand_perc

#Print estimate to terminal for review
print("\n\nEstimated Cost Breakdown:")
print(f"\n                  Base Cost: {calc_print_price}")
print(f"                  Time Cost: {calc_time_price}")
print(f" Premium Filament Surcharge: {calc_prem_fila_price}")
print(f" Multicolor Print Surcharge: {calc_num_fila_colors_price}")
print(f"             Ship Surcharge: {calc_ship_surcharge}")
print(f"Supply and Demand Surcharge: {calc_supp_demand_perc}")
print(f"\n  Final Print Cost Estimate: {calc_final_estimate}")

#Get current timestamp for use in printing service and database collections
now = datetime.now()
# Format it as "MM/DD/YY HH:MM AM/PM"
date_now = now.strftime("%m/%d/%y %I:%M %p")

#Printing service for estimate
print("\n\n Would you like to print estimate? (y/n)")
print_est_choice = input("->")
if print_est_choice == "y":
    print("This will lead to the printing service in a future update")

#Storing Estimate in database
print("Would you like to save this estimate for future reference (y/n)")
store_estimate_choice = input("->")
if store_estimate_choice == "y":
    print("Saving estimate to database...")


    # Open the CSV file and write a new line
    with open(database_file_name, mode='a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write the data: first name, last name, objects printed, and costs
        csv_writer.writerow([
            buy_first_name,
            buy_last_name,
            date_now,
            build_notes,
            f"color(s):{colors_list}",
            f"print_price:{calc_print_price}",
            f"time_price:{calc_time_price}",
            f"premium_fila:{calc_prem_fila_price}",
            f"filament_num_cost:{calc_num_fila_colors_price}",
            f"ship_surcharge:{calc_ship_surcharge}",
            f"supp/demand_surch:{calc_supp_demand_perc}",
            f"final_cost:{calc_final_estimate}"
        ])

    print("Estimate saved to database.")
print("\n\nEstimate Completed, program closing")
