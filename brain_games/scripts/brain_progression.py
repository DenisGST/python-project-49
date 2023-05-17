#!/usr/bin/env python3
import prompt
import random


def main():
    flag = True
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, ", name, "!")
    while flag:
        print('What number is missing in the progression?')
        numb1 = random.randint(1, 10)
        numb2 = random.randint(numb1, numb1 + 10)
        print("Question:")
        for i in range(numb1, numb1 + 10):
            if i == numb2:
                print('.. ', end='')
            else:
                print(i, " ", end='')
        answer = prompt.string("\n Your answer:")
        if answer == str(numb2):
            print('Correct!')
        else:
            print(answer, " is wrong answer ;(. Correct answer was ", numb2)
            flag = False


if __name__ == '__main__':
    main()
