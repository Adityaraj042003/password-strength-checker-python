import re

# password strength check condition:
# min 8 chars,digit,upper case,lower case & Special charcter

def check_password_strength(password):
    if len(password) < 8:
        return "weak: password must be  at lest 8 chars"
    
    if not any(char.isdigit() for char in password):
        return "weak: password must contain a digit"
    
    if not any(char.isupper()for char in password):
        return "weak: password must contain an upper char"
    
    if not any(char.islower() for char in password):
        return "weak: password must contain an lower char"
    
    if not re.search(r"[!#$%&'()*+,-./:;<=>?@[\]^_`{|}~]",password):
        return "Medium: password must contain a special char"
    
    return "Strong: your password is secured!"


def password_checker():
    print("\n")
    print("Welcome to the password strength checker:\n")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")

        if password.lower() == "exit":
            print("Thanku for using this tool")
            break

        result = check_password_strength(password)
        print(result)


# Run the Password checker tool

if __name__ == "__main__":
    password_checker()  