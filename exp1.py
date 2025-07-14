import math


A = float(input("Enter stepness (A): "))
B = float(input("Enter peak hour (B): "))
peak_temp = float(input("Enter peak temperature (in °C): "))
T_target = float(input("Enter target temperature (in °C): "))

C = peak_temp - T_target

discriminant = B**2 - 4*A*C

if discriminant < 0:
    print("No real solution: temperature does not reach the target.")
else:
    t1 = (-B + math.sqrt(discriminant)) / (2*A)
    t2 = (-B - math.sqrt(discriminant)) / (2*A)
    print(f"Temperature {T_target}°C is reached at t = {t1:.2f} and t = {t2:.2f}")

