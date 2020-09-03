# Start with basics in Python

#Part 1
# Name: birthday_song
# Purpose: birthday_song prints out a personalized birthday song
# Input: name, string 
# Returns: none 
user_name = input("What's your name? ")
def birthday_song(user1):
    print("Happy birthday to you,\nHappy birthday to you,\nHappy birthday dear " + str(user_name) + "!\nHappy birthday to you!"  )
birthday_song(user_name)

#Part 2 Play a card game
print("\nWe are playing a game of cards!")
number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suit = ['Spades', 'Clubs', 'Diamonds', 'Hearts']

def card_game():
  import random
  card_picker = 0
  card_generator = [" ", " ", " ", " ", " "]
  
  def card_picked(numb, su):
    return numb + " of " + su
  while card_picker <= 4:
    number_picker = random.randint(0,12)
    suits_picker = random.randint(0,3)
    card_generator[card_picker] = card_picked(number[number_picker], suit[suits_picker])
    card_picker += 1
    
  print(card_generator)

card_game() # Part 3 Calling card game() function.

