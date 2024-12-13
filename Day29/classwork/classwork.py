
def sum_with_for(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
def sum_with_builtin(numbers):
    return sum(numbers)
numbers = [1, 2, 3, 4, 5]
print(sum_with_for(numbers)) 
print(sum_with_builtin(numbers)) 