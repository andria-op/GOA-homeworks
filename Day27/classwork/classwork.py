# 1)შექმენით ფუნქცია სახელად sum, რომელსაც გადაეცემა რიცხვების სია და თქვენი დავალებაა დაბეჭდოთ ამ სიაში მყოფი ყველა რიცხვის ჯამი
def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    print(total)


numbers_list = [1, 2, 3, 4, 5]
sum(numbers_list)
