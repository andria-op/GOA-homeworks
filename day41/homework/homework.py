# 1
def power(base, exponent):
    return base ** exponent
result = power(2, 3)
print(result)
# 2
def check_list_length(my_list):
    if len(my_list) % 2 == 0:
        return "List length is even"
    else:
        return "List length is odd"

print(check_list_length([1, 2, 3, 4]))
print(check_list_length([1, 2, 3]))
