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
def smash(words):  
    return ' '.join(words)
# 4
def manual_join(list1, list2):
    return list1 + list2
# 5
def is_palindrome(s):  
    s = s.lower()  
    return s == s[::-1]