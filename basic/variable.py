a = 10
b = 5
print(a + b)  # result will print 15 here
a = 10.5  # float number
print(b + a)  # now print 15.5 here
# and varial a is a float type variable
print(type(a))  # print <class 'float'>
print(type(b))  # print <class 'int'>
name = 'String type'
print(type(name))  # <class 'str'>

# if we want to find any variable class type then
# we use this type() methods and in type method we pass
# our desire variable

name = 'University'
print(name[1:5])  # print nive
#   thats mean it will print name[1] to name[5] index number character
print(name[:3])  # print Uni

print(name[-3])  # print i

print(name[:-3])  # print Univers
# thats means it will minus index from the last and all of the index
# will print without the last
# it will print from Zero to (last_index-3)
# important things if any index is not found then it will show a IndexError: string out of range
# print(name[15])
#   we also acces any string variable like this way   varname[index]


price = 10
# number 10 is decemal number
# for printing 10 to convert it to binary then computer store it
print(price)  # output: 10

# boolean type
is_published = False  # python is case sensitive
print(is_published)

# Example : We check in a patient nammed Jhon Smith.
# He is 20 years old and is a new patient

# solution:
patient_name = 'Jhon smith'
patient_age = 20
is_new_patient = True

print("Patient Name: " + patient_name + " \nPatient Age: " + str(patient_age))
print("Is patient new: " + str(is_new_patient))

#
course = 'Python for beginners'

print(course[0:4])  # print Pyth
print(course[:-1])  # print: Python for beginner *missing s is the last index
name = 'Jennifer'
print(name[1:-1])  # print: ennife

# formatted string
first = 'Jhon'
last = 'Smith'
message = first + ' [ ' + last + ' ] is a coder!'
msg = f'{first} [ {last} ] is a coder!' # dynamically insert value in string
print(message)
print(msg)

# string length
print(len(course)) # print: 20
# string lowwer case
print(course.lower())
# string Upper case
print(course.upper())   # print:PYTHON FOR BEGINNERS
# find a character in string
print(course.find('O')) # print: -1 because -1 means nothing found
print(course.find('o')) # print: 4 means  o found in index number 4
# replace a character to another
print(course.replace('P', 'J')) # note down it cannot change the original One
print(course)
# find existing a sequence
print('Python' in course)   # print: True
print('python' in course)   # print: False

# len , upper(), lower(), find(), replace, in operator
