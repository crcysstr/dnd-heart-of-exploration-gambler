### lucas hsu
### dnd heart of exploration gambler class
### ver: 4.5
### date: 8/14

### imported levels
import random
from typing import Coroutine, ValuesView

### jshoung stats
DEX = 2
INT = 3
CHA = 5
PROF = 3
level = 8
hitR = 25
docD = 10

### X, X/2 setup
if (level/2 > int(level/2)):
    X = int(level/2)+1
else:
    X = int(level/2)

if (X/2 > int(X/2)):
    X2 = int(X/2)+1
else:
    X2 = int(X/2)

### deck setup
deck = list(range(1,55))
random.shuffle(deck)
discard = list()

### bluff, crit, swapped
bluff = [False, 2]
crit = False
swapped = False

### for if you want to roll dice on your own
selfroll = False

### draws a card
def cardDraw():

    ### global variables used
    global discard
    global deck
    
    ### draw card
    rCard = deck.pop()
    discard.append(rCard)
    interpret(rCard)
    if (rCard == 17):
        print("\n!!!4 of Diamonds Drawn, gain Lifesteal!!!\n")

    if (rCard == 54):
        print("\nJoker Drawn, trigger Side Pot!\n")

    val = (rCard - 1) % 13 + 1
            
    if (val == 1 or val == 11 or val == 12 or val == 13):
        print("\nRoyal Drawn, trigger Side Pot!\n")

    ### if deck has been emptied
    size = len(deck)

    if (size == 0):
        
        if (swapped):
            print("Ran out of cards in swapped deck, swapping back!")
            unSwap()
            return rCard

        print("\nDesperate Deck Out!")
        print("Lose half your current health, refilling, casting Greedy Draw:")
        refill()
        greedyDraw()
        print()

    return rCard

### draws a card from discard
def discDraw():

    global discard

    rCard = discard.pop()
    interpret(rCard)

    return rCard

### displays the effect of a given card
def cardEffect(cardN):

    ### global variables used
    global discard
    global deck
    global X
    global X2
    global hitR

    critMod = critCheck()

    ### blank
    if (cardN == 53):
        print("All Allies lose 1 AC")
        print("All Allies are poisoned, taking 1d10 for {0} turns".format(X))
        print("All Allies rooted for {0} turns".format(X))
        print("All allies take an extra {0} dies of damage".format(X2))
        print()
        return

    ### joker
    if (cardN == 54):
        print("Inflict AC-1 on a target within {0} meters".format(hitR))
        print("Increase hit by {0}".format(X))
        print("Inflict poison, dealing 1d10 for {0} turns on a target within {1} meters".format(X, hitR))
        print("Heal {0} to a target within {1} meters".format(roll(4,X*critMod,0), hitR))
        print("Root for {0} turns".format(X))
        print("Give an ally within {0} meters 10 speed".format(hitR))
        print("Deal an extra {0} dies of damage".format(X2))
        print("Crit +{0}".format(X2))
        print()
        return
    
    ### all others
    suit = int((cardN-1)/13)
    val = cardN - int(cardN/13)*13
    
    if (val == 1):
        if (suit == 0 or suit == 3):
            print("Deal an extra {0} dies of damage".format(X2))
        else:
            print("Crit +{0}".format(X2))
    elif (val == 2):
        print("Decrease your AC by 1 for 1 turn")
    elif (val == 3):
        print("Take {0} damage".format(roll(4,2,0)))
    elif (val == 4):
        print("Decrease speed by 5 and take {0} damage".format(roll(4,1,0)))
    elif (val == 5):
        print("Take {0} damage".format(roll(4,1,0)))
    elif (val == 6):
        print("Nothing happens.")
    elif (val == 7):
        print("Nothing happens.")
    elif (val == 8):
        print("Deal {0} to target. Take {1} damage".format(roll(6,X*critMod,0),roll(4,2,0)))
    elif (val == 9):
        print("Increase your speed by 5 and deal {0} to target".format(roll(4,X*critMod,0)))
    elif (val == 10):
        print("Deal {0} to target and heal {1} to a target".format(roll(8,X*critMod,0),roll(4,X*critMod,0)))
    elif (val == 11):
        if (suit == 0 or suit == 3):
            print("Inflict AC-1 on a target within {0} meters".format(hitR))
        else:
            print("Increase hit by {0}".format(X))
    elif (val == 12):
        if (suit == 0 or suit == 3):
            print("Inflict poison, dealing 1d10 for {0} turns on a target within {1} meters".format(X, hitR))
        else:
            print("Heal {0} to a target within {1} meters".format(roll(4,X*critMod,0), hitR))
    elif (val == 0):
        if (suit == 0 or suit == 3):
            print("Root for {0} turns".format(X))
        else:
            print("Give an ally within {0} meters 10 speed".format(hitR))
    else:
        print("Error.")

### refills your deck with discard
def refill():

    ### global variables used
    global deck
    global discard

    ### empties discard, fills deck, shuffles
    for i in discard:
        deck.append(i)

    discard = []
    random.shuffle(deck)

    ### output
    print("Shuffled!\n")

### reads in the number of a card
### prints out the actual card represented
def interpret(cardN):

    ### printing
    if (cardN < 1 or cardN > 54):
        print("INVALID")
    else:
        if (cardN == 53):
            print("Blank Card")
        elif (cardN == 54):
            print("Joker")
        else:
            out = ""
            
            suit = int((cardN-1)/13)
            val = (cardN - 1) % 13 + 1
            
            if (val == 1):
                out += "Ace of "
            elif (val == 11):
                out += "Jack of "
            elif (val == 12):
                out += "Queen of "
            elif (val == 13):
                out += "King of "
            else:
                out += str(val) + " of "

            if (suit == 0):
                out += "Clubs"
            elif (suit == 1):
                out += "Diamonds"
            elif (suit == 2):
                out += "Hearts"
            else:
                out += "Spades"

            print(out)

