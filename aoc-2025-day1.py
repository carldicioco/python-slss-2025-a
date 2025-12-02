# AOC Day 1: Part 1
# Author: Carl Dicioco
# 1 December


def part_one():
    cur_location = 50
    count_zero = 0

    with open("data/aoc-2025-day1.txt") as f:
        for line in f:
            line = line.strip()
            direction = line[0]
            distance = int(line[1:])

            if direction == "R":
                cur_location = (cur_location + distance) % 100
            else:
                cur_location = (cur_location - distance) % 100

            if cur_location == 0:
                count_zero += 1

    print("Password:", count_zero)


def part_two():
    pass


if __name__ == "__main__":
    part_one()
