#!/usr/bin/env python3
import prompt, random

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, ", name, "!")
    flag = True
    while flag:
        print('Answer "yes" if the number is even, otherwise answer "no".')
        numb = random.randint(1,100) 
        print("Question:",numb)
        answer = prompt.string("Your answer:")
        if (numb % 2 and answer == 'no')  or (not numb % 2 and answer == 'yes'): 
            print('Correct!')
        else :
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            flag = False




if __name__ == '__main__':
    main()
