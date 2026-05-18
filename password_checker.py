import re

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&*)")

    if score == 5:
        print("Strong password!")
    elif score >= 3:
        print("Moderate password. Suggestions:")
        for f in feedback:
            print("-", f)
    else:
        print("Weak password. Suggestions:")
        for f in feedback:
            print("-", f)

password = input("Enter a password to check: ")
check_password(password)
