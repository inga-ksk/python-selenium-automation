# DESCRIPTION:
# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

input_number = input("Please enter a random non-negative number: ")
list1 = []
for i in input_number:
    list1.append(i)
list1.reverse()
print(list1)