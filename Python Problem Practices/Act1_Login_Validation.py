def validation(a,b):
    if a == "admin":
        if b == "password":
            print("welcome")
            return
    print("try again")

username = input("Input a username: ")
password = input("Input a password: ")

validation(username,password)
