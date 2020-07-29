import brainlet as bl
import random

def questions() -> bl.Q:
    while True:
        n1 = random.randint(100, 999)
        n2 = random.randint(100, 999)
        yield bl.Q(f'{n1} + {n2}', n1+n2)


def main():
    bl.quiz('3 by 3 addition', questions())


if __name__ == '__main__':
    main()
