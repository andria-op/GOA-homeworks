# ```1)შექმენით სია რომელშიც იქნება 5 სახელი შემდეგ, ამოიღეთ სიიდან პირველი და ბოლო ელემენტი


# 2)კომეტარებით ახსენით რას აკეთებს თითოეული ფუნქცია:

# .insert()
# .append()
# .pop()
# .len()


# 3) შექმენით სია რომელიც შედგება 5 სახელისგან შემდეგ insert მეთოდით დაამატეთ ახალი სახელი სიის მეორე ინდექსზე```

# პირველი დავალება
names = ["ზურა", "მარიამი", "ნინო", "თამარი", "გიორგი"]
names.pop(0)  
names.pop(-1)   
print(names)

# მეორე დავალება

# .insert - ამ ფუნქციით შეგიძლია დაასახავო ახალი ელემენტი ნებისმიერ ინდექსზე (index) სიის შიგნით. მაგალითად, თუ გინდა რომელიმე ელემენტი დაემატოს ინდექსზე 2, გამოიძახე insert(2, 'სახელი').

# .append - ამ ფუნქციით შეგიძლია დაამატო ელემენტი სიის ბოლოს. მაგალითად, append('ახალი სახელი') დაამატებს ამ სახელს სიის ბოლოს.

# .pop - ამ ფუნქციას სიის ელემენტის ამოსაღებად იყენებენ. თუ არ მიუთითებ ინდექსს, ამოიღებს ბოლო ელემენტს. მაგალითად, pop(0) ამოიყვანს პირველი ელემენტს.

# len - ეს ფუნქცია გამოიცნობდა სიის სიგრძეს, ანუ იმ ელემენტების რაოდენობას, რომლებიც სიაშია. მაგალითად, len(names) გიყვება რამდენი ელემენტი აქვს სიას.

# მესამე დავალება
names = ["გიორგი", "მარიამი", "ნინო", "ზურა", "თამარი"]
names.insert(2, "ილია")
print(names)