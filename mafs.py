import time
import pathlib
import csv
import os.path
from typing import Iterator

# a question tuple beacuse type annotations were sad
class Q:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer if type(answer) == str else str(answer)


def quiz(name: str, questions: Iterator[Q], blocksize=20):
    pathlib.Path(f'data/{name}').mkdir(parents=True, exist_ok=True)
    path = os.path.join('data', name, f'{time.time():.0f}.csv')

    with open(path, 'a', newline='') as f:
        w = csv.writer(f)
        w.writerow(['question', 'answer', 'correct_answer', 'time'])

        print(f'solve {blocksize} {name} questions!')
        for i, q in enumerate(questions):
            print(q.question)
            start = time.time()
            answer = input('-> ')
            end = time.time()
            if answer == q.answer:
                print('Correct')
            else:
                print(f'Wrong, {q.question} was {q.answer}')

            w.writerow([q.question, answer, q.answer, round(end - start, 2)])

            if i == blocksize-1: break


