print("Welcome to the Tip calculator!")
total=float(input("What was the total bill? "+"$s"))
people=float(input("How many people to split the bill? "))
p_tip=int(input("What percentage tip you would you like to give? 10, 12, or 15? "))
tip=round((total/people)*(1+p_tip/100),1)
print("Each person should pay: "+ "$"+str(tip))


