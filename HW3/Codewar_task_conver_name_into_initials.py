import re
full_name = str(input("Please enter your first and last name with a space between: "))
char = " "
space_index = [i.start() for i in re.finditer(char, full_name)]
def name_converter():
    print(full_name[0] + "." + full_name[(space_index[0])+1])
name_converter()




