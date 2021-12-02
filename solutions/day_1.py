def part_1():
    increases = 0
    with open("day_1_input.txt") as f:
        measurements = f.readlines()
        old_measurement = -1
        for i in measurements:
            i = i.rstrip("\n")
            i = int(i)
            if old_measurement == -1:
                old_measurement = i
                print(f'{i} (N/A - no previous measurement)')
                continue
            else:
                if i > old_measurement:
                    increases += 1
                    print(f'{i} (increased)')
                elif i < old_measurement:
                    print(f'{i} (decreased)')
                else:
                    print(f'{i} (same)')
                old_measurement = i
    f.close()
    print(f'Number of increases: {increases}')


def part_2():
    increases = 0
    with open("day_1_input.txt") as f:
        measurements = f.readlines()
        for i in range(0, len(measurements)-1):
            print(i)
            if not i + 3 >= len(measurements):
                first_sum = int(measurements[i]) + int(measurements[i+1]) + int(measurements[i+2])
                second_sum = int(measurements[i+1]) + int(measurements[i+2]) + int(measurements[i+3])
                if second_sum > first_sum:
                    increases += 1
    f.close()
    print(f'Number of increases: {increases}')


if __name__ == "__main__":
    # part_1()
    part_2()
