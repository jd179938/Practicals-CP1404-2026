"""
Emails
Estimate: 20 minutes
Actual: 25 minutes
"""


def main():
    """Store users email and name in a dictionary."""
    email_to_name = {}
    email = input("Enter email: ")
    while email != "":
        name = extract_name_from_email(email)
        correct_name = input(f"Is your name {name}? (Y/n) ").upper()
        if correct_name != 'Y':
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Enter email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Extract name from email."""
    name = email.split('@')[0]
    return (" ".join(name.split('.'))).title()



main()
