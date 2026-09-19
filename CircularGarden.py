# CIRCULAR GARDEN
# 9-19-2026

import math

radius = float(input("Enter the radius of the garden (meters): "))

area =math.pi * math.pow(radius, 2)
circumference = 2 * math.pi * radius
areaSquareRoot = math.sqrt(area)
areaRoundeddown = math.floor(area)
areaRoundedup = math.ceil(area)

print(f"Area: {area:.2f} square meters")
print(f"Circumference: {circumference:.2f} meters")
print(f"Square Root of Area: {areaSquareRoot:.2f}")
print(f"Rounded Down Area: {areaRoundeddown:.2f} square meters")
print(f"Rounded Up Area: {areaRoundedup:.2f} square meters")