import random
import pickle
import os
from typing import Dict

def quiz(name: str, questions: Dict[str, str]):
    try:
        num_correct = pickle.load(open(f'{name}.pkl', 'rb'))
    except:
        num_correct = {q: 0 for q in questions}

    try:
        while True:
            for question, answer in sorted(
                    random.sample(questions.items(), len(questions.items())),
                    key = lambda x: num_correct[x[0]],
            ):
                q = random.choice(question)
                print(q)
                user_answer = input('-> ')
                if user_answer == answer:
                    print('Correct')
                    num_correct[question] += 1
                else:
                    print(f'Wrong, {q} was {answer}')
    except Exception as e:
        print(e)
        pickle.dump(num_correct, open('mafs.pkl', 'wb'))

def quiz_times_table():
    questions = {}
    for x in range(3, 10):
        for y in range(3, 10):
            questions[(f'{x} * {y}', f'{y} * {x}')] = str(x * y)

    quiz('times-tbl', questions)

def quiz_2_digit_by_11():
    quiz(
        '2-by-11',
        {(f'{x} * 11', f'11 * {x}'): str(11*x) for x in range(10, 100)},
    )

if __name__ == '__main__':
    quiz_2_digit_by_11()
