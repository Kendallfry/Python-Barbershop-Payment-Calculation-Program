'''
Programmer            :  Kendall Fry
Date of Submission    :  5/1/26
Course                :  CIS 245 -  Principles of Software Development
Instructor            :  Charles McSweeney
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Below is a neccessary code for the Hair Force barbershop/salon revenue trackng app.
The program predefines names of services as well as the prices for each service.
There is a pre-set list of stylist names defined within the program which represents the employees of Hair Force.
This program will Ggenerate a weekly report for money earned by each stylist based upon the amount of services they completed, in addition to tips earned. 
Each week, all stylist's must pay the owner, Slim, 50% of their total revenue as well as a weekly booth rental of $100. Tips a stylist receives is 100% theirs to keep.
If revenue adds to ever $100 the stylist keeps half of whatever is left as well as tips to them. 
If revenue does not add to at least $100, the stylist must still pay Slim at least 100$ for the week. 
After all revenue for a stylist is calculated , the weekly report will show how much the owner is owed and how much each stylist is owe, or owes.
The program will loop through services completed for each stylist (5 in total), and end once the last stylist report has been generated.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''




# Function 1 - Define Services and Service Price

#This portion of the function stores the service names in a list numbered 0-11
def get_service():
    service_names = [
        "Haircut",
        "Child's Haircut",
        "Hair-coloring",
        "Child's Hair-coloring",
        "Perm",
        "Child's perm",
        "Hair weave extension",
        "Child's hair weave extension",
        "Hair braiding",
        "Child's hair braiding",
        "Hair repair"
        "Child's hair repair"
    ]

#This portion of the function stores the service prices in a list, also numbered 0-11. The position of each price will match up
#with the postition of each service name. There are 12 Service names and 12 service prices. 
#So a "Haricut"(0) is 25.00(0), "hair-coloring"(1) is 70.00(1), and this continues for each item in each list. 
    service_prices = [25.00, 15.00, 70.00, 50.00, 65.00, 55.00, 150.00, 120.00, 125.00, 100.00,  75.00, 55.00]

#The return tag sends the list back to where the fuction was called from. 
    return service_names, service_prices

# Function 2 - Get Services Done. This function asks how many of each service was done
# It utilizes the "service_names" list which will be used to get an amount of the number of services done. 
def get_services_done(service_names):
    
    #Below an empty list is created 
    quantities = []

    # This will print an instruction for the user on a new line
    print("\nEnter how many of each service the stylist completed:\n")

    # Below is a loop that will go through each service name, one at a time. 
    # The 1st loop will be for "Haircut", the second for "Hair-coloring", third for "Perm", and so on.
    for service in service_names:

        # Will ensure that the number input is positive and whole and keeps asking until so.
        while True:
            try:
                # This converts the input into an intiger and includes the service name >>> (f"{service}:)
                amount = int(input(f"{service}: "))

                # This ensure a positive number in input and sends an error if a negative number is input
                if amount < 0:
                    print("Please enter 0 or a positive number.")

                # Once an acceptable number is input, quantaties.appened will add that number to the "quantaties" list in order from 1-12 (0-11)
                else:
                    quantities.append(amount)

                    # This break exits the loop and moves to the next service in the list to start the loop again. 
                    break

                # This will throw an error if something other than a positive whole number, such as letter or symbols, are entered.
                # This will prevent the program from crashing
            except ValueError:
                print("You must enter a whole number.")

    # After all quantaties are entered, this will return the now comptleted quantaties list
    return quantities

# Function 3 - Get Tips. This function asks for tips given
# Tips are seperate because they go directly to the stylist
def get_tips():

    # Will ensure that the number input is positive and keeps asking until so.
    while True:

        # The input below accepts numbers with a decimal as a tip can include change
        # An error will be thrown is a negetive number is input
        try:
            tips = float(input("\nEnter the total amount of tips received for stylist: $"))
            if tips < 0:
                print("Tips must be a positive number.")

            # Returns tips once all valid inputs are included
            else:
                return tips
            
        # This will throw an error if something other than a positive float number, such as letter or symbols, are entered.
        except ValueError:
            print("Tips entered must be a number.")

# Function 4 - Calculate Service Total. This calculates total sales
def calculate_service_total(quantities, prices):

    # The total starts at 0 and will be added up as the program loops
    total = 0

    # len(quantities) gets the number of items in the quantities list.
    # range(len(quantities)) creates index numbers. If there are 12 services, i becomes 0, 1, 2, 3, 4, 5, etc.

    for i in range(len(quantities)):

        # Total is redefined by adding the sum of each service quantatiy * services prices
        # If the the 1st quantaty is 2, for haircuts, then it would add 2 * 25 (50) to total
        # This will happen for each service
        total = total + quantities[i] * prices[i]

    #Total is returned
    return total

# Function 5 - Calculate Payment. This function will calculate the owner (Slim) and stylist shares.
def calculate_payment(service_total, tips):

    # This defines owners share as %50 of what the stylist generates for revenue
    owner_share = service_total * 0.50

    # The max() attribute, will define owner_amount with the largest  number (max) in the parenthesis
    # This ensures that the owner will recieve the minimum of $100 per week
    owner_amount = max(owner_share, 100)

    # The stylist gets whatever service money is left, after the owner amount is taken out.
    stylist_take_home_total = service_total - owner_amount

    # Tips are added because tips go directly to the stylist.
    stylist_total_plus_tips = stylist_take_home_total + tips

    # Owner and stylist take home pays are returned
    return owner_amount, stylist_total_plus_tips

# Function 6 - Print Report. This function will print a final report of the weeks revenue and share spilts
def print_report(stylist_name, service_names, prices, quantities,
                 tips, service_total, owner_amount, stylist_total_plus_tips):

    # This line prints a n= sign 50 times to create a line across the page for better visual
    print("\n" + "=" * 50)
    print("Hair Force Stylist Weekly Income Report")
    print("=" * 50)

    # The stylist name is printed here
    print(f"Stylist Name: {stylist_name}\n")

    # This loop goes through each service and prints the name, quantity, price, and line total for each service that was done.
    # It will only print if the service done has a value of at least 1.
    print("Services Provided:\n")
    for i in range(len(service_names)):
        if quantities[i] > 0:

            # For services that were done, the line total is calculated by multiplying the quantity of that service by the price of that service.
            line_total = quantities[i] * prices[i]

            # Prints service name, quantity and price up to 2 decimal points. 
            print(f">>> {service_names[i]} {quantities[i]} x ${prices[i]:.2f} = ${line_total:.2f}\n")

     # This line prints an = sign 50 times to create a line across the page for better visual
    print("\n" + "-" * 50)

    # Total sales, tips, owner amount, and stylist amount due is printed below up to 2 decimal places.  
    print(f"Total Service Sales:             ${service_total:.2f}")
    print(f"Total Tips:                      ${tips:.2f}")
    print(f"Slim Amount Due:                ${owner_amount:.2f}")
    print(f"Stylist Final Amount Due:        ${stylist_total_plus_tips:.2f}")

    #The line below uses absolute value to display a positive number owed to the Owner, despite the result being negative. This is for a better visual of money owed. 
    if stylist_total_plus_tips < 0:
        print(f"\nStylist owes Slim:              ${abs(stylist_total_plus_tips):.2f}")
    else:
        print(f"\nStylist will receive:           ${stylist_total_plus_tips:.2f}")

    print("=" * 50)

# Main Function. This is basically the control center of the program
# This function manages teh secwuence of all of my other functions. It ensures
# that the program exectes everything in a logical order.
def main():

    # This calls get_service() to retrieve service names and prices
    service_names, service_prices = get_service()

    # Define a list of the shop's stylist names
    stylist_names = ["Moon", "Brandon", "Wendy", "Kesha", "Ced"]

    # Loop through each stylist and prints thier name above report indicating who's report it is. 
    for stylist_name in stylist_names:
        print(f"\nEntering information for {stylist_name}")

        # Call get_services_done() to collect how many of each service was performed
        quantities = get_services_done(service_names)

        # Call get_tips() to collect total tips earned by the stylist
        tips = get_tips()

        # Call calculate_service_total() to compute total revenue from services completed
        service_total = calculate_service_total(quantities, service_prices)

        # Call calculate_payment() to determine Slim's share and his stylist's earnings
        owner_amount, stylist_total_plus_tips = calculate_payment(service_total, tips)

        # Call print_report() to display the final report for each stylist
        print_report(stylist_name, service_names, service_prices, quantities,
                    tips, service_total, owner_amount, stylist_total_plus_tips)

#This runs all of the functions created allowing the program to run.
main()

