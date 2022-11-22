"""
Problem:
How to find median value in a list without using a premade function and loop?

Solution:
"""

list1 = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
list2 = [22, 19, 24, 20, 25, 26, 24, 25, 24]

def find_median(x):
    x_length = len(x)
    x_length_half = int(x_length / 2)
    
    if(x_length % 2):
        return x[x_length_half]
    else: 
        return x[x_length_half-1], x[x_length_half]
        
print(find_median(list1))
print(find_median(list2))
