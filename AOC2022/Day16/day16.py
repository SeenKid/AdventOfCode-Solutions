import sys
import functools

sys.setrecursionlimit(10000)

FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def main():
    print(f"Using file {FILE}")
    with open(FILE, "r", encoding="utf-8") as f:
        state = {}
        for line in f:
            line = line.strip().split(" ")
            name = line[1]
            rate = int(line[4].split("=")[-1].split(";")[0])
            valves = [word.split(",")[0] for word in line[9:]]

            state[name] = {"rate": rate, "valves": valves}

        @functools.cache
        def part_one(opened, minutes, curr):
            if minutes <= 0:
                return 0

            best = 0
            s = state[curr]
            for valve in s["valves"]:
                best = max(best, part_one(opened, minutes - 1, valve))

            if curr not in opened and s["rate"] > 0 and minutes > 0:
                opened = set(opened)
                opened.add(curr)
                minutes -= 1
                new_sum = minutes * s["rate"]

                for valve in s["valves"]:
                    best = max(
                        best,
                        new_sum + part_one(frozenset(opened), minutes - 1, valve),
                    )

            return best

        @functools.cache
        def part_two(opened, minutes, curr):
            """
            TL;DR: Just do part one basically, then do it again once done to simulate the elephant.
            """

            if minutes <= 0:
                return part_one(opened, 26, "AA")

            best = 0
            s = state[curr]
            for valve in s["valves"]:
                best = max(best, part_two(opened, minutes - 1, valve))

            if curr not in opened and s["rate"] > 0 and minutes > 0:
                opened = set(opened)
                opened.add(curr)
                minutes -= 1
                new_sum = minutes * s["rate"]

                for valve in s["valves"]:
                    best = max(
                        best,
                        new_sum + part_two(frozenset(opened), minutes - 1, valve),
                    )

            return best

        # print(f"Part one: {part_one(frozenset(), 30, 'AA')}")
        print(f"Part two: {part_two(frozenset(), 26, 'AA')}")


main()
