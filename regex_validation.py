import re
def validate_email(email):
    if not email:
        return "Email cannot be empty"

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.fullmatch(pattern, email):
        return "Valid Email ✅"
    else:
        return "Invalid Email ❌"
def validate_mobile(mobile):
    if not mobile:
        return "Mobile number cannot be empty"

    pattern = r'^[6-9]\d{9}$'
    
    if re.fullmatch(pattern, mobile):
        return "Valid Indian Mobile Number ✅"
    else:
        return "Invalid Mobile Number ❌"
def validate_password(password):
    if not password:
        return "Password cannot be empty"

    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'

    if re.fullmatch(pattern, password):
        return "Strong Password ✅"
    else:
        return "Weak Password ❌"
def main():
    email = input("Enter email: ")
    print(validate_email(email))

    mobile = input("Enter mobile number: ")
    print(validate_mobile(mobile))

    password = input("Enter password: ")
    print(validate_password(password))
if __name__ == "__main__":
    main()
