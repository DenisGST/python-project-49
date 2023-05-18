#!/usr/bin/env python3
import prompt
import random


def main():
    flag = True
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, ", name, "!")
    while flag:
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        numb1 = random.randint(1, 100)
        print("Question:", numb1)
        answer = prompt.string("Your answer:")
        result = IsPrime(numb1)
        if answer == result:
            print('Correct!')
        else:
            print(answer, " is wrong answer ;(. Correct answer was ", result)
            flag = False


def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    if (d ==n ):
        return 'yes'
    else:
        return 'no'


if __name__ == '__main__':
    main()
