stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

word_list = ["dangal", "dunki", "drishyam", "bahubali", "chichore", "animal"]

player_lives = 6

import random

chosen_word = random.choice(word_list)
print(chosen_word)

word_length = len(chosen_word)

blanks = ""
for p in range(word_length):
  blanks += "_"

print(blanks)

gameOver = False
correct_alphabets = []

while not gameOver:
  guess = input("Guess a letter:").lower()

  display = ""

  for letter in chosen_word:
    if letter == guess:
      display += letter
      correct_alphabets.append(letter)
    elif letter in correct_alphabets:
      display += letter
    else:
      display += "_"

  print(display)

  if guess not in chosen_word:
    player_lives -= 1
    if player_lives == 0:
      gameOver = True
      print("You lose")

  if "_" not in display:
    gameOver = True
    print("You Won")

  print(stages[player_lives])
