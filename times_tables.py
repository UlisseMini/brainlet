import mafs
import random

def questions() -> mafs.Q:
    while True:
        n1 = random.randint(2, 9)
        n2 = random.randint(6, 9)

        yield random.choice([
            mafs.Q(f'{n1} * {n2}', n1*n2),
            mafs.Q(f'{n2} * {n1}', n1*n2),
        ])


def main():
    mafs.quiz('times tables', questions(), 100)


if __name__ == '__main__':
    main()
