#Software for make glorious estimates of interdepartmental Shipcrafting
#Version 0.9 9/25/2024
#This program allows the estimated gold costs of 3D printed ships, carts, artwork, etc. 
#It is designed to be run in a terminal instance of Python3
#Please feel free to submit any bugs or concerns to the trashcan

while True:
    try:
        print("\nWhat is the real-world cost of this print:")
        real_world_cost = float(input("-> "))
        break
    except:
        print("Provide a number, dingus...")
#Collect print time and convert to minutes

while True:
    try:
        print("\nHow long will this print take:")
        hours_print =   int(input("   (HOURS ex '1')-> "))
        minutes_print = int(input("(MINUTES ex '36')-> "))
    except:
        print("Invalid number, please use whole numbers")
    try:
        converted_time_print_minutes = (hours_print * 60) + minutes_print
        break
    except:
        print("time conversion failed, please try again!")
print(f"\nConverted time in minutes: {converted_time_print_minutes}")

while True:
    try:
        print("\nHow Many Colors are requested:")
        num_color_choice = int(input("->"))
        break
    except:
        print("Provide a number, dingus...")

while True:
    try:
        print("\nHow many of the colors are 'premium':")
        num_premium_filament = int(input("->"))
        break
    except:
        print("Provide a number, dingus...")


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
print("\nwhole-number scale between -4 to +4:")
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
print(f"\n                  Base Cost: {round(calc_print_price)}")
print(f"                  Time Cost: {round(calc_time_price)}")
print(f" Premium Filament Surcharge: {round(calc_prem_fila_price)}")
print(f" Multicolor Print Surcharge: {round(calc_num_fila_colors_price)}")
print(f"             Ship Surcharge: {round(calc_ship_surcharge)}")
print(f"Supply and Demand Surcharge: {round(calc_supp_demand_perc)}")
print(f"\n  Final Print Cost Estimate: {round(calc_final_estimate)}")


print("\n\nEstimate Completed, program closing")
