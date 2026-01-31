# Topic: String Slicing (Reversing), Logic (and)
# Problem: Validate a password.
# It must be a palindrome (reads the same backwards) AND match case-insensitively AND be longer than 3 characters.

password = input("Enter your password: ")

password = password.lower()
rev = password[::-1]

print("Password accepted") if len(password) > 3 and rev == password else print("Password rejected")