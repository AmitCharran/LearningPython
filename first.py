print("This line will be printed")

x = 1

if x == 1:
    print("x is 1")

print("Goodbye, World")

myInt = 7
print('int test', myInt)
print('also use this ' + str(myInt))

myFloat = 7.0
print('float test ' + str(myFloat))

myString = 'string'
myString2 = "string2"
print("String test" + " " + myString + " " + myString2)

one = 1
two = 2
three = one + two
print(three)
print('\nMultiple Variable Declaration - line 27')
a, b = 2, 3
print(a + b)
a, b = 2, 'three'
# this will not work
# print( a + " " + b)
print(str(a) + " " + b)

# List
print('\n')
print('List:')
myList = []
myList.append(1)
myList.append(2)
myList.append(3)

print(myList[0]),  # prints 1
print(myList[1]),  # prints 2
print(myList[2]),  # prints 3

print('')
# prints out 1,2,3
for x in myList:
    print(x),

print("\nmyList only has 3 variables but if I try an access index outside it ex. myList[10]")
print('\tDoes not work but does not give error and does not even print the print statement')

# print('myList[10]:',myList[10])
# but nothing can execute after this


# Arithmatic Operations
print('\n\nArithmatic Operations line 57')
print('squared = 7**2: so 7 squared')
print(7 ** 2)
print("cubed = 7**3: so 7 cubed")
print(7 ** 3)

print("\nmultiplication operation on string")
string = "hello "
print('string = "hello "\nstring * 10 = ' + str(string * 10))

print("\nOperations on List - line 67")
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = even_numbers + odd_numbers
print("all_numbers= even_numbers + odd_numbers = " + str(all_numbers))
print("[1,2,3]*3 = " + str([1, 2, 3] * 3))

print("\n\nString Format")
name = "John"
print('name = "John"\n"Hello, %s!" % name')
print("Hello, %s!" % name)

name = "Jane"
last = "Doe"
age = 23
print('"hello %s %s you are %d years old" % (name,last,age)')
print("hello %s %s you are %d years old" % (name, last, age))

# printing lists
myList = [1, 2, 3]
print('"A list: %s" % myList')
print("A list: %s: " % myList)

print('"%s" = String and list \n"%d" - Integers\n"%f" - Floating Point Number\n"%.<number of digits>"fixed digits'
      '\n"%x/%X" - Integers in Hex Representation (lowercase/uppercase)')

# String Operations
print("\n\nString Operations - line 93")
print("name = " + name)
print("len(name): " + str(len(name)))
print("name.index('n'): " + str(name.index("n")))
print('name.count("a"): ' + str(name.count('a')))
print("name[1:3] :" + str(name[1:3]))
# idk what this is
# name[start:stop:step]
print("name[1:2:3] :" + str(name[1:2:3]))
print("name[::-1] :" + str(name[::-1]))
print("Getting odd index from string")
print("name[1::2] :" + str(name[1::2]))
print('name.upper() :' + name.upper())
print('name.lower() :' + name.lower())
print("name.startswith('Ja') :" + str(name.startswith('Ja')))
print('name.endswith("nadshd") :' + str(name.endswith('nadshd')))
print("name.split('n')" + str(name.split('n')))

# Booleans
print('\n\nBoolean')
print("x = 2")
x = 2
print("x == 2 : " + str(x == 2))
print("x == 3 : " + str(x == 3))
print("x < 3 : " + str(x < 3))
print("if 'in' operator - look at code line 120")
if x in [1, 2, 3, 4]:
    print("x is in list")
else:
    print("x is not in list")

if x != 2:
    print("x is not 2")
else:
    print("x is 2")

print("There's also a not operator - line 131")
print(not (x == 3))

# is myList is not empty
if myList:
    print("yes")
else:
    print("no")

# Loops/for loops
print("\n\nLoops/For Loops/While Loops - line 142")
print("For Loops")
primes = [2, 3, 5, 7, 11]
for x in primes:
    print(x),

print("")
for i in range(5):
    print(primes[i]),