### Calculated Risk
### Level 1 Ability
def calcRisk():

    ### shows card drawn
    print("Calculated Risk, Card Drawn:\n")
    card = cardDraw()

    card = bluffCheck(card, 2)

    ### loops til good input
    while (True):
        
        ### input
        print("To play, enter 1. To throw, enter 2.")
        ipt = input()

        ### card effect used
        if (ipt == "1"):
            print("Hit Roll: {0}".format(roll(20, 1, INT+PROF)))
            cardEffect(card)
            unSwap()
            return
        
        ### card thrown
        elif (ipt == "2"):
            print("Hit Roll: {0}".format(roll(20, 1, INT+PROF)))
            if (card == 53):
                val = 0
            elif (card == 54):
                val = 11
            else:
                val = (card - 1) % 13 + 1
                if (val > 10):
                    val = 10
            print("Damage: {0}".format(INT+val))
            unSwap()
            return

### Greedy Draw
### Level 1 Ability
def greedyDraw():

    ### checks for at least 2 cards in deck
    if (invalid(2)):
        return

    ### prints and draws 2 cards
    print("Greedy Draw, 2 Cards drawn:\n")

    cards = []
    cards.append(cardDraw())
    cards.append(cardDraw())

    cards = multiBluffCheck(cards, 2)
    for i in cards:
        cardEffect(i)

    unSwap()

### Quick Draw
### Level 1 Ability
def quickDraw():

    print("Quick Drawing, Card drawn:\n")

    ### draws a card
    card = cardDraw()
    card = bluffCheck(card, 1)
    cardEffect(card)

    unSwap()

### Cheat the Flop
### Level 2 Ability
def cheatFlop():

    print("Cheat the Flop, 4 Cards drawn:\n")

    ### checks for 4 cards
    if (invalid(4)):
        return
    
    ### draws 4 cards
    cards = []
    cards.append(cardDraw())
    cards.append(cardDraw())
    cards.append(cardDraw())
    cards.append(cardDraw())

    cards = multiBluffCheck(cards, 2)

    ### interprets cards
    vals = []
    for i in cards:
        if (i == 53):
            vals.append(0)
        elif (i == 54):
            vals.append(12)
        else:
            val = (i - 1) % 13 + 1
            if (val >= 10):
                vals.append(10)
            elif (val == 1):
                vals.append(11)
            else:
                vals.append(val)

    vals.sort()
    
    ### output
    print("Heal 3 of {0}".format(vals))

    unSwap()

### Fold
### Level 3 Ability
def fold():

    print("Folding, card drawn:\n")

    ### draws card
    card = cardDraw()

    ### processes
    if (card == 53):
        val = 0
    elif (card == 54):
        val = 12
    else:
        tval = (card - 1) % 13 + 1
        if (tval >= 10):
            val = 10
        elif (tval == 1):
            val = 11
        else:
            val = tval

    ### heals, refills
    print("Heal {0}".format(roll(4,12-val,0)))
    refill()

    unSwap()

### Bluff
### Level 3 Ability
def startBluff():

    ### flips bluff[0] to true, sets bluff[1] to 2
    global bluff
    bluff[0] = True
    bluff[1] = 1

    print("Bluff Active!")

### Bluff helper
### checks if a single card needs to be bluffed
def bluffCheck(card, num):
    
    ### gets bluff
    global bluff

    ### checks if bluffing needs to stop
    ext = unBluff(num)

    ### if bluffing needs to instastop, does so
    if (ext == 2):
        print("\nYou exited bluff by using another action.\n")
        return card

    ### if bluffing is good:
    if bluff[0]:

        ### shows bluff
        print("\nBluffed!")

        ### gets value
        val = card - int(card/13) * 13

        ### changes or doesn't change as needed
        if (card == 54):
            print("Stays at:", end = " ")
            interpret(card)
            print("Cast Twice!")
        elif (card == 53):
            print("Blank Card bluffed to Joker!")
            card = 54
        elif (val >= 2 and val <= 7):
            card += 3
            print("Bluffed to:", end = " ")
            interpret(card)
        elif (val == 8):
            card += 2
            print("Bluffed to:", end = " ")
            interpret(card)
        else:
            print("Stays at:", end = " ")
            interpret(card)
            print("Cast Twice!")

    ### if bluffing is done, says so and flips bluff
    if (ext == 1):
        print("You exited bluff by using 2 (bonus) actions")
        bluff[0] = False

    ### output
    print()
    return card

### Bluff helper
### checks if multiple cards need to be bluffed
def multiBluffCheck(cards, num):
    
    ### gets bluff
    global bluff

    ### checks if bluffing needs to stop
    ext = unBluff(num)

    ### if bluffing needs to instastop, does so
    if (ext == 2):
        print("\nYou exited bluff by using another action\n")
        return cards

    ### if bluffing is good:
    if bluff[0]:

        ### shows bluff
        print("\nBluffed!")

        ### for each of the cards:
        for i in range(0, len(cards)):

            ### gets value
            val = cards[i] - int(cards[i]/13) * 13

            ### changes or doesn't change as needed
            if (cards[i] == 54):
                print("Stays at: Joker")
                print("Cast Twice!")
            elif (cards[i] == 53):
                print("Blank Card bluffed to Joker!")
                cards[i] = 54
            elif (val >= 2 and val <= 7):
                cards[i] += 3
                print("Bluffed to:", end = " ")
                interpret(cards[i])
            elif (val == 8):
                cards[i] += 2
                print("Bluffed to:", end = " ")
                interpret(cards[i])
            else:
                print("Stays at:", end = " ")
                interpret(cards[i])

    ### if bluffing is done, says so and flips bluff
    if (ext == 1):
        print("You exited bluff by using 2 (bonus) actions")
        bluff[0] = False
    
    ### output
    print()
    return cards

### Bluff helper
### checks if multiple cards need to be bluffed
def pokerBluffCheck():
    
    ### gets bluff
    global bluff

    bluffed = False

    ### checks if bluffing needs to stop
    ext = unBluff(2)

    ### if bluffing needs to instastop, does so
    if (ext == 2):
        print("\nYou exited bluff by using another action\n")
        return bluffed

    ### if bluffing is good:
    if bluff[0]:

        ### shows bluff
        print("\nBluffed!")

        bluffed = True

    ### if bluffing is done, says so and flips bluff
    if (ext == 1):
        print("You exited bluff by using 2 (bonus) actions")
        bluff[0] = False
    
    ### output
    print()
    return bluffed

