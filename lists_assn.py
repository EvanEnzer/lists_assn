## Part 1 ##

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
print(f"the grades in desendeing order are {grades}")
total_grades = len(grades)
all_grades = sum(grades)
print(f"the total number of grades is: {total_grades}")
print(f"the sum of all grades is {all_grades}")
average_grade = sum(grades) / len(grades)
print(f"average grade: {average_grade}")
grades[0] = ("FAIL") # we have not gotten to iterating or loops but it looks like you can do that
grades[1] = ("FAIL")
grades[2] = ("FAIL")
print(grades)

## Part 2 ##
'''You have two lists of student names. 
One list contains the names of students who have submitted their assignments,
and the other list contains the names of students who attended the 
last class.

Find out which students both submitted 
their assignments and attended the class.

Check if the two lists are 
identical in terms of their content, regardless of order.
'''
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

print("Charlie" in submitted) #returns true if in both
print("Eve" in submitted)
print("Alice" in submitted)
print("Frank" in submitted)

if "Charlie" in submitted: # this is another way to check and display
    print("Charlie is in both")
else: 
    print("Charlie is in both")
if "Eve" in submitted:
    print("Eve is in both")
else: 
    print("Eve is not in both")
if "Alice" in submitted:
    print("Alice is in both")
else: 
    print("Alice is not in both")
if "Frank" in submitted:
    print("Frank is in both")
else: 
    print("Frank is not in both")

# this doesn't check content, but it checks if they are the same
    
# if submitted == attended:
#   print("the lists are the same")
# if submitted != attended: 
#    print("the lists are not the same")

# the below checks for content
if "Alice" in submitted and attended and "Bob" in submitted and attended and "Charlie" in submitted and attended and "David" in submitted and attended and "Eve" in submitted and attended and "Frank" in submitted and attended:
    print("the lists are the same")
else:
    print("the lists are not the same")

if "Charlie" not in submitted:
    attended.index("Charlie") 
    attended.remove("Charlie")
if "Eve" not in submitted:
    attended.index("Eve") 
    attended.remove("Eve")
if "Alice" not in submitted:
    attended.index("Alice") 
    attended.remove("Alice")
if "Frank" not in submitted:
    attended.index("Frank") 
    attended.remove("Frank")
print(attended)

## Part 3 ##

'''
You have a list of daily temperatures for a month, and you'd like to extract specific data from it.
Extract the temperatures for the second week (7 days) of the month.
Extract all the temperatures above 100.
 Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.
'''

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
temperatures_copy = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
seven_days = temperatures [-7: ]
print(f"the last seven days are {seven_days}")
temperatures.sort()
print(temperatures)
over_100 = temperatures [-7: ]
print(f" the following tempritures are over 100 {over_100}")
temperatures_copy.reverse
fifth_day = temperatures_copy [4:5]
seventh_day = temperatures_copy [6:7]
fifth_seventh_days = fifth_day + seventh_day
print(f" the temperatures on the fifth and seventh days are {fifth_seventh_days}")

## Part 4 ##

'''
You have a list of numbers, and you'd like to generate a new list based on certain conditions.
Use a list comprehension to create a new list containing only even numbers.
Use a list comprehension to create a new list containing numbers greater than 5.
Check if the number 7 is in the original numbers list.
'''

numbers = ["1, ", "2, ", "3, ", "4, ", "5, ", "6,", "7, " ,"8, ", "9, ", "10"]
numbers_copy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_2 = numbers[1]
number_4 = numbers[3]
number_6 = numbers[5]
number_8 = numbers[7]
number_10 = numbers[9]
even_numbers = number_2 + number_4 + number_6 + number_8 + number_10
print(f" the even numbers are: {even_numbers}")
over_five = numbers_copy [5: ]
print(f"the numbers over five are: {over_five}")
if 7 in numbers_copy:
    print("seven is in the list.") 

## Part 5 ##

'''
You're organizing a school event, and you have lists containing student names, their grades, and the activities they're interested in.
Create a new list where each element is a dictionary with keys name, grade, and activity and the corresponding values from the provided lists.
Filter out students who have grades below 80.
For the remaining students, add a new key-value pair in their dictionary: "status": "Passed".
'''

# note that we have not done dictionaries yet or key-value pairs

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["football", "music", "art", "dance"]

john_dictionary = {"name": students[0], "grade": grades[0], "activities": activities[0]}
doe_dictionary = {"name": students[1], "grade": grades[1], "activities": activities[1]}
jane_dictionary = {"name": students[2], "grade": grades[2], "activities": activities[2]}
smith_dictionary = {"name": students[3], "grade": grades[3], "activities": activities[3]}

if (john_dictionary["grade"]) < 80:
    students[students.index("John")]
    students.remove("John")
else:
    john_dictionary["status"] = "passed"
if (jane_dictionary["grade"]) < 80:
    students[students.index("Jane")]
    students.remove("Jane")
else:
    jane_dictionary["status"] = "passed"
if (doe_dictionary["grade"]) < 80:
    students[students.index("Doe")]
    students.remove("Doe")
else:
    doe_dictionary["status"] = "passed"
if (smith_dictionary["grade"]) < 80:
    students[students.index("Smith")]
    students.remove("Smith")
else:
    smith_dictionary["status"] = "passed"
print(students)
print(john_dictionary)

