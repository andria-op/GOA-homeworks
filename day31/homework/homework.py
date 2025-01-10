# https://www.codewars.com/kata/523b4ff7adca849afe000035/train/python
def greet():  
    return "hello world!"
# https://www.codewars.com/kata/56dec885c54a926dcd001095/train/python
def opposite(number):  
    return -number
# https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python
def make_negative(number):  
    if number > 0:  
        return -number  
    return number
# https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python
def positive_sum(arr):  
    return sum(x for x in arr if x > 0)
# https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/train/python
def repeat_str(n, s):  
    return s * n
# https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
def square_sum(numbers):  
    return sum(x ** 2 for x in numbers)
# https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python
def find_smallest_int(arr):  
    return min(arr)
# https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python
def summation(num):  
    return sum(range(1, num + 1))
# https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/python
def no_space(x):  
    return x.replace(" ", "")
# https://www.codewars.com/kata/54edbc7200b811e956000556/train/python
def count_sheeps(sheep):  
    return sum(1 for s in sheep if s)