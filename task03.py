import re

# ASCII Art Banner for "Pass Check"
print("""
  ____                  ____ _               _            
 |  _ \ __ _ ___ ___   / ___| |__   ___  ___| | _____ _ __ 
 | |_) / _` / __/ __| | |   | '_ \ / _ \/ __| |/ / _ \ '__|
 |  __/ (_| \__ \__ \ | |___| | | |  __/ (__|   <  __/ |   
 |_|   \__,_|___/___/  \____|_| |_|\___|\___|_|\_\___|_|   

""")

# Function to check password complexity
def check_password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    number_criteria = re.search(r"[0-9]", password) is not None
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Check strength based on criteria
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    # Provide feedback
    if strength_score == 5:
        strength = "Strong"
        feedback = "Your password is strong. Great job!"
    elif strength_score == 4:
        strength = "Moderate"
        feedback = "Your password is fairly strong, but adding more special characters could make it stronger."
    elif strength_score == 3:
        strength = "Weak"
        feedback = "Consider adding numbers and special characters to increase the password strength."
    else:
        strength = "Very Weak"
        feedback = "Your password is too weak. Try adding more characters, including uppercase letters, numbers, and special characters."

    return strength, feedback

# Main function to get user input and assess password strength
def main():
    password = input("Enter your password to check its strength: ")
    strength, feedback = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")
    print(f"Feedback: {feedback}\n")

# Run the program
if __name__ == "__main__":
    main()

