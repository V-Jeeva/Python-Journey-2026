#Topic: String Methods (find, rfind, isdigit) Problem: Agents enter IDs as agent_code_lastname.
#Dynamically extract the code and last name.
#Access is granted ONLY if the middle code consists purely of numbers.

ID = input("Enter the ID: ")
us1 = ID.find("_")
us2 = ID.rfind("_")

last_name = ID[us2+1:]
code = ID[us1+1 : us2]

print(f"Access Granted. Welcome agent {last_name}.") if code.isdigit() else print("Access denied")