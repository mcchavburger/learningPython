expenses = []
num_expenses = int(input("Enter the number of expenses you have: "))
for i in range(num_expenses):
    expenses.append(float(input("Enter the expense amount: ")))

'''
for loop can be used to add values like so, but better to use built in functions

sum = 0
for x in expenses:
    sum = sum + x

#using a comma instead of using str(sum)
#using ,sep = '' will set the default seperator to no space, if we dont have that python automatically adds a space 
print('You spent $', sum, sep = '')
'''

total = sum(expenses)
print('You spent $', total, sep = '')