import random
from replit import clear
from art import logo

global Cards
Cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_initial_cards():
  return random.sample(Cards, 2)

def deal_cards():
  return random.choice(Cards)

def ace_check(player):
  if sum(player) > 21 and 11 in player:
    return True

def blackjack_check(player):
  if sum(player) == 21:
    return True

def play_game():

  print(logo)
  
  player_cards = deal_initial_cards()
  if ace_check(player_cards):
    player_cards.remove(11)
    player_cards.append(1)

  dealer_cards = deal_initial_cards()
  if ace_check(dealer_cards):
    dealer_cards.remove(11)
    dealer_cards.append(1)

  take_card = 'y'
  
  while  take_card == 'y':
    print(f"Your cards: {player_cards}. Your current score: {sum(player_cards)}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    take_card = input('Do you to take a card: "y" or "n" ')
    if take_card == 'y':
      player_cards.append(deal_cards())
    if take_card =='y' and  sum(player_cards) > 21:
      take_card = 'n'

  while sum(dealer_cards) < 17:
    dealer_cards.append(deal_cards())

  print(f'Final score:\nYour score - {sum(player_cards)}\nDealer\'s score - {sum(dealer_cards)}')

  if sum(player_cards) == sum(dealer_cards):
    print('It\'s a draw')
  elif blackjack_check(player_cards):
    print('Yay! You Win😁👍')
  elif blackjack_check(dealer_cards):
    print('Dealer got a black jack, You loose😭')
  elif sum(player_cards) > 21:
    print('You went over. You loose😭')
  elif sum(dealer_cards) > 21:
    print('Dealer went over. You Win😁👍')
  elif sum(player_cards) < 21 and sum(player_cards) > sum(dealer_cards):
    print('Yay! You Win😁👍')
  else:
    print('You Loose')

while input('Do you want to play BlackJack: "y" or "n": ') == 'y':
  clear()
  play_game()
