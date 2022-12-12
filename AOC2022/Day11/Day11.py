import collections
import copy
import math
import pathlib
import re


class Monkey:
    def __init__(
        self,
        id: int,
        starting_items: list[int],
        worry_operation_text: str,
        test_val: int,
        item_reciever: dict[bool, int],
    ) -> None:
        self.id = id
        self.items = collections.deque(starting_items)
        self.worry_operation = lambda old: eval(worry_operation_text)
        self.test_val = test_val
        self.item_reciever = item_reciever
        self.inspect_counter = 0

    def throw_item(self, worry_reducer: int | None) -> tuple[int, int]:
        self.inspect_counter += 1
        # inspect item
        item = self.items.popleft()
        item = self.worry_operation(item)
        if worry_reducer is None:
            # bored with item
            item //= 3
        else:
            item %= worry_reducer

        return item, self.item_reciever[item % self.test_val == 0]

    def recieve_item(self, item: int):
        self.items.append(item)


def main():
    file_path = pathlib.Path(__file__)
    with open("input.txt") as file:
        monkeys: dict[int, Monkey] = {}
        try:
            while True:
                assert (match := re.match(r"Monkey (\d)", next(file)))
                monkey_id = int(match.group(1))
                assert (
                    match := re.search(
                        r"Starting items: (\d+(?:[ \t]*,[ \t]*\d+)*)", next(file)
                    )
                )
                starting_items = list(map(int, match.group(1).split(", ")))
                assert (match := re.search(r"Operation: new = (.*)", next(file)))
                worry_operation_text = match.group(1)
                assert (match := re.search(r"Test: divisible by (\d+)", next(file)))
                test_val = int(match.group(1))
                assert (
                    match := re.search(r"If true: throw to monkey (\d+)", next(file))
                )
                true_reciever = int(match.group(1))
                assert (
                    match := re.search(r"If false: throw to monkey (\d+)", next(file))
                )
                false_reciever = int(match.group(1))
                recievers = {True: true_reciever, False: false_reciever}
                monkeys[monkey_id] = Monkey(
                    monkey_id, starting_items, worry_operation_text, test_val, recievers
                )
                assert next(file).strip() == ""

        except StopIteration:
            pass

    calculate_monkey_business(copy.deepcopy(monkeys))
    calculate_monkey_business(
        monkeys, worry_reducer=math.prod(monkey.test_val for monkey in monkeys.values())
    )


def calculate_monkey_business(
    monkeys: dict[int, Monkey], worry_reducer: int | None = None
):
    for _ in range(20 if worry_reducer is None else 10000):
        for monkey in monkeys.values():
            while monkey.items:
                item, reciever = monkey.throw_item(worry_reducer=worry_reducer)
                monkeys[reciever].recieve_item(item)

    inspection_counts = sorted(monkey.inspect_counter for monkey in monkeys.values())
    print(inspection_counts[-1] * inspection_counts[-2])


if __name__ == "__main__":
    main()