import math

print("Choose either 'investment' or 'Bonds' from the menu below to proceed : ")
print(" ")
print(" ")

print("Investment -              To calculate the amount of interest you'll earn on interest")
print("Bond       -              To calculate the amount you will have to pay on a home loan")
print(" ")
print(" ")

#Ask question, convert answer to lower case
selection = input("Proceed with 'Investments' or 'Bonds'? : ") .lower()
print(" ")

#store possible answers as lower case
investments = "investments"
bonds = "bonds"
simple = "simple"
compound = "compound"


#create if statements for bonds and ask questions if selected
#spacing between questions 
#perform calculations
#print monthly payments and round up to make reading easier and simple

if selection == bonds :
    current_value = float(input("Enter current value of house in Rands (R): "))

    print(" ")
    int_rate = float(input("What is the interest rate in '%'? : "))
    i = int_rate / 100

    print(" ")
    num_of_months = int(input("How many months do you want to repay the bond? : "))
    print(" ")

    monthly_payments = math.ceil((i/12 * current_value)/(1 - math.pow((1+i/12),(-num_of_months)))) 
    print("Your monthly payments are R{}".format(monthly_payments))
    print(" ")

#create statement for investments and ask questions if selected
#perform calculations
#print earnings 

elif selection == investments :
    deposit = float(input("How much money are you depositing in Rands (R)? : "))
    print(" ")
    int_rate = float(input("What is the interest rate in '%'? : "))
    print(" ")
    num_of_years = int(input("How many years are you investing for? : "))
    print(" ")
    print(" Answer using 'simple' or'compound' : ")
    print(" ")
    interest = input("Simple interest or compound interest? ") .lower()
    print(" ")


#nest if statement if users selects simple or compound interest
 #perform calculations   
    if interest == simple:
        final_simp_amount = math.ceil(deposit * (1 + (int_rate / 100) * num_of_years))

        print("Your total amount is R{}" .format(final_simp_amount))
        print(" ")

    elif interest == compound :
        final_comp_amount =math.ceil( deposit * math.pow((1+(int_rate/100)) , num_of_years))

        print("Your total amount is R{}" .format(final_comp_amount))
        print(" ")

#only allow for simple or compund as answers 
    else :
        raise ValueError("Please enter Simple or Compound")

    
#only allow for investments or bonds as answers
else :
    raise ValueError ("Please enter Investments or Bonds")







    







    



