# Topic: String Slicing, Casting & Ternary Operators 
# Problem: A scanner reads tags in the format ##ITEM-PRICE$$.
# Extract the item name and price, add 10% tax, and check if it's a "High Value Item" (> 1000) or "Standard Item".

code = input("Enter the code of scanner: ")
hyphen = code.find("-")

item_name = code[2:hyphen]
price = int(code[hyphen+1 : -2])

price = price + price/10


print("High Value Item!") if price > 1000 else print("Standard Item")
