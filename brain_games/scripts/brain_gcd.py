#!/usr/bin/env python3
import prompt
import random
import math


def main():
    flag = True
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, ", name, "!")
    while flag:
        print('Find the greatest common divisor of given numbers.')
        numb1 = random.randint(1, 100)
        numb2 = random.randint(1, 100)
        print("Question:", numb1, ' ', numb2)
        answer = prompt.string("Your answer:")
        result = math.gcd(numb1, numb2)
        if answer == str(result):
            print('Correct!')
        else:
            print(answer, " is wrong answer ;(. Correct answer was ", result)
            flag = False


if __name__ == '__main__':
    main()
