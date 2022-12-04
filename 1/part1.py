#!/usr/bin/env python3

def read_file_lines(path):
    with open(path, 'r') as f:
        return f.readlines()

def main():
    filepath = "sample.input"
    filepath = "main.input"
    file_lines = read_file_lines(filepath)

    elf_idx = 0
    calories_per_elf = [[]]

    for line in file_lines:
        line = line.strip()
        if len(line) > 0:
            calories_per_elf[elf_idx].append(int(line))
        else:
            elf_idx += 1
            calories_per_elf.append([])

    calories_total_per_elf = [sum(calories) for calories in calories_per_elf]

    print(max(calories_total_per_elf))

if __name__ == "__main__":
    main()