### Bluff helper function
### checks if bluffing needs to stop
def unBluff(num):

    ### vars
    global bluff
    out = 0

    ### if bluffing
    if bluff[0]:

        ## 2 bonus actions can be cast after bluffing
        if (num == 1):

            ### decrements 
            bluff[1] -= 0.4
    
        ### 1 action can be cast after bluffing
        elif (num == 2):
            if (bluff[1] - 0.6) >= 0:
                bluff[1] -= 0.6
            else:
                out = 2
                bluff[0] = False

        else:
            print("ERROR- UNBLUFF")

        ### if bluff needs to stop
        if bluff[1] <= 0.2:
            out = 1

    ### output
    return out

### Poker Hand
### Level 4 Ability
def pokerHand():

    ### needs 5 cards
    if (invalid(5)):
        return

    ### bluff stuff
    bm = 0
    if (pokerBluffCheck()):
        bm = 3

    ### draws your hands
    cards = []
    print("Your hand:\n")
    for i in range(0, 5):
        cards.append(cardDraw())
    print()

    ### checks for wilds, uses appropriate process
    if ((53 in cards) and (54 in cards)):
        results = doubleWildPokerProcess(cards)
    if ((53 in cards) or (54 in cards)):
        results = wildPokerProcess(cards)
    else:
        results = pokerProcess(cards)

    ### names to be pulled
    cardNames = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes", "Sevens"]
    cardNames += ["Eights", "Nines", "Tens", "Jacks", "Queens", "Kings"]
    suitNames = ["Clubs", "Diamonds", "Hearts", "Spades"]
    resultNames = ["Pair of", "Two Pair of", "Three of a Kind of", "straight", "flush"]
    mods = [INT, INT+DEX, INT+DEX+CHA]

    ### high card
    if (results[0] == 0):
        if (bm > 0):
            print("High Card. Bluffing negated the damage.")
        else:
            print("High Card. Take {0} damage.".format(roll(4,2,0)))

    ### first set
    elif (results[0] == 1):
        if (results[1] == 2):
            print("Two pair of {0} over {1}".format(cardNames[results[2]-1], cardNames[results[4]-1]))
        elif (results[1] == 4):
            print("{0}-high straight".format(cardNames[results[2]-1]))
        elif (results[1] == 5):
            print("{0}-high flush in {1}".format(cardNames[results[2]-1], suitNames[results[4]]))
        else:
            print("{0} {1}".format(resultNames[results[1]-1], cardNames[results[2]-1]))
        print("Deal {0}".format(roll(docD+bm, results[1], refactor(results[2]) + mods[results[3]])))
        #print("{0}d{3}+{1}+{2}".format(results[1],refactor(results[2]),mods[results[3]],docD+bm))

    ### full house
    elif (results[0] == 2):
        print("Full House of {0} over {1}!".format(cardNames[results[2]-1], cardNames[results[4]-1]))
        print("Deal {0}".format(roll(docD+bm, results[1], refactor(results[2]) + mods[results[3]])))
        print("Heal two allies {0}".format(roll(4, refactor(results[4]), 0)))
        #print("{0}d{3}+{1}+{2}".format(results[1],refactor(results[2]),mods[results[3]],docD+bm))

    ### 4/kind
    elif (results[0] == 3):
        print("Four of a Kind of {0}!".format(cardNames[results[2]-1]))
        print("Deal {0}".format(roll(docD+bm, results[1], 4*refactor(results[2]) + mods[results[3]])))
        print("Heal four allies {0}".format(roll(4, refactor(results[4]), 0)))
        #print("{0}d{3}+{1}+{2}".format(results[1],refactor(results[2]),mods[results[3]],docD+bm))

    ### straight flush
    elif (results[0] == 4):
        print("{0}-high Straight Flush in {1}!!".format(cardNames[results[2]-1], suitNames[results[4]]))
        print("Instant Kill your target!")

    ### royal flush
    elif (results[0] == 5):
        print("Royal Flush in {0}!!!".format(suitNames[results[4]]))
        print("Instant Kill your target! Full Heal Allies!")

    ### 5/kind
    elif (results[0] == 6):
        print("FIVE OF A KIND OF {0}!!!".format(cardNames[results[2]-1].upper()))
        print("Instant Kill! Full Heal Allies! Gain {0} Temp Health! Refresh your turn!".format(results[2]))

    ### if this happens something is very wrong
    else:
        print("ERROR!?!")

    unSwap()

### for processing poker hands
### the wildcard processes divert into here
def pokerProcess(cards):
    
    ### preps vars
    ## results[0] == classification
    ## results[1] == multiplier
    ## results[2] == card value
    ## results[3] == modifier
    ## results[4] == suit?
    results = [0,0,0,0,0]
    vals = []
    suits = []
    
    ### converts cards into values, checks for dupes
    for i in cards:
        vals.append((i-1)%13 + 1)
        suits.append(int((i-1)/13))

    vals.sort()
        
    dupli = dupliCheck(vals)
    
    ### no duplicates (pairs)
    if (dupli[0] == 1):

        ### checks for flush
        if (suits.count(suits[0]) == 5):
            
            ### royal flush
            if ((vals[0] + 9 == vals[1])):
                results[0] = 5
                results[4] = suits[0]
            
            ### straight flush
            elif ((vals[0] + 4 == vals[4])):
                results[0] = 4
                results[2] = vals[4]
                results[4] = suits[0]

            ### flush
            else:
                results = [1,5,vals[4],2,suits[0]]

        ### checks for straight
        else:

            ### straight (head at top)
            if ((vals[0] + 4 == vals[4])):
                results = [1,4,vals[4],1,vals[4]]
            
            ### straight (head ace)
            elif ((vals[0] + 9 == vals[1])):
                results = [1,4,vals[0],1,vals[0]]

            ### high card
            else:
                results = [0,0,0,0,0]

    ### at least 1 duplicate set (size & number unknown)
    else:

        ### checks for a pair
        if (2 in dupli):

            ### ignores the current pair
            dupli.remove(2)

            ### two pair
            if (2 in dupli):
                if (vals[1] == 1):
                    results = [1,2,vals[1],0,vals[3]]
                else:
                    results = [1,2,vals[3],0,vals[1]]

            ### full house
            elif (3 in dupli):
                if (vals[1] == vals[2]):
                    pairval = vals[3]
                else:
                    pairval = vals[1]
                results = [2,5,vals[2],2,pairval]

            ### pair
            else:
                if ((vals[0] == vals[1]) or (vals[1] == vals[2])):
                    pairval = vals[1]
                else:
                    pairval = vals[3]
                results = [1,1,pairval,0,pairval]

        ### 3/kind
        elif (3 in dupli):
            results = [1,3,vals[2],1,vals[2]]

        ### 4/kind
        elif (4 in dupli):
            results = [3,5,vals[2],2,vals[2]]

        ### 5/kind
        elif (5 in dupli):
            results[0] = 1
            results[2] = vals[0]

        ### uh oh (if you're here, something is very wrong)
        else:
            print("ERROR???")

    return results

