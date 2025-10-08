# validate user input
# 1. username must not be more than 12 chars
# 2. username must not contain spaces
# 3. username must not contain digits or special chars
# 4. username will be stored in lowercase

username = input("Enter a username: ").lower()

if len(username) > 12:
    print("Your username can't be more than 12 chars")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers or special chars")
else:
    print(f"Welcome, {username}!")
