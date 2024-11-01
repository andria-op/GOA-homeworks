correct_password = "idk_what_to_write" 

while True:
    user_input = input("შეიყვანეთ პაროლი: ")
    
    if user_input == correct_password:
        print("პაროლი სწორი არის!")
        break 
    else:
        print("პაროლი არასწორია, სცადეთ კიდევ ერთხელ.")