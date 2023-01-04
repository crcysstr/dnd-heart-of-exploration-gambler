# DND-HEART OF EXPLORATION-GAMBLER
Gambler Class Docs

## Premise
This code is used to operate the custom class Gambler that is used in the Dungeons and Dragons Campaign Heart of Exploration. The main purpose is to simulate a virtual deck of cards to be used in performing skills that vary based on the specific cards drawn.

## Abilities
The program can be used to pilot the class, which includes the following abilities:
* Calculated Risk: Draw a card and use its effects, or instead throw the card to deal damage
* Greedy Draw: Draw 2 cards and use their effects
* Quick Draw: Draw a card and use its effects
* Cheat the Flop: Draw 4 cards, choose to discard 1, and then use the card values to heal allies
* Lucky 7: Roll 3d4, and mill that many cards. If there are at least 3 7's among them, restore 7 health to allies in a 7 foot radius.
* Desperate Deck Out: When you run out of cards, lose half your curent health, refill your deck, and cast Greedy Draw with lifesteal
* Poker Hand: Shuffle your deck, then draw 5 cards. Based on the Poker Hand, perform various effects
* Fresh Start: Shuffle the discard pile into your deck
* Fold: Draw a card. Heal yourself based on the value. Shuffle the discard pile into your deck.
* Bluff: If you pass the bluff check, increase the values of your cards drawn.
* Mill: Remove the top 1d6 cards of your deck
* Subtle Swap: Shuffle the discard pile, then swap the deck and the discard pile for one turn.
* Predict: Look at three random cards in your deck and place one at the top. The other two are placed at the bottom.
* Stack the Deck: Reorder the top 1d4+1 cards of your deck
* Reverse Draw: Draw your next card from the bottom of the deck
* Random Refresh: Randomly draw 3 cards from your discard pile and shuffle them back into the deck
* Ride the Bus: If there are 4 or more cards in the discard pile, call the color, high/low, in/out, and suite using 4 cards in the discard pile.
* Blackjack: Play blackjack using the cards in the discard pile. Depending on the results of the game, perform various effects. Shuffle used cards back into the deck.