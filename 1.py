dial_min = 0
dial_max = 99
dial_start = 50

dial_target = 0
input_file = '1-input.txt'

def parse_input(input):
    file = open(input)
    instructions = []
    for line in file:
        line = line.rstrip()
        dir = line[:1]
        count = int(line[1:])
        if dir is 'R':
            instructions.append(count)
        else:
            instructions.append(-count)
    return instructions

instructions = parse_input(input_file)

password = 0

for movement in instructions:
    next_start = (dial_start + movement) % 100
    if next_start == 0:
        password += 1
    dial_start = next_start

print(password)