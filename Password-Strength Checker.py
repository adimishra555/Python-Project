import re

def check_password_strength(password):
    """
    Checks the strength of a password based on the following criteria:
    - Length (minimum 8 characters)
    - Contains uppercase letters
    - Contains lowercase letters
    - Contains numbers
    - Contains special characters
    """
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    if strength == 8:
        return "Strong password!"
    elif strength >= 5:
        return "Moderate password. Consider improving it."
    else:
        return "Weak password. Please follow the feedback below:\n" + "\n".join(feedback)

def main():
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    print(result)

if __name__ == "__main__":
    main()
