import mafs
import random

def questions() -> mafs.Q:
    while True:
        n1 = random.randint(100, 999)
        n2 = random.randint(100, 999)
        yield mafs.Q(f'{n1} + {n2}', n1+n2)


def main():
    mafs.quiz('3 by 3 addition', questions())


if __name__ == '__main__':
    main()
