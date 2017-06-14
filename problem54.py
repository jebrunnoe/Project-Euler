from collections import Counter
deck = open("p054_poker.txt", "r").read().split()

faces = {"T" : 10, "J" : 11, "Q" : 12, "K" : 13, "A" : 14}
ranks = {"11111" : 0, "1112" : 1, "122" : 2, "113" : 3, "23" : 6, "14" : 7}

class Card():
   def __init__(self, value, suit):
      if value.isalpha(): self.value = faces[value]
      else: self.value = int(value)
      self.suit = suit

class Hand():
   def __init__(self, cards):
      self.cards = sorted(cards, key = lambda x: x.value)
      self.rank = None
      self.straight = self.is_straight()
      self.flush = self.is_flush()
      self.rating = list()
   def is_straight(self):
      if all(self.cards[i + 1].value - self.cards[i].value == 1 for i in range(len(self.cards) - 1)): return True 
      else: return False
   def is_flush(self):
      suits = [card.suit for card in self.cards]
      if all(s == suits[0] for s in suits): return True
      else: return False
   def grade(self):
      if self.straight: self.rank = 4
      if self.flush: self.rank = 5
      if self.straight and self.flush: self.rank = 8      
      values = [card.value for card in self.cards]
      count = Counter(values)
      
      rev_values = values[::-1]
      comp = list()
      while len(rev_values) > 0:
	 high_c = 0
	 high_v = 0
	 for v in rev_values:
	    if count[v] > high_c: 
	       high_c = count[v]
	       high_v = v	 
	    if high_c <= 1: high_v = max(rev_values)
	 comp.append(high_v)
	 rev_values = filter(lambda a: a != high_v, rev_values)
      self.rating = comp

      frequency = sorted([str(count[i]) for i in set(values)])
      histogram = ''.join(frequency)
      score = ranks[histogram]
      if score > self.rank: self.rank = score

class Player():
   def __init__(self, hands):
      self.hands = hands
      self.wins = 0

player1 = Player([Hand([Card(deck[row * 10 + i][0], deck[row * 10 + i][1]) for i in range(5)]) for row in range(len(deck)/ 10)])
player2 = Player([Hand([Card(deck[row * 10 + i][0], deck[row * 10 + i][1]) for i in range(5, 10)]) for row in range(len(deck) / 10)])

for hand in player1.hands: hand.grade()
for hand in player2.hands: hand.grade()

def resolve(hand1, hand2):
   for card in range(len(hand1.rating)):
      if hand1.rating[card] > hand2.rating[card]: 
	 player1.wins += 1
	 return
      elif hand1.rating[card] < hand2.rating[card]: 
	 player2.wins += 1
	 return

def compete(player1, player2):
   for deal in range(1000):
      if player1.hands[deal].rank > player2.hands[deal].rank: player1.wins += 1
      elif player1.hands[deal].rank < player2.hands[deal].rank: player2.wins += 1
      elif player1.hands[deal].rank == player2.hands[deal].rank: resolve(player1.hands[deal], player2.hands[deal])

compete(player1, player2)
print player1.wins, player2.wins 

