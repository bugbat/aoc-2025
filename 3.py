input = open('3-input.txt').read().splitlines()

jolts = []

for r in input:
    print(r)
    batt_a = 0
    batt_b = 0
    row_length = len(r)
    for pos, batt in enumerate(r):
        if int(batt) > batt_a and pos < row_length - 1:
            batt_a = int(batt)
            batt_b = 0
        elif int(batt) > batt_b:
            batt_b = int(batt)
    jolts.append(int(str(batt_a) + str(batt_b)))

print(sum(jolts))