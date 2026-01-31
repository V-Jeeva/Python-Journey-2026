code = input("Enter the code of scanner: ")
hyphen = code.find("-")

item_name = code[2:hyphen]
price = int(code[hyphen+1 : -2])

price = price + price/10

print("High Value Item!") if price > 1000 else print("Standard Item")