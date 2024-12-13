# hom 1
even_numbers = []
for number in range(201):
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# hom 2
favorite_names = []
for i in range(5):
    name = input("შეიყვანეთ თქვენი საყვარელი სახელი: ")
    favorite_names.append(name)
print(favorite_names)

# hom 3
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(1, len(numbers), 2):
    print(numbers[i])

# hom 4
text = "Hello, world!"
length = len(text)
print(length)

# hom 5
my_list = [10, 20, 30, 40, 50]
index = int(input("შეიყვანეთ რიცხვი, რომლის ინდექსსაც გსურთ ამოღება: "))
removed_element = my_list.pop(index)
print(f"ამოღებული ელემენტი: {removed_element}")

# hom 6
my_list = [1, 2, 3, 4, 5]
print(len(my_list))