import random

max_die = 6

def roll(max_die):
   die1 = random.choice(range(1, max_die + 1))
   die2 = random.choice(range(1, max_die + 1))
   return die1, die2

next_r = {7:15, 22:25, 36:5}
next_u = {7:12, 22:28, 36:12}

chance_deck = []
chance_deck.append(0)
chance_deck.append(10)
chance_deck.append(11)
chance_deck.append(24)
chance_deck.append(39)
chance_deck.append(5)
chance_deck.append('R')
chance_deck.append('R')
chance_deck.append('U')
chance_deck.append('B')
chance_deck.append(None)
chance_deck.append(None)
chance_deck.append(None)
chance_deck.append(None)
chance_deck.append(None)
chance_deck.append(None)

random.shuffle(chance_deck)
chance_cursor = 0

def chance(current, cursor):
   draw = chance_deck[cursor]
   print draw
   new = current
   if draw != None:
      if draw == 'R': new = next_r[current]
      elif draw == 'U': new = next_u[current]
      elif draw == 'B': new = current - 3
      else: new = draw
   new_cursor = (cursor + 1) % 16
   return new, new_cursor
   


print chance(7, 0)


