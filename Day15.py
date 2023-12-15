input_file = 'InputFiles/Day15.txt'
seq = open(input_file).read().split(",")

test_str = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
test_seq = test_str.split(",")


def get_hash(word, curr_value = 0):
    char = word[0]
    curr_value += ord(char)
    curr_value *= 17
    curr_value = curr_value % 256
    if len(word) == 1:
        return curr_value
    else:
        return get_hash(word[1:], curr_value)


results = sum([get_hash(x) for x in seq])
print(results)


light_boxes = {}
for x in range(256):
    names = "Box " + str(x)
    light_boxes[names] = []


for lens in seq:
    if "=" in lens:
        code = lens.split("=")[0]
        box_name = "Box " + str(get_hash(code))
        fl = int(lens.split("=")[1])
        # UPDATE LENS IF FOUND
        for i, l in enumerate(light_boxes[box_name]):
            if l[0] == code:
                light_boxes[box_name][i] = (code, fl)
                break
        else:
            light_boxes[box_name].append((code, fl))

    if "-" in lens:
        code = lens.split("-")[0]
        box_name = "Box " + str(get_hash(code))
        # REMOVE LENS IF FOUND
        light_boxes[box_name] = [l for l in light_boxes[box_name] if l[0] != code]


result = 0
for box, lenses in light_boxes.items():
    if len(lenses) == 0:
        continue
    for i, l in enumerate(lenses):
        result += (1 + int(box.split(" ")[1])) * (i+1) * l[1]

print(result)