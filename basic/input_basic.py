name = input('What is your name : ')
print("Your name is: " + name)
age = int(input('What is your age: '))
print("Your age is : " + str(age))

# Ask two question: persons name and person favourite color
# output: print message "Leo likes Blue"
# solution
person_name = input("Enter your name: ")
person_fav_color = input("Enter your favourite color: ")
print(person_name+" likes "+person_fav_color)

# Time and Date math
birth_year = input('Birth year: ')
print(type(birth_year)) # print data type
# age = 2019 - birth_year #this gonna error(TypeError)
age = 2019 - int(birth_year)
print(age)

# Example: Ask a user their weight(in pounds), convert it to kilogram
# and print on the terminal
weight_pounds = float(input('Enter your weight in pounds: '))
weight_kg = weight_pounds * 0.453592
print("Your weight in Kilograms: "+str(weight_kg))



