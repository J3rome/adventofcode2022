#!/usr/bin/env python3

def read_file_lines(path):
    with open(path, 'r') as f:
        return [l.strip() for l in f.readlines()]

def get_pos_set_from_range_str(range_str):
    start, stop = range_str.split("-")
    return set(range(int(start), int(stop)+1))

def main():
    filepath = "sample.input"
    filepath = "main.input"
    file_lines = read_file_lines(filepath)

    nb_overlap = 0

    for line in file_lines:
        first_elf_range, second_elf_range = line.split(",")

        first_elf_pos = get_pos_set_from_range_str(first_elf_range)
        second_elf_pos = get_pos_set_from_range_str(second_elf_range)

        print(f"{first_elf_pos=}")
        print(f"{second_elf_pos=}")

        nb_common = len(first_elf_pos.intersection(second_elf_pos))

        print(f"{nb_common=}")

        if nb_common > 0:
            print("Overlap !")
            nb_overlap += 1

        print("-"*30)

    print(f"\n{nb_overlap=}")

if __name__ == "__main__":
    main()
