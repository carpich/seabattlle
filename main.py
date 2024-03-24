import random


class Field():

    def __init__(self):
        pass

    def show(self):
        field_size = [[" "] * 6 for i in range(6)]
        print()
        print("    | 1 | 2 | 3 | 4 | 5 | 6 |")
        print("  --------------------------- ")
        for i, row in enumerate(field_size):
            row_str = f"  {i + 1} | {' | '.join(row)} | "
            print(row_str)
            print("  --------------------------- ")
        print()


if __name__ == '__main__':

    human_field = Field()
    human_field.show()
