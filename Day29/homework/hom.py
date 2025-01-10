# 1
def multiply(a, b):
    return a * b
# 2
"abc123".isalnum()  # True
"abc 123".isalnum()  # False (განსხვავებით სივრცე)
"12345".isdigit()  # True
"123a".isdigit()  # False
"hello".islower()  # True
"Hello".islower()  # False
"12345".isnumeric()  # True
"one".isnumeric()  # False
"HELLO".isupper()  # True
"Hello".isupper()  # False
"banana".count("a")  # 3
"apple".count("p")  # 2
# 3
min([3, 1, 7, 5])  # 1
max([3, 1, 7, 5])  # 7
min("hello")  # 'e' (მინიმალური ასო ამ სიტყვის მიხედვით)
max("hello")  # 'o' (მაქსიმალური ასო ამ სიტყვის მიხედვით)

