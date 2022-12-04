#!/usr/bin/env python3

NB_LINES_PER_GROUP=3

def read_file_lines(path):
    with open(path, 'r') as f:
        return [l.strip() for l in f.readlines()]

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

    groups = []

    for i in range(0, len(file_lines), NB_LINES_PER_GROUP):
        groups.append([])
        for line in file_lines[i:i+NB_LINES_PER_GROUP]:
            groups[-1].append(set(line))

    priority_sum = 0
    for group in groups:
        # FIXME : Can there be more than 1 letter in common ?
        common = list(set.intersection(*group))[0]

        print(f"{common=}")
        priority_sum += get_priority(common)

    print(f"{priority_sum=}")

if __name__ == "__main__":
    main()
