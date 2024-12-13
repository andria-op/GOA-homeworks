# hom 1
def sum_of_two_numbers(a, b):
    return a + b

print(sum_of_two_numbers(5, 7)) 
# hom 2
def even_or_odd(n):
    return "ლუწია" if n % 2 == 0 else "კენტია"

print(even_or_odd(8))

# hom 3
def positive_or_negative(n):
    if n > 0:
        return "დადებითია"
    elif n < 0:
        return "უარყოფითია"
    return "ნულოვანია"

print(positive_or_negative(-5)) 

# hom 4
def greet(name):
    print(f"Hello {name}")

greet("Giorgi")
greet("Nino")

# hom 5
def concatenate_strings(str1, str2):
    return str1 + str2

print(concatenate_strings("Hello, ", "world!"))
