import string

def check_password_strength(password):
    # Initialize our scoring metrics
    length_error = len(password) < 8
    digit_error = not any(char.isdigit() for char in password)
    uppercase_error = not any(char.isupper() for char in password)
    lowercase_error = not any(char.islower() for char in password)
    special_error = not any(char in string.punctuation for char in password)
    
    # Evaluate the rules
    errors = [length_error, digit_error, uppercase_error, lowercase_error, special_error]
    strength_score = errors.count(False) # Counts how many rules you PASSED
    
    # Determine the feedback string
    if strength_score == 5:
        return "🟢 STRONG: Excellent password. Meets corporate security protocols."
    elif strength_score >= 3:
        return "🟡 MEDIUM: Weak infrastructure defense. Needs more variance."
    else:
        return "🔴 WEAK: Critical Security Risk! Easily automated by brute-force attacks."

# Simple user interface loop
print("--- Corporate Network Password Validator ---")
user_pass = input("Enter a password to analyze: ")
print(check_password_strength(user_pass))
