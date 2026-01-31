# Topic: String Methods (strip, replace, upper), Type Casting, Logic
# Problem: Clean a raw barcode string (e.g., " milk-carton_45 ") by stripping spaces,
# formatting the product name (replace hyphens with spaces, convert to uppercase),
# and extracting the price to determine if it is a "Budget" or "Expensive" item.

raw = input("Enter the raw Data: ")

# Clean spaces
raw = raw.strip()

# Find separator
underscore = raw.find("_")

# Format Name
product_name = raw[:underscore]
product_name = product_name.replace("-", " ")
product_name = product_name.upper()

# Extract Price
price = int(raw[underscore +1 :])

# Determine Verdict
verdict = "Budget Item" if price < 50 else "Expensive Item"

print(f"Product: {product_name}")
print(f"Price: {price}")
print(f"Verdict: {verdict}")