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
    for range in ids:
        range_start = int(range[0])
        range_end = int(range[1])
        while range_start <= range_end:
            if not is_id_valid(range_start):
                invalid_ids.append(range_start)
            range_start += 1
    return invalid_ids

# part 1
id_input = open('2-input.txt')
invalid_ids = find_all_invalid_ids(id_input)
print(sum(invalid_ids))