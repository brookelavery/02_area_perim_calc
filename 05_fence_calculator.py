# functions go here

# checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:
        
        error = "Please enter a number that is more than zero"
        
        try:
        
            # ask user to enter a number
            response = float(input(question))
            
            # checks number is more than zero
            if response > 0:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error)    
    


# Main Routine goes here

# Introduction / Heading print statements
print()
print("**** Fence Cost Calculator *****")
print()

# Start of calculator loop
keep_going = ""
while keep_going == "":

    # call your number checker function three times to get the 
    # width, length and cost_per_m of the fencing
    width = num_check("Width: ")
    height = num_check("height: ")
    price_metre = num_check("price per metre: ")
    print("replace me with input statements")

    # Calulate perimeter (width + height) x 2
    perimeter = 2 * (width + height)
    # Calculate the cost of the fencing (perimeter x price / meter)
    fencing = perimeter * price_metre 
    # Output the perimeter and cost of the fencing
    print("perimeter: {:.2f}m".format(perimeter))
    print("cost: ${:.2f} ".format(fencing))
    print()
    
    keep_going = input("Press <enter> to keep going or any key to quit")
    
print()
print("Thanks for using the Fencing cost calculator")

        
    
    