MIN_PASSWORD_LENGTH = 7
password = input("Enter password: ")
while len(password) < MIN_PASSWORD_LENGTH:
    print("Password must be at least", MIN_PASSWORD_LENGTH)
    password = input("Enter password: ")
print("*" * len(password))