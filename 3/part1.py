#!/usr/bin/env python3

def read_file_lines(path):
    with open(path, 'r') as f:
        return f.readlines()

def get_priority(letter: str):
    if letter.isupper():
        offset = 27
        reference = ord('A')
    else:
        offset = 1
        reference = ord('a')

    return ord(letter) - reference + offset

def main():
    filepath = "sample.input"
    filepath = "main.input"
    file_lines = read_file_lines(filepath)

    priority_sum = 0
    for line in file_lines:
        line = line.strip()
        line_len = len(line)
        if line_len % 2 != 0:
            print("[ERROR] Can't handle odd number of packages...")
            exit(1)

        compartment_len = line_len//2

        first_compartment = set(line[:compartment_len])
        second_compartment = set(line[compartment_len:])

        common = list(first_compartment.intersection(second_compartment))

        # FIXME : Can there be more than 1 letter in common ?
        priority = get_priority(common[0])

        priority_sum += priority

        print(f"{''.join(first_compartment)} -- {''.join(second_compartment)} --> {common} --> {priority=}")

    print(f"{priority_sum=}")

if __name__ == "__main__":
    main()
