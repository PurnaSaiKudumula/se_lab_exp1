def Temperature_modeling(a, b, c, time):
    # Example model: quadratic equation
    return a * time ** 2 + b * time + c

with open('input.txt', 'r') as file:
    line = file.readline().strip()
    a, b, c, time = line.split()
    a = float(a)
    b = float(b)
    c = float(c)
    time = int(time)

    temp = Temperature_modeling(a, b, c, time)
    print(f'The Temperature at time {time} is {temp}')