### when there's one wild card
def wildPokerProcess(cards):

    ### shows wild
    print("WILD!\n")

    ### gets rid of the wild
    if (53 in cards):
        cards.remove(53)
    else:
        cards.remove(54)
    
    ### var setup
    vals = []
    suits = []
    flushCheck = False
    straightCheck = False

    ### calculates vals, checks for dupes
    for i in cards:
        vals.append((i-1)%13 + 1)
        suits.append(int((i-1)/13))

    vals.sort()
        
    dupli = dupliCheck(vals)
    
    ### no duplicates (pairs)
    if (dupli[0] == 1):

        ### checks for flush
        if (suits.count(suits[0]) == 4):
            flushCheck = True

        ### checks for straight
        dist = []
        for i in range(0, len(vals)-1):
            dist.append(vals[i+1] - vals[i])

        strpass = False

        ### if ace, uses diff method
        if (1 in vals):
            strpass = True
            for i in vals:
                if (i < 10 and i != 1):
                    strpass = False

        if (sum(dist) <= 4 or strpass):
            straightCheck = True

        ### straight is possible
        if (flushCheck and straightCheck):

            ### if numbers are grouped
            if (vals[0] + 3 == vals[3]):

                ### have 10/J/Q/K, adds ace
                if (vals[3] == 13):
                    cards.append(1 + 13 * suits[0])

                ### have other group, adds higher card
                else:
                    cards.append(vals[3] + 1 + 13 * suits[0])

            ### gap in numbers
            else:

                ### if ace in
                if (strpass):

                    ### checks which of 10/J/Q/K the hand doesn't have, adds it
                    for i in [10,11,12,13]:
                        if (i not in vals):
                            cards.append(i + 13 * suits[0])

                ### if no ace
                else:

                    ### checks which of the cards the hand is missing in the set of 5
                    for i in range(vals[0], vals[0]+5):
                        if (i not in vals):
                            cards.append(i + 13 * suits[0])

        ### if a flush is possible
        elif (flushCheck):

            ### adds the highest card possible of that suit
            for i in [1, 13, 12, 11, 10]:
                if (i not in vals):
                    cards.append(i + 13 * suits[0])
                    break
        
        ### just high card otherwise
        else:

            ### makes the highest value pair
            if (vals[0] == 1):
                cards.append(1)
            else:
                cards.append(vals[3])

    ### at least 1 duplicate set (size & number unknown)
    else:

        ### checks for a pair
        if (2 in dupli):

            ### ignores the current pair
            dupli.remove(2)

            ### two pair -> full house
            if (2 in dupli):
                if (vals[1] == 1):
                    cards.append(1)
                else:
                    cards.append(vals[3])

            ### pair -> 3/kind
            else:
                if ((vals[0] == vals[1]) or (vals[1] == vals[2])):
                    pairval = vals[1]
                else:
                    pairval = vals[3]

                cards.append(pairval)

        ### 3/kind -> 4/kind
        elif (3 in dupli):
            cards.append(vals[1])

        ### 4/kind -> 5/kind
        elif (4 in dupli):
            cards.append(vals[0])

        ### uh oh (if you're here, something is very wrong)
        else:
            print("ERROR???")

    ### processes and returns
    results = pokerProcess(cards)

    return results

### for when there are 2 wild cards
def doubleWildPokerProcess(cards):

    ### prints
    print("2 WILDS!")

    ### throws out wilds
    cards.remove(53)
    cards.remove(54)

    ### variables
    vals = []
    suits = []
    flushCheck = False
    straightCheck = False

    ### calculates values, finds duplicates
    for i in cards:
        vals.append((i-1)%13 + 1)
        suits.append(int((i-1)/13))

    vals.sort()
        
    dupli = dupliCheck(vals)
    
    ### no duplicates (pairs)
    if (dupli[0] == 1):

        ### checks for flush
        if (suits.count(suits[0]) == 3):
            flushCheck = True

        ### checks for straight
        dist = []
        for i in range(0, len(vals)-1):
            dist.append(vals[i+1] - vals[i])

        strpass = False

        ### checks for if a straight is possible
        if (1 in vals):
            strpass = True
            for i in vals:
                if (i < 10 and i != 1):
                    strpass = False

        if (sum(dist) <= 4 or strpass):
            straightCheck = True

        ### if a straight is possible
        if (straightCheck):

            ### if the numbers are grouped
            if (vals[0] + 2 == vals[2]):

                ### if you have J/Q/K, adds 10 & A
                if (vals[2] == 13):
                    cards.append(1 + 13 * suits[0])
                    cards.append(10 + 13 * suits[0])

                ### if you have 10/J/Q, adds K & A
                elif (vals[2] == 12):
                    cards.append(13 + 13 * suits[0])
                    cards.append(1 + 13 * suits[0])

                ### otherwise, adds next two cards
                else:
                    cards.append(vals[3] + 1 + 13 * suits[0])
                    cards.append(vals[3] + 2 + 13 * suits[0])

            ### if the numbers are separated
            else:

                ### if there is an ace
                if (strpass):

                    ### adds the other high cards needed
                    for i in [10,11,12,13]:
                        if (i not in vals):
                            cards.append(i + 13 * suits[0])

                ### if there are not aces
                else:

                    ### adds the other missing cards
                    for i in range(vals[0], vals[0]+5):
                        if (i not in vals):
                            cards.append(i + 13 * suits[0])

        ### if a flush is possible
        elif (flushCheck):

            ### adds highest possible cards in the suit
            for i in [1, 13, 12, 11, 10]:
                if (i not in vals):
                    cards.append(i + 13 * suits[0])
                    if (len(cards) == 5):
                        break

        ### high card
        else:

            ### makes a three of a kind out of the highest card
            if (vals[0] == 1):
                cards.append(1)
                cards.append(1)
            else:
                cards.append(vals[2])
                cards.append(vals[2])

    ### at least 1 duplicate set (size & number unknown)
    else:

        ### pair -> 4/kind
        if (2 in dupli):
            cards.append(vals[1])
            cards.append(vals[1])

        ### 3/kind -> 5/kind
        elif (3 in dupli):
            cards.append(vals[1])
            cards.append(vals[1])

        ### uh oh (if you're here, something is very wrong)
        else:
            print("ERROR???")

    ### processes and returns
    results = pokerProcess(cards)

    return results

