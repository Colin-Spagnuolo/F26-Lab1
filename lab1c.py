
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Colin Spagnuolo
# Date: September 18th, 2026
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1c.py
import math
radius=input("Enter the radius of the circle: ")
radius=int(radius)
area=math.pi*radius**2
print(f"The area of the circle with radius {radius} is {area}")