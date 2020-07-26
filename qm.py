import random
import pickle
import os
from typing import Dict

def combinations(iterable):
    for x in iterable:
        for y in iterable:
            yield (x, y)

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
        pickle.dump(num_correct, open(f'{name}.pkl', 'wb'))

def quiz_times_table():
    questions = {}
    for x in range(3, 10):
        for y in range(3, 10):
            questions[(f'{x} * {y}', f'{y} * {x}')] = str(x * y)

    quiz('times-tbl', questions)

"""
To multiply a two digit number by 11, add the digits and put the result in the middle

11 * 26 = 286

Carry if needed: 11 * 99 = 1089, 11 * 83 = 913
"""
def quiz_2_digit_by_11():
    quiz(
        '2-by-11',
        {(f'{x} * 11', f'11 * {x}'): str(11*x) for x in range(10, 100)},
    )

"""
To square a two digit number that ends in 5, you need to remember only two things.

1. The answer begins by multiplying the first digit by the next higher digit
2. The answer ends in 25

Example:
85 squared = 9*8 = 72 = 7225
"""
def quiz_square_endingin_5():
    quiz(
        'sq-endingin-5',
        {(f'{x}',): str(x**2) for x in range(15, 100, 10)}
    )


"""
When multiplying two digit numbers with the same first digit, and second digits that sum to 10.
The answer begins the same way that it did beforoe (the first digit multiplied by the next higher digit)
followed by the product of the second digits.
For example, let's try 83 * 87. (Both numbers begin with 8, and the last digits sum to 3 + 7 = 10.)
Since 8 * 9 = 72, and 3 * 7 = 21, the answer is 7221.
"""
def quiz_2digit_same_first_digit():
    pass


def quiz_addition(number_range):
    quiz(
        f'addition-{number_range}',
        {(f'{x} + {y}', f'{y} + {x}'): str(x + y) for x,y in combinations(list(number_range))}
    )


if __name__ == '__main__':
    quiz_addition(range(11, 1000))