print("\n\nWhile loop -- line 152")
count = 0
while count < 5:
    print("primes[%d]" % count),
    print(primes[count])
    count += 1

count = 0
print("count:"),
while True:
    print(count),
    count += 1
    if count > 5:
        break

print('')
for x in range(10):
    if x % 2 == 0:
        print(x),

print('')
for i in range(100, 200):
    if i % 10 == 0:
        print(i),

print("\n\nFunctions -- line 180")


def my_function():
    print("this is my function")


my_function()


def function2(name, greeting):
    print("%s, %s\nHow are you?" % (name, greeting))


function2(name, "hello")


def sum5(a2, b2):
    return a2 + b2


print(sum5(4, 5))

# Classes and Objects
print('\n\nClasses and Objects -- line 203')


class MyClass:
    variable = 'blah'

    def function(self):
        print("this is my function from inside class: " + self.variable)


myObjectX = MyClass()
print(myObjectX.variable)
myObjecty = MyClass()

myObjecty.variable = 'yackity'

print(myObjectX.variable)
print(myObjecty.variable)

myObjectX.function()
myObjecty.function()

# Dictionaries
# Dictionaries are similar to arrays but works with keys. It's like a SQL table
print('\n\nDictionaries -- line 224')
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print('phonebook = name: number = ' + str(phonebook))

# also can do this
phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}

print('\nCan also iterate through dictionaries -- line 238')
for name, number in phonebook.items():
    print("phone number of %s is %d" % (name, number))

# can also delete
print("\ndel phonebook['John'] \\n print(phonebook)")
del phonebook['John']
print(phonebook)
print('or... phonebook.pop("John")')


# Modules and Packages
print('\n\nModeules and Packages -- line 250')
print('Modules is python file with .py extension')
print('This is something I should learn another day')



# Numpy Arrays
print('\n\nNumpy Arrays -- line 257')
print("This gives users the opportunity to perform calculations on the entire array")

height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# import numpy package as np

import numpy as np
# create 2 numpy arrays from height to weight
np_height = np.array(height)
np_weight = np.array(weight)

print("type(np.height) = " + str(type(np_height)))
# calulate bmi
bmi = np_weight / (np_height ** 2)  # for this arrays length must match
print("bmi = np_weight / (np_height ** 2) = " + str(bmi))

print('\nNow lets do subsetting with numpy ')
print('bmi[bmi > 24] = ' + str(bmi[bmi > 24]))

print('\nConverting arrays of kg tp lbs using np -- line 278')
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
np_weight_kg = np.array(weight_kg)
np_weight_lbs = np_weight_kg * 2.2
print('Now we have the weights converted to kg to np using np\n' + str(np_weight_lbs))

# Pandas Basic DataFrame
print('\n\nPandas Basic DataFrame -- line 285')
print('\tPandas basic DataFrame is a high level manipulation tool developed by Wes McKinney.\n'
      '\tIt is built on Numpy package and its key data structure is called the DataFrame.\n'
      '\tDataFrame allows you to store tabular data in rows of observations and column variables.\n'
      '\tThere are several ways to create DataFrame.\n')

countries = {"country":['Brazil', 'Russia', "India", 'China', "South Africa"],
             'capital':["Brasilia", "Moscow", 'New Delhi', 'Beijing', "Pretoria"],
             "area":[8.516, 17.10, 3.286, 9.597, 1.221],
             "population":[200.4, 143.5, 1252, 1357, 52.98]
             }

import pandas as pd
brics = pd.DataFrame(countries)
print(brics)
brics.index = ("BR", "RU", 'IN', 'CH', "SA")
print("\n\n")
print(brics)

# Reading form csv file and using panda to go through data
print('\nUsing a .csv file to get data for pandas dataframe -- 305')
cars = pd.read_csv('cars.csv')
print(cars)
print('\nCan also switch the first column like this')
# doesn't reorder but shows this column first
cars2 = pd.read_csv('cars.csv', index_col=3)
print(cars2)


