# 1
def to_jaden_case(string):  
    return ' '.join(word.capitalize() for word in string.split())
# 2
def sequence_sum(begin_number, end_number, step):  
    total_sum = 0   
    if step <= 0 or begin_number > end_number:  
        return total_sum  
    for number in range(begin_number, end_number + 1, step):  
        total_sum += number 
    return total_sum
# 3
import re  
def lowercase_count(string):  
    return len(re.findall(r'[a-z]', string))
# 4
def better_than_average(class_points, your_points):  
    average = sum(class_points) / len(class_points)   
    return your_points > average
# 5
def grow(arr):  
    product = 1  
    for num in arr:  
        product *= num  
    return product
# 6
def smash(words):  
    return ' '.join(words)
# 7
def manual_join(list1, list2):
    return list1 + list2






