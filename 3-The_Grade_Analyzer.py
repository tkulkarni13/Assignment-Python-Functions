import numpy as np

# Task 1: Function to calculate average

def average (*args):
    return np.mean(args)

# Task 2: Function for highest and lowest grade

def highest(*args):
    return np.max(args)

def lowest(*args):
    return np.min(args)

# Task 3: Categorize grades into letter grades

def numToLetterGrade (n):
    if (n >= 90):
        return "A"
    elif (n >= 80):
        return "B"
    elif (n >= 70):
        return "C"
    elif (n >= 60):
        return "D"
    else:
        return "F"
    
grades = [36, 98, 99, 76, 80, 81, 92, 83, 72, 66, 90, 81, 12, 80, 79, 77]
print(average(grades))
print(highest(grades))
print(lowest(grades))

grades_letters = []
for g in grades:
    grades_letters.append(numToLetterGrade(g))
print (grades_letters)