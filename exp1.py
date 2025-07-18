
def temperature_model(t, a, h, k):
    temp = -a * (t - h)**2 + k
    return round(temp, 2)

with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

sets = [lines[i:i+5] for i in range(0, len(lines), 5)]

for idx, s in enumerate(sets):
    a = float(s[0])
    h = int(s[1])
    k = float(s[2])
    start_hour = int(s[3])
    end_hour = int(s[4])

    print(f"\n--- Set {idx + 1} ---")
    print("Hour\tTemperature (°C)")
    for hour in range(start_hour, end_hour + 1):
        print(f"{hour:02d}\t{temperature_model(hour, a, h, k)}")


