def Temperature_modeling(a, b, c, time):
    return a * time ** 2 + b * time + c

with open('input.txt', 'r') as files:
    for line in files:
        line = line.strip()
        if not line:
            continue  # Skip empty lines

        parts = line.split()
        if len(parts) != 4:
            print(f"Skipping malformed line: {line}")
            continue  # Skip lines with incorrect number of values

        a, b, c, time = parts
        a = float(a)
        b = float(b)
        c = float(c)
        time = int(time)

        temp = Temperature_modeling(a, b, c, time)
        print(f'The Temperature at time {time} is {temp}')


