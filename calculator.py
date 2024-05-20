# Codédex Python

import math

print("==================")
print("Area Calculator 📐")
print("==================\n")

print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Exit")

while True:
    response = input("\nWhich shape: ")

    print()

    if response.isdigit():
        response = int(response)
        if response == 1:
            base = float(input("Base: "))
            height = float(input("Height: "))
            area = (base * height) / 2
            print(f"\nArea: {area:}")
        elif response == 2:
            length = float(input("Length: "))
            width = float(input("Width: "))
            area = (length * width)
            print(f"\nArea: {area}")
        elif response == 3:
            side = float(input("Side: "))
            area = (side * side)
            print(f"\nArea: {area}")
        elif response == 4:
            radius = float(input("Radius: "))
            area = (math.pi * radius * radius)
            print(f"\nArea: {area}")
        elif response == 5:
            print("Program terminated.")
            break
        else:
            print("Invalid input.")
    else:
        print("Invalid input.")
