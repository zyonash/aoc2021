def part_1():
    h_position = 0
    depth = 0
    with open("day_2_input.txt") as f:
        full_instructions = f.readlines()
        for i in full_instructions:
            current_instruction = i.split()
            if current_instruction[0] == "forward":
                h_position += int(current_instruction[1])
            elif current_instruction[0] == "down":
                depth += int(current_instruction[1])
            else:
                depth -= int(current_instruction[1])
    f.close()
    print(f'Horizontal position is: {h_position}')
    print(f'Depth is: {depth}')
    print(f'Both multiplied is: {h_position * depth}')


def part_2():
    h_position = 0
    depth = 0
    aim = 0
    with open("day_2_input.txt") as f:
        full_instructions = f.readlines()
        for i in full_instructions:
            current_instruction = i.split()
            if current_instruction[0] == "forward":
                h_position += int(current_instruction[1])
                depth = depth + (aim * int(current_instruction[1]))
            elif current_instruction[0] == "down":
                aim += int(current_instruction[1])
            else:
                aim -= int(current_instruction[1])
    f.close()
    print(f'Horizontal position is: {h_position}')
    print(f'Depth is: {depth}')
    print(f'Aim is: {aim}')
    print(f'Both multiplied is: {h_position * depth}')


if __name__ == "__main__":
    part_1()
