{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "eeea2f39",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' Bagels, by Al Sweigart al@inventwithpython.com\\nA deductive logic game where you must guess a number based on clues.\\nView this code at https://nostarch.com/big-book-small-python-projects\\nA version of this game is featured in the book \"Invent Your Own \\nComputer Games with Python\" https://nostarch.com/inventwithpython\\nTags: short, game, puzzle'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\" Bagels, by Al Sweigart al@inventwithpython.com\n",
    "A deductive logic game where you must guess a number based on clues.\n",
    "View this code at https://nostarch.com/big-book-small-python-projects\n",
    "A version of this game is featured in the book \"Invent Your Own \n",
    "Computer Games with Python\" https://nostarch.com/inventwithpython\n",
    "Tags: short, game, puzzle\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f429a452",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9dd68357",
   "metadata": {},
   "outputs": [],
   "source": [
    "NUM_DIGITS= 3   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3ff44817",
   "metadata": {},
   "outputs": [],
   "source": [
    "MAX_GUESSES= 10 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "da13df0b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    print('''Bagels, a deductive logic game.\n",
    "    by Al Sweigart al@inventwithpython.com\n",
    "    I am thinking of a {}-digit number with no repeated digits.\n",
    "    Try to guess what it is. Here are some clues:\n",
    "    When I say:    That means:\n",
    "      Pico         One digit is correct but in the wrong position.\n",
    "      Fermi        One digit is correct and in the right position.\n",
    "      Bagels       No digit is correct.\n",
    "    For example, if the secret number was 248 and your guess was 843, the \n",
    "    clues would be Fermi Pico.'''.format(NUM_DIGITS))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f42d3663",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'getSecretNum' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_11876\\3351194567.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mwhile\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m     \u001b[0msecretNum\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mgetSecretNum\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'I have thought up a number.'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m' You have {} guesses to get it.'\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mMAX_GUESSES\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'getSecretNum' is not defined"
     ]
    }
   ],
   "source": [
    "    while True:\n",
    "        secretNum = getSecretNum()\n",
    "        print('I have thought up a number.')\n",
    "        print(' You have {} guesses to get it.'.format(MAX_GUESSES))\n",
    "        \n",
    "        numGuesses = 1\n",
    "        while numGuesses <= MAX_GUESSES:\n",
    "            guess = ''\n",
    "            while len(guess) != NUM_DIGITS or not guess.isdecimal():\n",
    "                print('Guess #{}: '.format(numGuesses))\n",
    "                guess = input('> ')\n",
    "                \n",
    "            clues = getClues(guess, secretNum)\n",
    "            print(clues)\n",
    "            numGuesses += 1\n",
    "            \n",
    "            if guess == secretNum:\n",
    "                break\n",
    "            if numGuesses > MAX_GUESSES:\n",
    "                print('You ran out of guesses.')\n",
    "                print('Thae answer was {}.'.format(secretNum))\n",
    "        print('Do you want to play again? (yes or no)')\n",
    "        if not input('> ').lower().startswith('y'):\n",
    "            break\n",
    "    print('Thanks for playing!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f564872",
   "metadata": {},
   "outputs": [],
   "source": [
    "def getSecretNum():\n",
    "    numbers = list('0123456789')\n",
    "    random.shuffle(numbers)\n",
    "    secretNum = ''\n",
    "    for i in range(NUM_DIGITS):\n",
    "        secretNum += str(numbers[i])\n",
    "    return secretNum    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d18cbbf9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def getClues(guess, secretNum):\n",
    "    if guess == secretNum:\n",
    "        return 'You got it!'\n",
    "    clues =[]\n",
    "    \n",
    "    for i in range(len(guess)):\n",
    "        if guess[i] == secretNum[i]:\n",
    "            clues.append('Fermi')\n",
    "        elif guess[i] in secretNum:\n",
    "            clues.append('Pico')\n",
    "    if len(clues) == 0:\n",
    "        return 'Bagels'\n",
    "    else:\n",
    "        clues.sort()\n",
    "        return ' '.join(clues)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c708da2b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bagels, a deductive logic game.\n",
      "    by Al Sweigart al@inventwithpython.com\n",
      "    I am thinking of a 3-digit number with no repeated digits.\n",
      "    Try to guess what it is. Here are some clues:\n",
      "    When I say:    That means:\n",
      "      Pico         One digit is correct but in the wrong position.\n",
      "      Fermi        One digit is correct and in the right position.\n",
      "      Bagels       No digit is correct.\n",
      "    For example, if the secret number was 248 and your guess was 843, the \n",
      "    clues would be Fermi Pico.\n"
     ]
    }
   ],
   "source": [
    "if __name__== '__main__':\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "86f0e69c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
