import re

def is_valid_email(email):
    # Regular expression to match email pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # If the pattern matches, the email is valid
    if re.match(pattern, email):
        return True
    return False