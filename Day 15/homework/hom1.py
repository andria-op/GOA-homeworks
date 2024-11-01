my_favorite_number = 7  


user_number = int(input("შეიყვანეთ თქვენი საყვარელი რიცხვი: "))


if user_number == my_favorite_number:
    print("Perfect")
elif user_number > my_favorite_number:
    print("More")
else:
    print("Less")