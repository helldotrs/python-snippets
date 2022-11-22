"""
Problem:
How to find median age in a list without using a premade function and loop?

Solution:
"""
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

list_length       = len(ages)
half_list_length  = int(list_length / 2)

if(list_length % 2):
  print(ages[half_list_length])
else:
  print(ages[half_list_length-1])
  print(ages[half_list_length])
  
"""
alternatively:
"""
if(not (list_length % 2)):
  print(ages[half_list_length-1])
print(ages[half_list_length])
  
