import math

radius = float(input("Enter the radius of the sphere: "))

diameter = 2 * radius

circumference = 2 * math.pi * radius

surface_area = 4 * math.pi * radius ** 2

volume = (4/3) * math.pi * radius ** 3

print(f"Diameter: {diameter}")
print(f"Circumference: {circumference}")
print(f"Surface Area: {surface_area}")
print(f"Volume: {volume}")