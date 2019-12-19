import random
print("Welcome to 21!")

dealer_cards = []
player_cards = []

# Dealer cards: while the number of cards the dealer has is 2, it will give 2 random numbers/cards
while len(dealer_cards) != 2:
	dealer_cards.append(random.randint(1,11))
	if len(dealer_cards) == 2:
		print("Dealer has X &", dealer_cards[1]) # shows the 2nd card because it is 1 in the list

# Player cards: while the number of cards the player has is 2, it will select 2 random card numbers between 1-11
while len(player_cards) != 2:
	player_cards.append(random.randint(1,11))
	if len(player_cards) == 2:
		print("Your cards are ", player_cards)

# Dealer cards: if the sum of cards the dealer has is 21, then the dealer automatically wins.  If the sum of cards the dealer has is greater than 21 then the dealer has busted and lost.
if sum(dealer_cards) == 21:
	print("Dealer has 21. Dealer WINS!")
elif sum (dealer_cards) > 21:
	print("Dealer BUSTED!")

while sum(player_cards) < 21:
	player_choice = str(input("Do you want to STAY or HIT? "))
	if player_choice == "HIT":
		player_cards.append(random.randint(1,11))
		print("Your new total is " + str(sum(player_cards)) + " from these cards ", player_cards)
	else:
		print("The dealer's total is " + str(sum(dealer_cards)) + " with ", dealer_cards)
		print("Your total is " + str(sum(player_cards)) + " with ", player_cards)
		if sum(dealer_cards) > sum(player_cards):
			print("Dealer WINS! You LOSE!")
			break
		else:
			print("You WIN!")
			break

	if sum(player_cards) > 21:
		print("You BUSTED! Dealer WINS!")
	elif sum(player_cards) == 21:
		print("You have 21! You WIN!")