# Get Details of loan
money_owed = float(input('How much money do you owe, in £?\n'))
apr = float(input('What is the annual percentage rate of the loan?\n'))
payment = float(input("How much will you pay off each month in dollars?\n"))
months = int(input("How many months do you want to see the results for?\n"))

monthly_rate = apr/100/12

for i in range(months):
    interest_paid = money_owed*monthly_rate

    money_owed = money_owed + interest_paid

    if(money_owed - payment < 0):
        print("your last loan payment is: ", money_owed)
        print("You have paid off the loan in, ",i+1, " months", sep="")
        break
    
    money_owed = money_owed - payment

    #by default different print statements are on new lines, by using end=" " means that we use what ever end= as new seperator, in this case a space rather than new line
    print('Paid', payment, 'of which', interest_paid, ' was interest', end=" ")
    print('Now I owe', money_owed)