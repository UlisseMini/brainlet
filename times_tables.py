import brainlet as bl
import random

def questions() -> bl.Q:
    while True:
        n1 = random.randint(2, 9)
        n2 = random.randint(6, 9)

        yield random.choice([
            bl.Q(f'{n1} * {n2}', n1*n2),
            bl.Q(f'{n2} * {n1}', n1*n2),
        ])


def main():
    bl.quiz('times tables', questions(), 100)


if __name__ == '__main__':
    main()
