#bill wallah calculator

try:
    # Ask user to input the total bill amount
    bill = float(input("Enter the bill amount: "))
    
    # Ask for the tip percentage (e.g. 10, 15, 20)
    tip = int(input("Enter the percentage of tip. Ex: 10, 15, 20...: "))
    
    # Ask for the number of people to split the bill with
    ppl = int(input("Enter the number of people you wanna split the bill with: "))

    # Check if the bill is zero or less (maybe they’re trying to run without paying 😆)
    if bill <= 0:
        print("Do you guys wanna run away without paying the bill? XD")

    else:
        # Convert tip percentage to decimal (e.g. 15% → 0.15)
        tip_per = tip / 100
        
        # Calculate the tip amount
        tip_amt = tip_per * bill
        
        # Add tip to the original bill to get the final amount
        final_amt = bill + tip_amt
        
        # Divide final amount among number of people
        new_bill = final_amt / ppl
        
        # Show how much each person has to pay (rounded to 2 decimal places)
        print(f"Each of you have to pay ₹{new_bill:.2f}")
        print("Now, you guys can enjoy the party without heavy math. :)")

# If user enters invalid input like a string instead of a number
except ValueError:
    print("Please enter amount of bill in numbers!")

# If number of people entered is 0 → can't divide by zero
except ZeroDivisionError:
    print("If you were alone my guy, why you pulled me in? :(")

    

