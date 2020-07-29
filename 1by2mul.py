import brainlet as bl
import random

def questions() -> bl.Q:
    while True:

        n1 = random.randint(2, 9)
        n2 = random.randint(11, 99)
        yield bl.Q(f'{n1} * {n2}', n1*n2)


def main():
    bl.quiz('one by two multiplication', questions())


if __name__ == '__main__':
    main()
