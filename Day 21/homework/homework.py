# hom1
my_list = [10, 20, 30, 40, 50]
last_three_elements = my_list[-3:]
print(last_three_elements)

# hom2
numbers = [5, 12, 8, 21, 10, 15, 3, 30, 9, 7]
filtered_numbers = [num for num in numbers if num >= 10]
print(filtered_numbers)

# hom3

# 1. print() - გამოაქვს კონსოლში ინფორმაცია
# 2. len() - დებს სიის ან სტრიქონის სიგრძეს
# 3. input() - მიიღებს ინფორმაციას მომხმარებლისგან
# 4. range() - გამოიწვევს რიცხვთა დასრესებას (პირობითი ტარება)
# 5. list() - კონვერტირებს მონაცემთა ტიპს სიად

# hom4

last_name = input("შეიყვანეთ თქვენი გვარი: ")
uppercase = input("გსურთ რომ თქვენი გვარი გადაიყვანოთ დიდ ასოებად? (yes/no): ")
if uppercase.lower() == "yes":
    first_name = input("შეიყვანეთ თქვენი სახელი: ")
    print(first_name.upper())
else:
    first_name = input("შეიყვანეთ თქვენი სახელი: ")
    print(first_name)
