#!/usr/bin/env python3

first_col_map = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

second_col_map = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

# 1st col = Opponent
# 2nd col = Us
output_map = {
    ("rock", "rock") : "draw",
    ("rock", "paper"): "win",
    ("rock", "scissors"): "loss",

    ("paper", "rock") : "loss",
    ("paper", "paper"): "draw",
    ("paper", "scissors"): "win",

    ("scissors", "rock") : "win",
    ("scissors", "paper"): "loss",
    ("scissors", "scissors"): "draw",
}

result_to_points = {
    "loss" : 0,
    "draw": 3,
    "win": 6
}

choice_to_points = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

def read_file_lines(path):
    with open(path, 'r') as f:
        return f.readlines()

def main():
    filepath = "sample.input"
    filepath = "main.input"
    file_lines = read_file_lines(filepath)


    score = 0
    for line in file_lines:
        line = line.strip()

        choice_1, choice_2 = line.split(" ")

        choice_1 = first_col_map[choice_1]
        choice_2 = second_col_map[choice_2]

        result = output_map[(choice_1, choice_2)]
        points = result_to_points[result] +  choice_to_points[choice_2]

        print(f"{choice_1} {choice_2} -> {result} -> {points=}")
        score += points

    print(f"Score : {score}")

if __name__ == "__main__":
    main()
