#Topic: Math Module (sqrt, ceil)
# Problem: Calculate the side length of a square room based on area.
# Round the side length UP to the nearest integer.
# If the side is Even, it's symmetrical; if Odd, there will be scraps.

import math

area = float(input("Enter the area: "))

side = math.sqrt(area)
length = math.ceil(side)

print(f"Buy {length} meters. It's symmetrical") if length % 2 == 0 else print(f"Buy {length} meters. You will have scraps.")