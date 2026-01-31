#Topic: Advanced Slicing, F-Strings
# Problem: Parse raw data in the format [Name]--<Year>--$Score$.
# Extract the name, calculate age from the year, and determine pass/fail status based on the score.

raw = input("Enter the raw data: ")

name = raw[raw.find("[")+1 : raw.find("]")]
birth_year = int(raw[raw.find("<")+1 : raw.find(">")])
score = float(raw[raw.find("$")+1 : raw.rfind("$")])

age = 2025 - birth_year

print(f"Student: {name} | Age: {age} | Status: Passed") if score > 50 else print(f"Student: {name} | Age: {age} | Status: Failed")