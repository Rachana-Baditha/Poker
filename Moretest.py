import random

class win:
    def __init__(self, rank, playercard1, playercard2, hand1, hand2, hand3, hand4, hand5):
        self.r = rank
        self.pc1 = playercard1
        self.pc2 = playercard2
        self.h1 = hand1
        self.h2 = hand2
        self.h3 = hand3
        self.h4 = hand4
        self.h5 = hand5

    def reset(self):
        self = win(1,0,0,0,0,0,0,0)

    def highcard(p1stat,p2stat,setcard1, setcard2):   #pstat is object holding rank, player cards and hand cards... setcard is any card in both player cards and hand

        p1 = [p1stat.pc1, p1stat.pc2]
        p2 = [p2stat.pc1, p2stat.pc2]

        for x in p1:
            if x == setcard1 or x==setcard2:
                p1.remove(x)
                                                   #Check if this is necessary
        for x in p2:
            if x == setcard1 or x==setcard2:
                p2.remove(x)


        if p1 and p2:

            max1 = max(p1)
            max2 = max(p2)

            if max1 > max2:
                return 1
            elif max2 > max1:
                return -1
            elif max1 == max2:

                if max1 == p1[0]:
                    max1 = p1[1]
                elif max1 == p1[1]:
                    max1 = p1[0]

                if max2 == p2[0]:
                    max2 = p2[1]
                elif max2 == p2[1]:
                    max2 = p2[0]

                if max1 > max2:
                    return 1
                elif max2 > max1:
                    return -1
                elif max1 == max2:
                    return 0

        else:
            return 0

    def t_onepair(p1stat,p2stat):   #Can combine onepair and threeset


        if p1stat.h1 > p2stat.h1:
            return 1
        elif p1stat.h1 < p2stat.h1:
            return -1
        else:
            return win.highcard(p1stat,p2stat,p1stat.h1,0)  #setcard is number in pair

    def t_twopair(p1stat,p2stat):

        temp=0

        if p1stat.h1 < p1stat.h3:
            temp = p1stat.h1
            p1stat.h1 = p1stat.h3
            p1stat.h3 = temp

        if p2stat.h1 < p2stat.h3:
            temp = p2stat.h1
            p2stat.h1 = p2stat.h3
            p2stat.h3 = temp

        if p1stat.h1 > p2stat.h1:
            return 1
        elif p1stat.h1 < p2stat.h1:
            return -1
        elif p1stat.h3 > p2stat.h3:
            return 1
        elif p1stat.h3 < p2stat.h3:
            return -1
        else:
            return win.highcard(p1stat,p2stat,p1stat.h1,p1stat.h3)   #setcards are numbers in pairs

    def t_threeset(p1stat,p2stat):

        if p1stat.h1 > p2stat.h1:
            return 1
        elif p1stat.h1 < p2stat.h1:
            return -1
        else:
            return win.highcard(p1stat,p2stat,p1stat.h1,0)   #setcard is number in three set

    def t_fourset(p1stat, p2stat):

        if p1stat.h1 > p2stat.h1:
            return 1
        elif p1stat.h1 < p2stat.h1:
            return -1
        else:
            return win.highcard(p1stat,p2stat,0,0)  #no setcard

    def t_fullhouse(p1stat,p2stat):

        if p1stat.h1 > p2stat.h1:
            return 1
        elif p1stat.h1 < p2stat.h1:
            return -1
        else:

            if p1stat.h4 > p2stat.h4:
                return 1
            elif p1stat.h4 < p2stat.h4:
                return -1
            else:
                return win.highcard(p1stat,p2stat,p1stat.h1,p1stat.h4)  #setcards are number in three set and pair

    def t_straight(p1stat,p2stat,board):

        straight = [p1stat.h1,p1stat.h2,p1stat.h3,p1stat.h4,p1stat.h5]

        if p1stat.h1 > p2stat.h1:
            return 1
        elif p1stat.h1 < p2stat.h1:
            return -1
        elif p1stat.h1 == p2stat.h1:

            if p1stat.pc1 in straight and p1stat.pc1 not in board:
                if p1stat.pc2 in straight and p1stat.pc2 not in board:
                    return win.highcard(p1stat,p2stat,p1stat.pc1,p1stat.pc2)
                else:
                    return win.highcard(p1stat,p2stat,p1stat.pc1,0)
            elif p1stat.pc2 in straight and p1stat.pc2 not in board:
                return win.highcard(p1stat,p2stat,p1stat.pc2,0)          #setcard is player card involved in set

    def t_flush(p1stat,p2stat,board):
        flush1 = [p1stat.h1,p1stat.h2,p1stat.h3,p1stat.h4,p1stat.h5]
        flush2 = [p2stat.h1,p2stat.h2,p2stat.h3,p2stat.h4,p2stat.h5]

        if flush1==flush2:
            return win.highcard(p1stat,p2stat,0,0)


        max1=0
        max2=0

        if p1stat.pc1 in flush1 and p1stat.pc1 not in board:
            if p1stat.pc2 in flush1 and p1stat.pc2 not in board:
                if p1stat.pc1 > p1stat.pc2:
                    max1 = p1stat.pc1
                else:
                    max1 = p1stat.pc2
            else:
                max1 = p1stat.pc1
        else:
            max1 = p1stat.pc2

        if p2stat.pc1 in flush2 and p2stat.pc1 not in board:
            if p2stat.pc2 in flush2 and p2stat.pc2 not in board:
                if p2stat.pc1 > p2stat.pc2:
                    max2 = p2stat.pc1
                else:
                    max2 = p2stat.pc2
            else:
                max2 = p2stat.pc1
        else:
            max2 = p2stat.pc2

        if max1 > max2:
            return 1
        elif max2 > max1:
            return -1

    def t_straightflush(p1stat,p2stat):

        if p1stat.h1 > p2stat.h1:
            return 1
        elif p2stat.h1 > p1stat.h1:
            return -1

    def checktie(p1stat,p2stat,board):
        rank = p1stat.r

        if rank == 1:
            return win.highcard(p1stat,p2stat,0,0)

        if rank == 2:
            return win.t_onepair(p1stat,p2stat)

        if rank == 3:
            return win.t_twopair(p1stat,p2stat)

        if rank == 4:
            return win.t_threeset(p1stat,p2stat)

        if rank == 5:
            return win.t_straight(p1stat,p2stat,board)

        if rank == 6:
            return win.t_flush(p1stat,p2stat,board)

        if rank == 7:
            return win.t_fullhouse(p1stat,p2stat)

        if rank == 8:
            return win.t_fourset(p1stat,p2stat)

        if rank == 9:
            return win.t_straightflush(p1stat,p2stat)

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

    def set(hand,pstat):
        twoset=0
        threeset=0
        fourset=0

        for i in range(7):
            for j in range(i+1,7):
                if hand[i].n == hand[j].n:
                    twoset+=1

                    if twoset==1:
                        pstat.h1 = hand[i].n
                        pstat.h2 = hand[j].n
                    elif twoset ==2:
                        pstat.h3 = hand[i].n
                        pstat.h4 = hand[j].n
                    elif twoset==3:
                        if pstat.h1 > pstat.h3:
                            pstat.h3 = hand[i].n
                            pstat.h4 = hand[j].n

                        elif pstat.h1 < pstat.h3:
                            pstat.h1 = hand[i].n
                            pstat.h2 = hand[j].n

                    for k in range(j+1,7):
                        if hand[i].n == hand[k].n:
                            twoset=twoset-3
                            threeset+=1

                            if twoset == 0:
                                pstat.h3 = hand[k].n
                            elif twoset == 1:
                                pstat.h5 = hand[k].n

                            for l in range(k+1,7):
                                if hand[i].n == hand[l].n:
                                    threeset=threeset-4
                                    fourset+=1
                                    pstat.h1 = hand[i].n

        if twoset == 1 and threeset == 0:
            pstat.r =  2
        elif twoset >= 2 and threeset == 0:
            pstat.r =  3
        elif threeset == 1 and twoset == 0:
            pstat.r =  4
        elif threeset == 2 or (threeset == 1 and twoset == 1):
            pstat.r =  7
        elif fourset == 1:
            pstat.r =  8

        return

    def flush(hand,pstat):

        for i in range(7):
            for j in range(i+1,7):
                if hand[i].s == hand[j].s:
                    pstat.h1 = hand[i].n
                    pstat.h2 = hand[j].n
                    for k in range(j+1,7):
                        if hand[i].s == hand[k].s:
                            pstat.h3 = hand[k].n
                            for l in range(k+1,7):
                                if hand[i].s == hand[l].s:
                                    pstat.h4 = hand[l].n
                                    for m in range(l+1,7):
                                        if hand[i].s == hand[m].s:
                                            pstat.h5 = hand[m].n
                                            pstat.r = 6
                                            return pstat
        return pstat

    def straight(hand,pstat):
        min = []
        plist = [0,0,0,0,0]

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
                    plist[0] = (x.n)
                    plist[i]= (x.n)+i
                if count ==4:
                    pstat.h1 = plist[4]
                    pstat.h2 = plist[3]
                    pstat.h3 = plist[2]
                    pstat.h4 = plist[1]
                    pstat.h5 = plist[0]
                    pstat.r = 5
                    return pstat

        if pstat.r!=5:
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
                pstat.r=5
                pstat.h1 = 5
                pstat.h2 = 4
                pstat.h3 = 3
                pstat.h4 = 2
                pstat.h5 = 1

        return pstat

    def royalflush(hand,pstat):

        for x in range(1,5):
            count=0
            for y in hand:
                if (y.n == 10 or y.n==11 or y.n==12 or y.n==13 or y.n==14) and y.s==x:
                    count+=1

            if count==5:
                pstat.r = 10

        return pstat

    def straightflush(hand,pstat):

        plist = [0,0,0,0,0]
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
                        plist[i-1] = x.n+i
                        if count==4:
                            pstat.r = 9
                            pstat.h1 = plist[4]
                            return pstat

        return pstat

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

        pstat = win(1,0,0,0,0,0,0,0)

        card.royalflush(hand,pstat)

        if pstat.r != 10:
            win.reset(pstat)
            card.straightflush(hand,pstat)

            if pstat.r != 9:
                win.reset(pstat)
                card.set(hand,pstat)

                if pstat.r!=8:
                    win.reset(pstat)
                    card.set(hand,pstat)

                    if pstat.r!=7:
                        win.reset(pstat)
                        card.flush(hand,pstat)

                        if pstat.r != 6:
                            win.reset(pstat)
                            card.straight(hand,pstat)

                            if pstat!=5:
                                win.reset(pstat)
                                card.set(hand,pstat)
        pstat.pc1 = hand[0].n
        pstat.pc2 = hand[1].n

        return pstat


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

#deck.append(card(14,1))
#deck.append(card(4,4))
#deck.append(card(3,2))
#deck.append(card(8,2))
#deck.append(card(2,2))
#deck.append(card(9,4))
#deck.append(card(7,1))
#deck.append(card(7,3))
#deck.append(card(10,1))


player1 = []
player2 = []
board = []
boardnum = []

i=0
for _ in range(2):
    player2.append(deck[i])
    player1.append(deck[i+1])
    i+=2

for _ in range(5):
    board.append(deck[i])
    boardnum.append(deck[i].n)
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

p1stat = card.checkhand(player1 + board)
p2stat = card.checkhand(player2 + board)

print("P1:",end=" ")
card.finalres(p1stat.r)

print("P2:",end=" ")
card.finalres(p2stat.r)

print("----------")
print("RESULTS:")

res = 0
if p2stat.r > p1stat.r:
    res = -1
elif p1stat.r > p2stat.r:
    res = 1
elif p1stat.r == p2stat.r:
    res = win.checktie(p1stat,p2stat,boardnum)

if res == 1:
    print("You Win")
elif res== -1:
    print("You Lose")
elif res==0:
    print("Tie")