### Lucky Seven
### Level 4 Ability
def lucky7():

    ### checks for 3 cards
    if (invalid(3)):
        return

    ### draws 3d4 cards
    cards = []
    drawn = hardroll(4,3,0)
    print("{0} cards drawn!\n".format(drawn))
    for i in range(0,drawn):
        cards.append(cardDraw())

    ### interprets cards
    vals = []
    for i in cards:
        if (i == 53):
            vals.append(0)
        elif (i == 54):
            vals.append(12)
        else:
            val = i - int(i/13) * 13
            if (val == 0 or val >= 10):
                vals.append(10)
            elif (val == 1):
                vals.append(11)
            else:
                vals.append(val)

    ### processes
    print()
    for i in range(0,3):
        if 53 in vals:
            vals.remove(53)
            print("{0} 7! (Blank)".format(i+1))
        elif 54 in vals:
            vals.remove(54)
            print("{0} 7! (Joker)".format(i+1))
        elif 7 in vals:
            vals.remove(7)
            print("{0} 7!".format(i+1))
        else:
            print("\nNo Lucky 7.")
            unSwap()
            return

    ### output
    print("\nLUCKY 7!!!")
    print("Restore 7 health to allies in a 7(*5) foot radius and your next roll is a guaranteed natural crit.")

    unSwap()

### Mill
### Level 5 Ability
def mill():

    ### variables
    global deck
    global discard

    ### draws cards, mills them
    drawn = hardroll(6,1,0)
    print("{0} cards milled!\n".format(drawn))
    for i in range(0,drawn):
        cardDraw()  

    unSwap()

### Stack the Deck
### Level 5 Ability
def stackDeck():

    ### variables
    global deck
    global discard
    vocab = ["first", "second", "third", "fourth", "fifth"]

    ### draws 1d4+1 cards
    drawn = hardroll(4,1,1)
    print("Top {0} cards:".format(drawn))
    cards = []
    for i in range(0, drawn):
        cards.append(cardDraw())

    ### more variables ig
    order = [0] * drawn
    skip = False

    ### gets valid order
    while (True):

        ### inputs
        for i in range(0, drawn):
            print("{0} card:".format(vocab[i].capitalize()), end = " ")
            interpret(cards[i])
            print("In which position should the {0} card go (options: 1 (top)-{1} (bot))?".format(vocab[i], drawn))
            ipt = input()
            try:
                ipt = int(ipt)
            except (ValueError):
                ipt = 1
            order[i] = ipt
        
        ### checks to see if numbers are out of range
        for i in order:
            if (i > drawn or i < 1):
                print("Invalid Input")
                skip = True

        ### skips if necessary
        if (skip):
            skip = False
            continue
        
        ### if dupliCheck says there are duplicates, continues
        if (dupliCheck(order)[0] > 1):
            print("Invalid Order")

        ### if passes 
        else:
            break

    ### puts the cards in in order, removes from discard (since card draw appended them to discard)
    for i in order:
        deck.append(cards[drawn-i])
        discard.pop()

    unSwap()

### Reverse Draw
### Level 6 Ability
def reverseDraw():

    ### global variables used
    global discard
    global deck
    
    ### draw card
    rCard = deck[0]
    discard.append(rCard)
    deck = deck[1:]
    interpret(rCard)
    if (rCard == 17):
        print("4 of Diamonds Drawn, gain Lifesteal!")

    ### if deck has been emptied
    size = len(deck)

    if (size == 0):
        print("Desperate Deck Out!")
        print("Lose half your max health, refill, cast Greedy Draw")
        refill()
        greedyDraw()

    unSwap()

    return rCard

### Predict
### Level 6 Ability
def predict():

    ### gets deck
    global deck

    ### gets 3 random cards
    rands = randInts(len(deck), 3)
    cards = []
    for i in rands:
        cards.append(deck[i-1])
        interpret(deck[i-1])

    ### gets a # from user, 1-3
    while (True):
        print("Which # card should go to the top?")
        ipt = input()
        try:
            ipt = int(ipt)
        except (ValueError):
            print("Not a number.")
            ipt = 0
            continue
        if (ipt > 3 or ipt < 1):
            print("Out of range")
        else:
            break

    ### removes cards from deck
    for i in cards:
        deck.remove(i)

    ### puts selected card on top
    deck.append(cards[ipt-1])
    cards.pop(ipt-1)

    ### puts others on bottom
    deck = cards + deck

    unSwap()

