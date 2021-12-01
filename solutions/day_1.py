def main():
    increases = 0
    with open("day_1_input.txt") as f:
        measurements = f.readlines()
        old_measurement = -1
        for i in measurements:
            i = i.rstrip("\n")
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


if __name__ == "__main__":
    main()
