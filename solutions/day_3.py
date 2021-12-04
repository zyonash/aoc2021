def part_1():
    zero_counter = [0] * 12
    one_counter = [0] * 12
    gamma_rate = [0] * 12
    epsilon_rate = [0] * 12
    with open("day_3_input.txt") as f:
        for i in f.read().splitlines():
            for j in range(0, len(i)):
                if i[j] == "0":
                    zero_counter[j] += 1
                else:
                    one_counter[j] += 1
        for i in range(0, len(zero_counter)):
            if zero_counter[i] > one_counter[i]:
                gamma_rate[i] = 0
                epsilon_rate[i] = 1
            else:
                gamma_rate[i] = 1
                epsilon_rate[i] = 0
    f.close()
    gamma = int(''.join(str(g) for g in gamma_rate), 2)
    epsilon = int(''.join(str(g) for g in epsilon_rate), 2)
    print(gamma * epsilon)


def part_2():
    og_rating = get_og_rating()
    co2_scrub_rating = get_co2_scrub_rating()
    print(int(og_rating[0], 2) * int(co2_scrub_rating[0], 2))


def get_og_rating():
    with open("day_3_input.txt") as f:
        sequence = f.read().splitlines()
        while len(sequence) > 1:
            zero_counter = [0] * 12
            one_counter = [0] * 12
            print(sequence)
            for j in range(0, len(sequence[0])):
                for i in sequence:
                    if i[j] == "0":
                        zero_counter[j] += 1
                    else:
                        one_counter[j] += 1
                if zero_counter[j] > one_counter[j]:
                    most_prevalent = "0"
                else:
                    most_prevalent = "1"
                print(f'Zero counter is: {zero_counter[j]}')
                print(f'One counter is: {one_counter[j]}')
                print(f'Most prevalent number in position {j} is {most_prevalent}.')
                sequence[:] = [i for i in sequence if i[j] != most_prevalent]
                if len(sequence) == 1:
                    break
            if len(sequence) == 1:
                break
        f.close()
        return sequence


def get_co2_scrub_rating():
    with open("day_3_input.txt") as f:
        sequence = f.read().splitlines()
        while len(sequence) > 1:
            print(sequence)
            zero_counter = [0] * 12
            one_counter = [0] * 12
            for j in range(0, len(sequence[0])):
                for i in sequence:
                    if i[j] == "0":
                        zero_counter[j] += 1
                    else:
                        one_counter[j] += 1
                if zero_counter[j] > one_counter[j]:
                    least_prevalent = "1"
                else:
                    least_prevalent = "0"
                print(f'Zero counter is: {zero_counter[j]}')
                print(f'One counter is: {one_counter[j]}')
                print(f'Least prevalent number in position {j} is {least_prevalent}.')
                sequence[:] = [i for i in sequence if i[j] != least_prevalent]
                if len(sequence) == 1:
                    break
            if len(sequence) == 1:
                break
        print(sequence)
        f.close()
        return sequence


if __name__ == "__main__":
    #part_1()
    part_2()