### Subtle Swap
### Level 7 Ability
def subtleSwap():

    ### grabs variables
    global discard
    global deck
    global swapped

    ### if you don't have cards in discard, exits
    if (invalidDisc(1)):
        return

    ### shuffle disc
    random.shuffle(discard)

    ### swaps, flips swapped, prints
    temp = discard
    discard = deck
    deck = temp
    swapped = True
    print("Discard and Deck swapped for next action!")

### Subtle Swap helper
### Unswaps deck & discard
### Placed at the end of most functions because they could have been using swapped decks
def unSwap():

    ### variables
    global swapped
    global discard
    global deck

    ### if swapped is True
    if (swapped):

        ### swaps back, flips swapped, prints
        temp = discard
        discard = deck
        deck = temp
        swapped = False
        print("Discard and Deck swapped back!")

### Random Refresh
### Level 7 Ability
def randomRefresh():

    ### checks for 3 cards
    if (invalidDisc(3)):
        return

    ### setup
    print("Randomly Refreshing!")
    global discard
    global deck

    ### gets 3 random cards
    rands = randInts(len(discard), 3)
    cards = []
    for i in rands:
        cards.append(discard[i-1])
    
    ### moves cards from discard into deck at random positions
    for card in cards:
        discard.remove(card)

    for i in cards:
        deck.insert(random.randint(0, len(deck)), i)

    unSwap()

### Ride the Bus
### Level 9 Ability
def rideBus():

    ### grabs discard
    global discard

    ### checks for 4 cards
    if (invalidDisc(4)):
        return

    ### shuffles
    random.shuffle(discard)

    ### variables
    success = 0
    wildpass = False

    ### call color
    print("Call Color!")
    while (True):
        print("R for red, B for Black")
        ipt = input().lower()
        if (ipt != "r" and ipt != "b"):
            continue
        break

    ### checks to see if color matches
    card1 = discDraw()
    val1 = (card1 - 1) % 13 + 1
    if (card1 == 53 or card1 == 54):
        print("WILD Success!")
        wildpass = True
        success += 1
    elif (int(card1/13) == 1 or int(card1/13) == 2):
        if (ipt == "r"):
            print("Success!")
            success += 1
    else:
        if (ipt == "b"):
            print("Success!")
            success += 1

    ### high/low
    print("\nHigh/Low!")
    while (True):
        print("H for high, L for low")
        ipt = input().lower()
        if (ipt != "h" and ipt != "l"):
            continue
        break

    ### compares val1 to val2, checks
    card2 = discDraw()
    val2 = (card2 - 1) % 13 + 1
    if (card2 == 53 or card2 == 54 or wildpass):
        print("WILD Success!")
        wildpass = True
        success += 1
    elif (val2 > val1):
        if (ipt == "h"):
            print("Success!")
            success += 1
    elif (val2 < val1):
        if (ipt == "l"):
            print("Success!")
            success += 1

    ### in/out
    print("\nIn/Out!")
    while (True):
        print("I for in, O for out")
        ipt = input().lower()
        if (ipt != "i" and ipt != "o"):
            continue
        break

    ### compares val3 to val1 & val2
    card3 = discDraw()
    val3 = (card3 - 1) % 13 + 1
    if (card3 == 53 or card3 == 54 or wildpass):
        print("WILD Success!")
        success += 1
    elif (min(val1, val2) < val3 and max(val1, val2) > val3):
        if (ipt == "i"):
            print("Success!")
            success += 1
    elif (min(val1, val2) > val3 or max(val1, val2) < val3):
        if (ipt == "o"):
            print("Success!")
            success += 1

    ### suite
    print("\nSuite!")
    while (True):
        print("C for clubs, D for diamonds, H for hearts, S for spades")
        ipt = input().lower()
        if (ipt != "c" and ipt != "d" and ipt != "h" and ipt != "s"):
            continue
        break

    ### checks suite of card 4
    card4 = discDraw()
    if (card4 == 53 or card4 == 54):
        print("WILD Success!")
        success += 1
    elif (int(card4/13) == 0):
        if (ipt == "c"):
            print("Success!")
            success += 1
    elif (int(card4/13) == 1):
        if (ipt == "d"):
            print("Success!")
            success += 1
    elif (int(card4/13) == 2):
        if (ipt == "h"):
            print("Success!")
            success += 1
    else:
        if (ipt == "s"):
            print("Success!")
            success += 1

    ### puts the cards back in discard
    discard.append(card1)
    discard.append(card2)
    discard.append(card3)
    discard.append(card4)

    ### prints successes
    print("\n{0} successes!".format(success))

    ### grabs dice, rolls
    dice = [0,2,3,6,9][success]
    print("Deal {0} damage.".format(roll(success*2+2, dice, 0)))

    unSwap()

### Blackjack
### Level 9 Ability
def blackjack():

    ### pulls discard
    global discard

    ### checks to see if enough in disc
    if (invalidDisc(2)):
        return

    ### shuffles
    random.shuffle(discard)

    ### creates hands; draws; converts to strings
    bjhand = []
    strhand = []

    bjhand.append(discDraw())
    bjhand.append(discDraw())

    strhand.append(strconvert(bjhand[0]))
    strhand.append(strconvert(bjhand[1]))

    ### shows hand
    print("Your hand: {0}".format(strhand))
    total = BJevaluate(strhand)
    print("Score: {0}".format(total))

    ### while not bust
    while (total < 21):

        ### input
        print("Input 'h' to hit or 'f' to fold")
        ipt = input()

        if (ipt != "h" and ipt != "f"):
            print("Invalid Input")
            continue


        ### hit
        if (ipt == "h"):

            if (invalidDisc(1)):
                print("You must fold and do so.")
                break

            bjhand.append(discDraw())
            strhand.append(strconvert(bjhand[-1]))

        ### fold
        else:
            break
        
        ### shows hand
        print("Your hand: {0}".format(strhand))
        total = BJevaluate(strhand)
        print("Score: {0}".format(total))

    ### blackjack
    if (total == 21):
        print("BLACKJACK!")
        print("Heal {0}; up to 7 of it can go into temporary HP.".format(roll(4,6,0)))

    ### bust
    elif (total > 21):
        print("You busted.")
        print("Take {0} damage.".format(roll(4,total-21,0)))

    ### fold
    elif (total > 0):
        print("You folded.")
        print("Heal {0}.".format(roll(4, max(0, total-15),0)))

    ### something weird happened
    else:
        print("Error")

    ### puts cards into deck
    for i in bjhand:
        deck.append(i)

    random.shuffle(deck)

    unSwap()


