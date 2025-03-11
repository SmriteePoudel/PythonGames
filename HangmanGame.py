{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "0fbff155-301b-471d-8b74-a022262e0a5d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Hangman!\n",
      "_ _ _ _ _ _ _ _ _ _\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a letter:  o\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "_ _ _ _ _ _ _ o _ _\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a letter:  u\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "u _ _ _ u _ _ o u _\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a letter:  t\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "u _ _ _ u _ t o u _\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a letter:  i\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "u _ i _ u i t o u _\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a letter:  ubiquitous\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "u _ i _ u i t o u _\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a letter:  b\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "u b i _ u i t o u _\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a letter:  i\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You've already guessed this letter.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a letter:  q\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "u b i q u i t o u _\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a letter:  s\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "u b i q u i t o u s\n",
      "You Win!!! 🎉\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "words = [\n",
    "    \"Apple\",\n",
    "    \"Table\",\n",
    "    \"Bright\",\n",
    "    \"Journey\",\n",
    "    \"Whisper\",\n",
    "    \"Perception\",\n",
    "    \"Exaggerate\",\n",
    "    \"Metamorphosis\",\n",
    "    \"Ubiquitous\",\n",
    "    \"Ephemeral\"\n",
    "]\n",
    "\n",
    "\n",
    "chosen_word = random.choice(words).lower()\n",
    "lives = 6\n",
    "display = [\"_\"] * len(chosen_word)\n",
    "game_over = False\n",
    "\n",
    "print(\"Welcome to Hangman!\")\n",
    "print(\" \".join(display))\n",
    "\n",
    "while not game_over:\n",
    "    guessed_letter = input(\"Guess a letter: \").lower()\n",
    "\n",
    "    if guessed_letter in display:\n",
    "        print(\"You've already guessed this letter.\")\n",
    "        continue\n",
    "\n",
    "    if guessed_letter in chosen_word:\n",
    "        for position in range(len(chosen_word)):\n",
    "            if chosen_word[position] == guessed_letter:\n",
    "                display[position] = guessed_letter\n",
    "    else:\n",
    "        lives -= 1\n",
    "        print(f\"Wrong guess! Lives left: {lives}\")\n",
    "\n",
    "    print(\" \".join(display))\n",
    "\n",
    "    if \"_\" not in display:\n",
    "        game_over = True\n",
    "        print(\"You Win!!! 🎉\")\n",
    "    elif lives == 0:\n",
    "        game_over = True\n",
    "        print(f\"You Lose!!! The word was '{chosen_word}'.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8ed468fc-b313-445e-8b34-f87acd511f78",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'word' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[10], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m chosen_word\u001b[38;5;241m=\u001b[39mrandom\u001b[38;5;241m.\u001b[39mchoice(word)\u001b[38;5;241m.\u001b[39mlower()\n\u001b[0;32m      2\u001b[0m lives\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m6\u001b[39m\n\u001b[0;32m      3\u001b[0m display\u001b[38;5;241m=\u001b[39m[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m_\u001b[39m\u001b[38;5;124m\"\u001b[39m]\u001b[38;5;241m*\u001b[39m\u001b[38;5;28mlen\u001b[39m(chosen_word)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'word' is not defined"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "1f8be66f-d452-4e2b-ad76-3cb36a324145",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to game\n",
      "\n"
     ]
    }
   ],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ed747df-553f-482b-92a0-cc2e9b7c14d7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "68e20ecf-df23-4786-b36f-225c0bbe5f35",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
