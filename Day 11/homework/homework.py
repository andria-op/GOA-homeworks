my_name = "Andria"
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_height = float(input("Enter your height in meters: "))
if user_age > 18 and user_name == my_name and user_height > 1.80:
    print("you look like me")
else:
    print("we aren't same")