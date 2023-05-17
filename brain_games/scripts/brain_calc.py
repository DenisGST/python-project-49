#!/usr/bin/env python3
import prompt
import random


def main():
    flag = True
    lst = ['+', '-', '*']

    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, ", name, "!")
    while flag:
        print('What is the result of the expression?')
        numb1 = random.randint(1, 10)
        numb2 = random.randint(1, 10)
        result = 0
        operation = random.choice(lst)
        print("Question:", numb1, ' ', operation, ' ', numb2)
        answer = prompt.string("Your answer:")
        if operation == "+":
            result = numb1 + numb2
        elif (operation == "-"):
            result = numb1 - numb2
        else:
            result = numb1 * numb2
        if (str(result) == answer):
            print('Correct!')
        else:
            print(answer, " is wrong answer ;(. Correct answer was ", result)
            flag = False


if __name__ == '__main__':
    main()
