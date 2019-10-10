# *THIS SHOULD BE SOLVED USING DICTIONARIES!
# *YOU MAY NOT CHECK IF THE ARRAYS ARE EQUAL. THIS METHOD *DOES* WORK IN
# *PYTHON, BUT NOT IN JAVASCRIPT. THE EXERCISE IS TO PRACTICE USING
# *DICTIONARIES AND FREQUENCY PATTERNS
# Given two arrays write a function to find out if two arrays have the same frequency of digits.

# dict1 = {}
# dict2 = {}

arr1 = [1,2,3,4]
arr2 = [1,2,3,4]
# arr2 = [1,3,2,4]

def compare_freq(arr1, arr2):
    dict1 = {}
    dict2 = {}
    for num in arr1:
        if num in dict1:
            