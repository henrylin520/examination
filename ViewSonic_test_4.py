# -*- coding: utf-8 -*-
"""
ViewSonic examine 4
"""

import itertools

def find_combunations_with_zero_sum(numbers):
    result = []
    num_sum = 0
    for r in range(2, len(numbers)+1):
        for combo in itertools.combinations(numbers, r):
            for num in combo:
                num_sum += int(num)
            if num_sum == 0:
                result.append(combo)
            num_sum = 0
    return result

while(True):
    a = input("Plese enter a list with numbers.(Separate by \',\') \ninput:")
    user_input_numbers = []
    user_input_numbers = a.split(',')
    
    #check if the value user input is at least two numbers 
    if len(user_input_numbers) <= 1:
        print('Please enter at least two numbers')
        continue
    for numbers in user_input_numbers:
        #check if the numbers user input is numberic
        if numbers.isnumeric() != True and str(abs(int(user_input_numbers[0]))).isnumeric()==False:
            print('Input with non numeric. \nPlease re-enter again!')
            continue
    
    result = find_combunations_with_zero_sum(user_input_numbers)
   
    if len(result) == 0 :
        print('None of combination is zero ')
        break
    else :
        print('Output:\n')
        print(result)
        break
