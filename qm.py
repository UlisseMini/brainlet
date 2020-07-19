import random
import pickle
import os
from typing import Dict

def quiz(questions: Dict[str, str]):
    try:
        num_correct = pickle.load(open('mafs.pkl', 'rb'))
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

def main():
    questions = {}
    for x in range(3, 10):
        for y in range(3, 10):
            questions[(f'{x} * {y}', f'{y} * {x}')] = str(x * y)

    quiz(questions)

if __name__ == '__main__':
    main()
