password = 12345 # corect password

attempts = 0
max_attempts = 5 #max attempts for input password

while attempts < max_attempts:
    Input_password = int(input("Enter your password:"))
    attempts += 1 #attempt counter

    if Input_password == password:
        print("Access has been granted.") #when password is correct
    else:
        remaining_attempts = max_attempts - attempts #when password is incorrect
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            print("Too many failed attempts. Authorities have been alerted!")

    
