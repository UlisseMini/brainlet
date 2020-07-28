import time
import csv
import os.path
from typing import Iterator

# a question tuple beacuse type annotations were sad
class Q:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer if type(answer) == str else str(answer)


def quiz(path: str, questions: Iterator[Q]):
    # write the header if t he fiel does not exist
    # note if directory this will be sad
    if not os.path.isfile(path):
        with open(path, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['question', 'answer', 'correct_answer', 'time'])


    with open(path, 'a', newline='') as f:
        w = csv.writer(f)

        for q in questions:
            start = time.time()
            print(q.question)
            answer = input('-> ')
            if answer == q.answer:
                print('Correct')
            else:
                print(f'Wrong, {q.question} was {q.answer}')

            w.writerow([q.question, answer, q.answer, round(time.time() - start, 2)])


