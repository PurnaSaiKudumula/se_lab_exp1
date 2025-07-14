import math

# Open and read values from the file
with open("input.txt", "r") as file:
    lines = file.readlines()
    A = float(lines[0].strip())
    B = float(lines[1].strip())
    peak_temp = float(lines[2].strip())
    T_target = float(lines[3].strip())

C = peak_temp - T_target
discriminant = B**2 - 4*A*C

if discriminant < 0:
    print("No real solution: temperature does not reach the target.")
else:
    t1 = (-B + math.sqrt(discriminant)) / (2*A)
    t2 = (-B - math.sqrt(discriminant)) / (2*A)
    print(f"Temperature {T_target}°C is reached at t = {t1:.2f} and t = {t2:.2f}")


