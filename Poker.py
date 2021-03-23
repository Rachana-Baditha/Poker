import random
import pygame

class card:
    def __init__(self,num,suit):
        self.n = num
        self.s = suit
        
    def checknum(num):
        if(num==14):
            return "A"
        elif(num==11):
            return "J"
        elif(num==12):
            return "Q"
        elif(num==13):
            return "K"
        else:
            return num

    def checksuit(suit):
        if(suit==1):
            return "Hearts"
        elif(suit==2):
            return "Spades"
        elif(suit==3):
            return "Clubs"
        elif(suit==4):
            return "Diamonds"

    def set(hand):
        twoset=0
        threeset=0
        fourset=0

        for i in range(7):
            for j in range(i+1,7):
                if hand[i].n == hand[j].n:
                    twoset+=1
                    for k in range(j+1,7):
                        if hand[i].n == hand[k].n:
                            twoset=twoset-3
                            threeset+=1
                            for l in range(k+1,7):
                                if hand[i].n == hand[l].n:
                                    threeset=threeset-4
                                    fourset+=1

        if twoset == 1 and threeset == 0:
            return 2
        elif twoset >= 2 and threeset == 0:
            return 3
        elif threeset == 1 and twoset == 0:
            return 4
        elif threeset == 2 or (threeset == 1 and twoset == 1):
            return 7
        elif fourset == 1:
            return 8
        else:
            return 1

    def flush(hand):
        flush=1

        for i in range(7):
            for j in range(i+1,7):
                if hand[i].s == hand[j].s:
                    for k in range(j+1,7):
                        if hand[i].s == hand[k].s:
                            for l in range(k+1,7):
                                if hand[i].s == hand[l].s:
                                    for m in range(l+1,7):
                                        if hand[i].s == hand[m].s:
                                            flush=6
        return flush

    def straight(hand):
        min = []

        straight = 1
        handnum = []
        for x in hand:
            handnum.append(x.n)

        min1 = hand[0]

        for x in hand:
            if min1.n > x.n:
                min1 = x

        min2 = hand[0]

        for x in hand:
            if min2.n > x.n and min2 != min1:
                min2 = x

        min3 = hand[0]

        for x in hand:
            if min3.n > x.n and min3 != min1 and min3 != min2:
                min3 = x

        min.append(min1)
        min.append(min2)
        min.append(min3)


        for x in min:
            count=0
            for i in range(1,5):
                if (x.n)+i in handnum:
                    count+=1
            if count ==4:
                straight = 5
                break

        if straight!=5:
            count=0
            for y in range(2,6):
                for x in hand:
                    if y == x.n:
                        count+=1
                        break

            for x in hand:
                if x.n ==14:
                    count+=1
                    break

            if count == 5:
                straight=5

        return straight

    def royalflush(hand):

        royalflush=1
        for x in range(1,5):
            count=0
            for y in hand:
                if (y.n == 10 or y.n==11 or y.n==12 or y.n==13 or y.n==14) and y.s==x:
                    count+=1

            if count==5:
                royalflush=10

        return royalflush

    def straightflush(hand):

        straightflush=1
        min1 = hand[0]

        for i in range(1,7):
            if min1.n > hand[i].n:
                min1 = hand[i]

        min2 = hand[0]

        for i in range(7):
            if (min2.n > hand[i].n and hand[i] != min1) or (hand[i].n == min1.n and hand[i].s != min1.s):
                min2 = hand[i]

        min3 = hand[0]

        for i in range(7):
            if (min3.n > hand[i].n and hand[i] != min1) or (hand[i].n == min1.n and hand[i].s != min1.s) and (min3.n > hand[i].n and hand[i] != min2) or (hand[i].n == min2.n and hand[i].s != min2.s):
                min3 = hand[i]


        #print("Min1.n={}  min1.s={}  min2.n={}  min2.s={}  min3.n={}  min3.s={}".format(min1.n,min1.s,min2.n, min2.s, min3.n, min3.s))

        min = [min1,min2,min3]

        for x in min:
            count=0
            for i in range(1,6):
                for y in hand:
                    if y.n == (x.n+i) and y.s == x.s:
                        count+=1
                        break
        if count==4:
            straightflush=9

        return straightflush

    def finalres(max):

        if max==10:
            print("ROYAL FLUSH")
        elif max==9:
            print("STRAIGHT FLUSH")
        elif max==8:
            print("FOUR OF A KIND")
        elif max==7:
            print("FULL HOUSE")
        elif max==6:
            print("FLUSH")
        elif max==5:
            print("STRAIGHT")
        elif max==4:
            print("THREE OF A KIND")
        elif max==3:
            print("TWO PAIR")
        elif max==2:
            print("ONE PAIR")
        elif max==1:
            print("HIGH CARD")

    def checkhand(hand):

        rank = []

        rank.append( card.set(hand) )
        rank.append( card.flush(hand) )
        rank.append( card.straight(hand) )
        rank.append( card.straightflush(hand) )
        rank.append( card.royalflush(hand) )

        max = rank[0]

        for x in rank:
            if max<x:
                max = x

        return max


deck=[]
q=0
while q<52:

    a = random.randint(2,14)
    b= random.randint(1,4)
    flag=0
    for x in deck:
        if a==x.n and b==x.s:

            flag =1
            break

    if flag==0:
        deck.append( card(a,b))
        q+=1

player1 = []
player2 = []
board = []

i=0
for _ in range(2):
    player2.append(deck[i])
    player1.append(deck[i+1])
    i+=2

for _ in range(5):
    board.append(deck[i])
    i+=1


print("----------")

print("Your Cards:")
for pcard in player1:
    num = card.checknum(pcard.n)
    suit = card.checksuit(pcard.s)
    print("{} of {}".format(num, suit))

print("----------")

print("Board:")
for bcard in board:
    num = card.checknum(bcard.n)
    suit = card.checksuit(bcard.s)
    print("{} of {}".format(num, suit))

print("----------")

print("Opponent's Cards:")
for pcard in player2:
    num = card.checknum(pcard.n)
    suit = card.checksuit(pcard.s)
    print("{} of {}".format(num, suit))

print("----------")

p1rank = card.checkhand(player1 + board)
p2rank = card.checkhand(player2 + board)

print("P1:",end=" ")
card.finalres(p1rank)

print("P2:",end=" ")
card.finalres(p2rank)

print("----------")
print("RESULTS:")

if p2rank > p1rank:
    print("You Lose")
elif p1rank > p2rank:
    print("You Win")
elif p1rank == p2rank:
    print("Tie")