### Performs a dice roll
### input 1: dieSides (sides per die)
### input 2: dieNo (number of dice to roll)
def roll(dieSides, dieNo, constMod):

    ### global var
    global selfroll

    if (selfroll):

        if (constMod == 0):
            print("\nRoll {0}d{1}".format(dieNo, dieSides))

        else:
            print("\nRoll {0}d{1}+{2}".format(dieNo, dieSides, constMod))

        return "rolled"

    else:

        ### initialize
        out = constMod

        ### roll number of times with dice sides
        for i in range(0, dieNo):
            out += random.randint(1, dieSides)

        ### return
        return out

### roll but without selfroll capabilities
def hardroll(dieSides, dieNo, constMod):
    
    ### initialize
    out = constMod

    ### roll number of times with dice sides
    for i in range(0, dieNo):
        out += random.randint(1, dieSides)

    ### return
    return out

### Checks to see if there are at least num cards in the deck
def invalid(num):

    ### global variable used
    global deck

    ### checks & outputs
    if (len(deck) < num):
        print("You don't have enough cards!")
        return True
    else:
        return False

### Checks to see if there are at least num cards in discard
def invalidDisc(num):

    ### global variable used
    global discard

    ### checks & outputs
    if (len(discard) < num):
        print("You don't have enough cards in discard!")
        return True
    else:
        return False

### Look at your discard pile.
def remember():

    ### global variable used
    global discard

    ### cycles through discard
    print("In your discard pile:")
    for i in discard:
        interpret(i)

### prints the number of cards in deck & discard
def deckCheck():

    ### global variables used
    global deck
    global discard

    ### output
    print("\nYou have {0} cards in deck and {1} cards in discard\n".format(len(deck), len(discard)))

### checks in an array to see if there are duplicates
def dupliCheck(nums):

    ### vars
    dupli = [0] * len(nums)
    out = [1] * len(nums)

    ### checks how many of each number there are using count(), puts in dupli
    for i in range(0, len(nums)):
        dupli[i] = nums.count(nums[i])

    ### index if needed for out
    index = 0

    ### goes through the numbers
    for i in range(0, len(nums)):

        ### if there's more than 1 of a count
        if dupli[i] > 1:

            ### puts it in
            out[index] = dupli[i]
            index += 1
            
            ### now we don't want to doublecount, so we remove the number and its copies
            val = dupli[i]
            dupli[i] = 1
            for i in range(1, val):
                dupli.remove(val)
                dupli.append(1)

    ### output
    return out

### returns 'num' random numbers between 1 and 'limit'
def randInts(limit, num):

    ### var
    out = []

    ### adds (unique) random variables
    while num >= 1:
        rand = random.randint(1, limit)
        while (rand in out):
            rand = random.randint(1, limit)
        out.append(rand)
        num -= 1

    ### output
    return out

### takes in the number of a card
### outputs the string representation of the card name
def strconvert(num):

    ### jokers & blanks return wild
    if (num == 53 or num == 54):
        return "Wild"

    ### otherwise:
    elif (num < 53 and num > 0):

        ### calc modulo 13
        val = (num - 1) % 13 + 1

        ### returns A, J, Q, K for 1, 11, 12, 13
        if (val == 1):
            return "A"
        elif (val == 11):
            return "J"
        elif (val == 12):
            return "Q"
        elif (val == 13):
            return "K"

        ### returns the number as a string
        else:
            return str(val)

    ### if not in range, returns error
    else:
        return "ERROR"

### function to evaluate the score of a blackjack hand
def BJevaluate(strhand):

    ### variable set up
    reevaluateA = [False, 1]
    reevaluateW = [False, 1]
    score = 0

    ### goes through hand
    for card in strhand:

        ### if numerical value, adds
        try:
            score += int(card)

        ### if not numerical value
        except (ValueError):

            ### if ace, modifies reevaluateA to True or increases by 1
            if (card == "A"):
                if (reevaluateA[0]):
                    reevaluateA[1] +=1
                else:
                    reevaluateA[0] = True

            ### if face card, adds 10
            elif (card == "J" or card == "Q" or card == "K"):
                score += 10

            ### if wild, modifies reevaluateW to True or increases by 1
            elif (card == "Wild"):
                if (reevaluateW[0]):
                    reevaluateW[1] +=1
                else:
                    reevaluateW[0] = True
    
    ### ace calculations
    if (reevaluateA[0]):

        ### checks # of aces
        for i in range(0, reevaluateA[1]):

            ### if you can add 11, does so
            if (score + 11 <= 21):
                score += 11

            ### if the first ace added 11 to get to 21 but there's another ace
            ### turns the first ace to 1 (-10) and has the new ace be 1 (-10+1=-9)
            elif (score == 21 and i >= 1 and reevaluateA[1] > 1):
                score -= 9

            ### if you can't add 11, adds 1
            else:
                score += 1

    ### wild calculations
    if (reevaluateW[0]):

        ### if your score is already 21
        if (score == 21):

            ### if there was an ace
            if (reevaluateA[0]):

                ### turns the ace to 1, the wilds fill in
                score = 21

            ### otherwise
            else:

                ### the wilds count as 1
                score += reevaluateW[1]
        
        ### if the score is 20 and you have more than 1 wild
        elif (score == 20 and reevaluateW[1] > 1):

            ### if there was an ace
            if (reevaluateA[0]):

                ### turns the ace to 1, the wilds fill in
                score = 21

            ### otherwise
            else:

                ### the wilds count as 1
                score += reevaluateW[1]

        ### otherwise
        else:

            ### if you have 1 wild
            if (reevaluateW[1] == 1):

                ### you can either add 11
                if (score + 11 <= 21):
                    score += 11

                ### if you can't add 11, goes to 21
                else:
                    score = 21

            ### if you have >1 wild
            else:

                ### score increments to 21
                score = 21

    return score

