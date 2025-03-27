def login(username, password):
    correct_username ="admin"
    correct_password ="xyz1234"

    if username == correct_username and password == correct_password:
        return "login successful!"
    else:
        return "invalid username or password"
    
user_name =(input("enter your username :"))
user_password = (input("enter your password :"))
print(login(user_name , user_password))
