def calculate_tip(bill_amount, tip_percentage):
    tip = bill_amount * tip_percentage * .01
    return tip


def total_bill(tip, bill_amount):
    total = tip + bill_amount
    return total


def split_bill(bill_amount, num_ppl):
    total = bill_amount / num_ppl
    return total

# tip = calculate_tip(36, 15)
# print "The tip is" + str(tip)
# total_bill = total_bill(tip, 36)
# print "The total is" + str(total_bill)
# print "Everyone owes" + str(split_bill(total_bill, 4))

# print "The tip is" , tip

print "hi"


def main():
    menu = raw_input("What would you like to do? Type 1 to calculate tip or 2 to split the bill: ")
    if menu == "1":
        bill = float(raw_input("What is the original bill amount? "))
        tip = float(raw_input("What percent tip would you like to put? "))
        total = bill + calculate_tip(bill, tip)
        print "The total tip will be:", calculate_tip(bill, tip)
        print "The total bill will be: ", total
        split = raw_input("Would you like to have the bill split? Type Y or N: ").lower()
        if split == "y":
            ppl = float(raw_input("Amongst how many people? "))
            splitted = total / ppl
            print "Everyone owes ", splitted
        else:
            print "You owe all", total
    else:
        total = float(raw_input("what is the total amount?"))
        people = int(raw_input("How many people are you splitting between?"))
        splitted = total / people
        print splitted

if __name__ == '__main__':
    main()
