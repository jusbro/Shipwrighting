print("Purchaser's First Name:")
buy_first_name = input("-> ")

print("Purchaser's Last Name:")
buy_last_name = input("-> ")

print("What is the real-world cost of this print:")
real_world_cost = float(input("-> "))

while True:
    try:
        print("How long will this print take:")
        hours_print =   int(input("  (HOURS ex '1')-> "))
        minutes_print = int(input("(MINUTES ex '36')-> "))
    except:
        print("Invalid number, please use whole numbers")
    try:
        converted_time_print_minutes = (hours_print * 60) + minutes_print
        break
    except:
        print("time conversion failed, please try again!")
print(f"Converted time in minutes: {converted_time_print_minutes}")

print("How Many Colors are requested:")
num_color_choice = int(input("->"))

print("How many of the colors are 'premium':")
num_premium_filament = int(input("->"))

while True:
    print("Does this print contain a ship?")
    ship_choice = input("(y/n) ->")
    if ship_choice == "y":
        ship_surcharge = True
        break
    elif ship_choice == "n":
        ship_surcharge = False
        break
    print("Invalid selection, please use 'y' or 'n'")

print("Supply and Demand Multiplier:")
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

#calculate a ship surcharge
if ship_surcharge == True:
    calc_ship_surcharge = calc_final_estimate * 4
    calc_final_estimate = calc_final_estimate + calc_ship_surcharge
else:
    calc_ship_surcharge = 0

print("\n\nEstimated Cost Breakdown:")
print(f"\n                 Base Cost: {calc_print_price}")
print(f"                 Time Cost: {calc_time_price}")
print(f"Premium Filament Surcharge: {calc_prem_fila_price}")
print(f"Multicolor Print Surcharge: {calc_num_fila_colors_price}")
print(f"            Ship Surcharge: {calc_ship_surcharge}")
print(f"\n Final Print Cost Estimate: {calc_final_estimate}")
