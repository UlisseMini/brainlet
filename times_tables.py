import mafs
import random

def questions() -> mafs.Q:
    while True:
        n1 = random.randint(2, 9)
        n2 = random.randint(2, 9)
        yield mafs.Q(f'{n1} * {n2}', n1*n2)


def main():
    mafs.quiz('data/tt.csv', questions())


if __name__ == '__main__':
    main()
