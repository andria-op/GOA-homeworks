# upper რაიმე რაიმე სტრინგს დიდი ასოებით წერს
# lower რაიმე  სტრინგს პატარა ასოებით წერს
# capitalize რაიმე სტრინგს დიდი ასოთი იწყბს სხვას კი აპატარავებს 
# find პოულობს მითითებულ ასოს რაიმე სტრინგში


last_name = input("შეიტანეთ თქვენი გვარი: ")
if last_name[0].isupper():
    print("Hello")
else:
    print("Bye")





name = input("შეიტანეთ თქვენი სახელი: ")
char = input("შეიტანეთ ასო: ")

if char in name:
    index = name.index(char) 
    print("found it,")
else:
    print("Can't find character")




last_name = input("შეიტანეთ თქვენი გვარი: ")
change_case = input("როგორ უნდა შეიცვალოს თქვენი გვარი (upper, lower, capitalize)? ")
if change_case == "upper":
    print(last_name.upper())  
elif change_case == "lower":
    print(last_name.lower())  
elif change_case == "capitalize":
    print(last_name.capitalize())  
else:
    print("არასწორი არჩევანი")


