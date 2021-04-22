.......................................Q1.......................................

1) Write a python code that ask the user to
enter his birth year and then print his age in
years.

......................................Answer.......................

name = input("Enter your name: ")
Age = int(input("Enter your age: "))
print("Hello", name, " You were born in ", 2021 - Age,".")
 
 ......................................Q2............................
 
2) Write a python code to find Sum and Average of N Natural
Numbers


.......................................Answe...........................


sum=0
Ave=1
for num in range(0, 51):
    sum=sum+num
    Ave=sum/50

print (sum)
print (Ave)


.......................................Q3..............................
3) Pyramid Pattern with Stars

......................................ANswer.............................

length = 5
k = (2 * length) - 2
for p in range(0, length):
   for n in range(0, k):
      print(end=" ")
   k = k - 1
   for n in range(0, p + 1):
      print("*", end=' ')
   print(" ")
   
   
   ...................................Q4...............................
  4)Python Program to Check Even or Odd
  
  ...................................Answe.............................
  
  

count=0
word= "q"
while(count<10):
   num=int(input("Enter the number please" ))
   if (num%2==0):
      print("this number is even")
   
   elif(str(num) == 'q'):
      break
   else:
      print("this number is odd")

   count+=1


........................................Q5...................................
Remove Vowels from String

........................................ANSWER..............................

string = input("Enter any string: ")
if string == 'q':
    exit();
else:
    newstr = string;
    print("\nRemoving vowels from the given string");
    vowels = ('a', 'e', 'i', 'o', 'u');
    for x in string.lower():
        if x in vowels:
            newstr = newstr.replace(x,"");
    print(newstr);
  

...........................................Q6....................................
Write a Python program to write a list to a file.

...........................................ANswe...................................
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('abc.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('abc.txt')
print(content.read())


.........................................Q7......................................
7)Write a Python function to sum all the numbers in a list
print(sum((2, 6, 7, 9, 0)))

..........................................Answer .......................................


def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

print(sum((2, 6, 7, 9, 0)))



...........................................Q8........................................

8) Write a Python program to print the even numbers from
a given list.
print(is_even_num([3, 9, 5, 4, 5, 18, 7, 18,19]))
Output : [4, 18, 18]


.........................................Answer.....................................

def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))



.................................................Q9.........................................

Write a Python class which has two methods get_String and
print_String. get_String accept a string from the user and print_String
print the string in upper case.

...............................................Answe.......................................

class func():  
    def __init__(self):  
        self.str1 = ""  
  
    def get_String(self):  
        self.str1 = input()  
  
    def print_String(self):  
        print(self.str1.upper())  
  
str1 = func()  
str1.get_String()  
str1.print_String()

.................................................Q10...................................

Write a python class to calculate the average speed, distance travelled and
the trip duration of a vehicle: car, bus, train, bike, motorcycle, plane etc.
constructed by a Distance (Km) and Time(H) and a method which will
compute the speed of a car.

.................................................Answer...................................

sec_to_hr = 1/3600 # 3600 seconds in 1 hour
min_to_hr = 1/60 # 60 minutes in 1 hour
km_to_miles = 0.62 # 0.62 miles in 1 kilometer

time_hrs = 1 + (5*min_to_hr)+ (42*sec_to_hr) # Total time in hours
dist_miles = 10 * km_to_miles # Total time in miles

av_speed = dist_miles/time_hrs # Average Speed in miles/hour

answer1 = "Average speed = {} miles per hour".format(round(av_speed,2))

print(answer1)  


.........................................Q11..................................

11) Write a NumPy program to create a 3x3 matrix with
values ranging from 2 to 10.


........................................Answer....................................

import numpy as np
x =  np.arange(2, 10).reshape(3,3)
print(x)

........................................Q12.............................................
12) Write a NumPy program to remove the negative
values in a NumPy array with 0

...........................................Answer..........................

import numpy as np
x = np.array([-1, -4, 0, 2, 3, 4, 5, -6])
print("Original array:")
print(x)
print("Replace the negative values of the said array with 0:")
x[x < 0] = 0
print(x)

.............................................Q13...................................

13) Write a NumPy program to partition a given array in a specified
position and move all the smaller elements values to the left of the
partition, and the remaining values to the right, in arbitrary order.

Original array:
[ 70 50 20 30 -11 60 50 40]
After partitioning on 4 the position:
[-11 30 20 40 50 50 60 70]


.............................................Answer............................


import numpy as np
nums = np.array([70, 50, 20, 30, -11, 60, 50, 40])
print("Original array:")
print(nums)
print("\nAfter partitioning on 4 the position:")
print(np.partition(nums, 4))


................................................Q14..................................

Write a program that repeatedly prompts a user for integer numbers until
the user enters 'done'. Once 'done' is entered, print out the largest and smallest
of the numbers. If the user enters anything other than a valid number catch it
with a try/except and put out an appropriate message and ignore the number.
Enter 7, 2, bob, 10, and 4 and match the output below.


...........................................ANswer......................................

largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
#print (num)
        num = int(num)
        if largest is None or largest < num:
            largest = num
        elif smallest is None or smallest > num:
            smallest = num
    except ValueError:
            print("Invalid input")

print ("Maximum is", largest)
print ("Minimum is", smallest)


...................................................Q15..............................
Write a program that prompts for a file name, then opens that file
and reads through the file, and print the contents of the file in upper
case. Use the file words.txt to produce the output below (Green Whit black pink yellow)

...............................................Answer.........................


fname = input("Enter file name: ")
try :
    fh = open(fname)
except:
    print('Cannot open the file ',fname ,'please try again')
    quit()

for line in fh :
    line = line.upper()
    line = line.rstrip()
    print(line)
    
    .....................................Q16...........................................
    Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who
sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.


......................................Answer..............................................

fhand = open("mbox-short.txt")
count = 0
for line in fhand:
    line = line.rstrip()
    if line == "": continue
        
    words = line.split()
    if words[0] !="From": continue
        
    print(words[1])
    count = count+1

print ("There were", count, "lines in the file with From as the first word")

   
