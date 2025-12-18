def is_id_valid(id):
    id_len = len(str(id))
    if id_len % 2 == 1:
        return True
    else:
        id_a = str(id)[:id_len // 2]
        id_b = str(id)[id_len // 2:]
        if id_a == id_b:
            return False
    return True

def is_id_valid_alternate(id):
    id_str = str(id)
    id_len = len(id_str)
    if id_len == 1:
        return True
    else:
        for i in range(id_len // 2):
            seq = id_str[0:i + 1]
            for x in range(len(seq), id_len, len(seq)):
                if seq != id_str[x:x + len(seq)]:
                    valid = True
                    break
                valid = False
            if valid == False:
                return False
    return True

def parse_input(input):
    split_input = input.split(',')
    id_list = []
    for i in split_input:
        a, b = i.split('-')
        id_list.append((a, b))
    return id_list

def find_all_invalid_ids(id_list):
    ids = parse_input(id_list.read())
    invalid_ids = []
    invalid_ids_alternate = []
    for range in ids:
        range_start = int(range[0])
        range_end = int(range[1])
        while range_start <= range_end:
            if not is_id_valid(range_start):
                invalid_ids.append(range_start)
                invalid_ids_alternate.append(range_start)
            else:
                if not is_id_valid_alternate(range_start):
                    invalid_ids_alternate.append(range_start)
            range_start += 1
    return [invalid_ids, invalid_ids_alternate]

# part 1
id_input = open('2-input.txt')
invalid_ids = find_all_invalid_ids(id_input)
print(f'Part 1 answer: {sum(invalid_ids[0])} \nPart 2 answer: {sum(invalid_ids[1])}')

# part 2
# id_input = open('2-input.txt')
# invalid_ids_part2 = find_all_invalid_ids(id_input)
# print(sum(invalid_ids_part2))

# test = '012345'
# print(test[0:1])
# for i in range(10):
#     print(i)