### refactoring numbers
def refactor(cardval):
    if (cardval == 1):
        cardval = 14
    return cardval

### attack with diamond daggers
def diamondHands():

    print("Drawing cards for Diamond Hands:\n")

    critMod = critCheck()
    dice = 1
    drawn = cardDraw()
    suit = int((drawn - 1)/13)

    while (suit != 1):
        drawn = cardDraw()
        suit = int((drawn - 1)/13)
        dice += 1

    print ("\nDrew {0} cards! Deal {1} damage!".format(dice, roll(4, 2*dice*critMod, 2*DEX)))

    unSwap()

### crit
def critOn():

    ### flips crit, turns it on
    global crit
    crit = True
    print("Crits are on!")

### crit damage
def critCheck():

    ### checks to see if crit is True
    ### if it is, returns 2 and flips crit
    ### else, returns 1
    
    global crit
    if (crit):

        print("CRIT!")
        crit = False
        return 2

    else:
        return 1

### to flip unwanted things
def cancel():
    global crit
    global bluff
    global swapped

    if (crit):
        print("Cancelled Crit.")
        crit = False
    
    if (bluff[0]):
        print("Cancelled Bluff")
        bluff[0] = False

    if (swapped):
        print("Cancelled Swap")
        unSwap()

### function that allows user to inspect the contents of deck & discard
### DEV USE ONLY
def debug():

    ### global vars
    global deck
    global discard

    ### prints for viewing
    print(deck)
    print(discard)

### for testing poker hand
### DEV USE ONLY
def rig():

    global deck
    refill()

    print("index")
    ipt = input().lower()
    if (ipt == "0"):
        rem = [1,2,7,8,18]
    elif (ipt == "1"):
        rem = [1,2,7,8,14]
    elif (ipt == "2"):
        rem = [1,2,7,14,15]
    elif (ipt == "3"):
        rem = [1,14,27,2,3]
    elif (ipt == "4"):
        rem = [15,3,4,5,6]
    elif (ipt == "41"):
        rem = [1,10,11,12,26]
    elif (ipt == "5"):
        rem = [1,3,4,5,6]
    elif (ipt == "6"):
        rem = [1,14,2,15,28]
    elif (ipt == "7"):
        rem = [1,14,27,40,2]
    elif (ipt == "8"):
        rem = [2,3,4,5,6]
    elif (ipt == "9"):
        rem = [1,10,11,12,13]
    elif (ipt == "w"):
        rem = [53]
    elif (ipt == "2w"):
        rem = [53, 54]
    else:
        print("failed rig")
        rem = [1,5,9,15,52]
    
    for i in rem:
        deck.remove(i)
        deck.append(i)
    
    print("lol rigged")

### save dexstate
def save():

    ### global var calls
    global deck
    global discard

    ### open file
    fi = open("savedata.txt", "w")

    ### writes in discard
    for i in discard:
        fi.write(str(i)+"\n")

    ### close file
    fi.close()

### load deckstate
def load():

    ### global var calls
    global deck
    global discard

    ### open file
    fi = open("savedata.txt", "r")

    ### calls temp array
    temparray = []
    
    ### goes through, puts it in
    for line in fi:
        strline = str(line)
        strline.strip("\n")
        intline = int(strline)
        temparray.append(intline)

    ### close file
    fi.close()

    ### puts temparray into discard   
    discard = temparray

    ### empties deck
    deck = []

    ### puts missing cards into deck
    for i in range(1,55):
        if i not in discard:
            deck.append(i)

    ### shuffles
    random.shuffle(deck)

### toggle rolling on your own or not
def toggleRoll():

    global selfroll

    if (selfroll):
        print("Rolls will now be done for you!")
    
    else:
        print("Rolls will no longer be done for you. Roll on your own.")

    selfroll = not selfroll

### main function run
def main():
    global deck
    global discard

    while(True):
        print("1 for CalcRisk, 2 for Greedy Draw, 3 for Quick Draw, 4 for Refill, 5 for Cheat the Flop")
        print("6 for Remember, 7 for Lucky7, 8 for mill, 9 for bluff, 10 for fold")
        print("11 for stack the deck, 12 for reverse draw, 13 for predict, 14 for subtle swap")
        print("15 for random refresh, 16 for ride the bus, 17 for blackjack")
        print("ATK for hit on diamond daggers attack")
        print("PKR for poker hand, CRIT for crit enable, CNCL to cancel")
        print("SAVE to save, LOAD to load, E to exit")
        print("ROLL to toggle rolling for yourself")
        ipt = input().lower()
        print()
        if (ipt == "1"):
            calcRisk()
        elif (ipt == "2"):
            greedyDraw()
        elif (ipt == "3"):
            quickDraw()
        elif (ipt == "4"):
            refill()
        elif (ipt == "5"):
            cheatFlop()
        elif (ipt == "e"):
            return
        elif (ipt == "7"):
            lucky7()
        elif (ipt == "6"):
            remember()
        elif (ipt == "8"):
            mill()
        elif (ipt == "9"):
            startBluff()
        elif (ipt == "10"):
            fold()
        elif (ipt == "11"):
            stackDeck()
        elif (ipt == "12"):
            reverseDraw()
        elif (ipt == "13"):
            predict()
        elif (ipt == "14"):
            subtleSwap()
        elif (ipt == "15"):
            randomRefresh()
        elif (ipt == "16"):
            rideBus()
        elif (ipt == "17"):
            blackjack()
        elif (ipt == "d"):
            debug()
        elif (ipt == "atk"):
            diamondHands()
        elif (ipt == "crit"):
            critOn()
        elif (ipt == "pkr"):
            pokerHand()
        elif (ipt == "rig"):
            rig()
        elif (ipt == "cncl"):
            cancel()
        elif (ipt == "save"):
            save()
        elif (ipt == "load"):
            load()
        elif (ipt == "roll"):
            toggleRoll()


        deckCheck()

main()
