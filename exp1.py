import math

STEPNESS = 0.5
PEAK_HOUR = 4
PEAK_TEMP = 10
T_target = 20

A = STEPNESS
B = PEAK_HOUR
C = PEAK_TEMP - T_target

discriminant = B**2 - 4*A*C

if discriminant < 0:
    print("No real solution: temperature does not reach the target.")
else:
    t1 = (-B + math.sqrt(discriminant)) / (2*A)
    t2 = (-B - math.sqrt(discriminant)) / (2*A)
    print(f"Temperature {T_target}°C is reached at t = {t1:.2f} and t = {t2:.2f}")
