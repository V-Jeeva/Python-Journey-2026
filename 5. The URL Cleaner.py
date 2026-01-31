# Topic: replace, count, Conditionals
# Problem: Clean a raw URL by stripping https:// and www. prefixes, replacing slashes with hyphens, and
# validating that the format doesn't have too many dots.

URL = input("Enter the URL: ")

if URL[0] == "h":
    URL = URL[8:]

if URL[0] == "w":
    URL = URL[4:]

URL = URL.replace("/", "-")

print("Invalid URL") if URL.count(".") > 2 else print(URL)