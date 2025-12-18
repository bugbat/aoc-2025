def parse_input(input):
    file = open(input)
    instructions = []
    for line in file:
        line = line.rstrip()
        dir = line[:1]
        count = int(line[1:])
        if dir == 'R':
            instructions.append(count)
        else:
            instructions.append(-count)
    return instructions

def get_password_a(input_file, dial_min=0, dial_max=99, dial_start = 50, dial_target = 0):
    instructions = parse_input(input_file)
    password = 0
    for movement in instructions:
        next_start = (dial_start + movement) % 100
        if next_start == 0:
            password += 1
        dial_start = next_start

    return password

def get_password_b(input_file, dial_min=0, dial_max=99, dial_start = 50, dial_target = 0):
    instructions = parse_input(input_file)
    password = 0
    for movement in instructions:
        if movement < 0:
            div, mod = divmod(movement, -100)
            password += div
            if dial_start != 0 and dial_start + mod <= 0:
                password += 1
        else:
            div, mod = divmod(movement, 100)
            password += div
            if dial_start + mod >= 100:
                password += 1

        dial_start = (dial_start + movement) % 100
    return password

print(get_password_a('1-input.txt', 0, 99, 50, 0))
print(get_password_b('1-input.txt', 0, 99, 50, 0))