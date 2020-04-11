# Prakriti Kharel
import random

#final array that stores the mancala board with the correct values
#at the beginning, all the holes have rocks # of stones in them
rocks = 4
al = [0,rocks,rocks,rocks,rocks,rocks,0,rocks,rocks,rocks,rocks,rocks,0,rocks,rocks,rocks,rocks,rocks,0,rocks,rocks,rocks,rocks,rocks]
first = [0,rocks,rocks,rocks,rocks,rocks,0,rocks,rocks,rocks,rocks,rocks,0,rocks,rocks,rocks,rocks,rocks,0,rocks,rocks,rocks,rocks,rocks]
second = [0,rocks,rocks,rocks,rocks,rocks,0,rocks,rocks,rocks,rocks,rocks,0,rocks,rocks,rocks,rocks,rocks,0,rocks,rocks,rocks,rocks,rocks]
count = 0
c = 0

redMoves = [1, 2, 9, 10, 11, 13, 14, 21, 22, 23]
redMancala = [0, 12]
blueMoves = [3, 4, 5, 7, 8, 15, 16, 17, 19, 20]
blueMancala = [6, 18]

def reset(one,two):
    for i in range(23):
        two[i] = one[i]

def redCount():
    count = 0
    for i in range (10):
        count+= al[redMoves[i]]
    return count

def blueCount():
    count = 0
    for i in range (10):
        count+= al[blueMoves[i]]
    return count

#a function to decide who goes first
def flipaCoin():
    global turn;
    h1 = random.randint(0, 1)
    if (h1 == 0):
        print("Red Starts")
        turn = 'R'
        print("----------------------------------------------------------------------")



    else:
        print("Blue Starts")
        turn = 'B'
        print("----------------------------------------------------------------------")


def printfunc(final):


    print ("              ", "\033[96m {}\033[00m" .format(final[6]))
    print("           ", "\033[96m {}\033[00m" .format(final[7]), " ", "\033[96m {}\033[00m" .format(final[5]))
    print("           ", "\033[96m {}\033[00m" .format(final[8]), " ", "\033[96m {}\033[00m" .format(final[4]))

    print(" ", "\033[91m {}\033[00m" .format(final[11]), " ", "\033[91m {}\033[00m" .format(final[10]), " ", "\033[91m {}\033[00m" .format(final[9]), " ", "\033[96m {}\033[00m" .format(final[3]), " ", "\033[91m {}\033[00m" .format(final[2]), " ", "\033[91m {}\033[00m" .format(final[1]), " ")
    print("\033[91m {}\033" .format(final[12]), "                          ", "\033[91m {}\033[00m" .format(final[0]))
    print(" ", "\033[91m {}\033[00m" .format(final[13]), " ", "\033[91m {}\033[00m" .format(final[14]), " ", "\033[96m {}\033[00m" .format(final[15]), " ", "\033[91m {}\033[00m" .format(final[21]), " ", "\033[91m {}\033[00m" .format(final[22]), " ", "\033[91m {}\033[00m" .format(final[23]), " ")
    print("           ", "\033[96m {}\033[00m".format(final[16]), " ", "\033[96m {}\033[00m".format(final[20]))
    print("           ", "\033[96m {}\033[00m".format(final[17]), " ", "\033[96m {}\033[00m".format(final[19]))
    print ("              ", "\033[96m {}\033[00m" .format(final[18]))

#without color
'''
    print ("              ", final[6])
    print ("            ", final[7]," ", final[5])
    print ("            ", final[8]," ", final[4])
    print ("    ", final[8]," ", final[4]," ", final[8]," ", final[8]," ",final[8]," ",final[8]," ")
    print (" ",final[12],"                        ", final[0])
    print ("    ", final[13]," ", final[14]," ", final[15]," ", final[21]," ",final[22]," ",final[23]," ")
    print ("            ", final[16]," ", final[20])
    print ("            ", final[17]," ", final[19])
    print ("              ", final[18])
    '''

#The red positions are 1 2 9 10 11 13 14 21 22 23
#given a particular index move the stones
#def blue moves
def moves(given, temp):
    global turn;

    #first check if its a blue moving or red moving
    if given in blueMoves:
        turn = 'B'
    if given in redMoves:
        turn = 'R'


    #figuring out how many rocks are there at a given index
    #decided on a clockwise direction
    storing = temp[given]
    temp[given] = 0
    while storing != 0:
        storing -= 1
         #figuring out how to loop after 23, i want to go to 0
        if (given == 23):
            given = 0
        else:
            given += 1

        #skip the other player's mancala
        if (turn == 'B' and (given == 0 or given == 12)):
            given += 1
            if (temp == al):
                print("skipping red's mancala")
        elif (turn == 'R' and (given == 6 or given == 18)):
            given += 1
            if (temp == al):
                print(" skipping blue's mancala")
        temp[given] += 1

        #need to figure out if it lands on empty on its side, which rocks to add to whose mancala
        # + 6, - 6 works because then you are emptying two of opponents and adding it to your mancala
        #the only problem is there are special cases: 23 + 6, 0 -6 # edge cases

        if ((turn == 'R') and (given in redMoves) and (temp[given] == 1)):
            if (temp == al):
                print("adjacent stones added to red's mancala")
            temp[0] += 1  #adding that particular one
            temp[given] -= 0
            #dealing with edge cases
            if(given == 2):
                temp[0] += temp[20]
                temp[20] = 0
                temp[0] += temp[given + 6]
                temp[given + 6] = 0
            elif (given == 1):
                temp[0] += temp[19]
                temp[19] = 0
                temp[0] += temp[given + 6]
                temp[given + 6] = 0

            elif (given == 23):
                temp[0] += temp[5]
                temp[5] = 0
                temp[0] += temp[given - 6]
                temp[given - 6] = 0

            elif (given == 22):
                temp[0] += temp[4]
                temp[4] = 0
                temp[0] += temp[given - 6]
                temp[given - 6] = 0

            elif (given == 21):
                temp[0] += temp[3]
                temp[3] = 0
                temp[0] += temp[given - 6]
                temp[given - 6] = 0

            else: #rest of the cases
                temp[0] += temp[given+6]
                temp[0] += temp[given-6]
                temp[given - 6] = 0
                temp[given + 6] = 0

            #take all the stone from adjacent and add to blue's mancala
        elif ((turn == 'B') and (given in blueMoves) and (temp[given] == 1)):
            if (temp == al):
                print("adjacent stones added to blue's mancala")
            temp[6] += 1
            temp[given] -= 0
            #dealing with edge cases

            if (given == 20):
                temp[6] += temp[2]
                temp[2] = 0
                temp[6] += temp[given - 6]
                temp[given - 6] = 0
            elif (given == 19):
                temp[6] += temp[1]
                temp[1] = 0
                temp[6] += temp[given - 6]
                temp[given - 6] = 0

            elif (given == 5):
                temp[6] += temp[23]
                temp[23] = 0
                temp[6] += temp[given + 6]
                temp[given + 6] = 0

            elif (given == 4):
                temp[6] += temp[22]
                temp[22] = 0
                temp[6] += temp[given + 6]
                temp[given + 6] = 0

            elif (given == 3):
                temp[6] += temp[21]
                temp[21] = 0
                temp[6] += temp[given + 6]
                temp[given + 6] = 0

            else: #rest of the cases
                temp[6] += temp[given + 6]
                temp[6] += temp[given - 6]
                temp[given - 6] = 0
                temp[given + 6] = 0

#Notes:


def whoNext(given):
    global turn
    printfunc(al)
    # ends in their own mancala
    if (turn == 'R' and (given == 0 or given == 12)):
        turn == 'R'
        print("Next, its red's turn again")
    elif (turn == 'B' and (given == 6 or given == 18)):
        print("Next, its blue's turn again")
        turn = 'B'
    elif (turn == 'B'):
        print("Next, it's reds turn")
        turn = 'R'
    else:
        print("Next, it's blue's turn")
        turn = 'B'
    print("")

    
#if all of red moves is 0 or all of blue moves is 0, then the game has ended
def gameOver():
    if (redCount() == 0 or blueCount() == 0):
        return True
    else:
        return False


#should use h1 and h2
def computerVcomputer1():
    flipaCoin()
    temp = 0
    while (not gameOver()):
        temp += 1
        if (turn == 'B'):
            minMax1b()
        else:
            minMax2r()
    print("the count for red  is ", count)
    print("the count for blue  is ", c)

    print("# of rounds ", temp)
    mancalaCount(al)

def computerVcomputer2():
    flipaCoin()
    temp = 0

    while (not gameOver()):
        temp += 1
        if (turn == 'B'):
            minMax2b()
        else:
            minMax1r()
    print("the count is ", count)
    print("# of rounds ", temp)
    mancalaCount(al)



#should use either h1 or h2 random
def computerVperson():
    temp = 0
    whoAmI= "red"
    heuristic = "one"
    h1 = random.randint(0, 1)
    if (h1 == 0):
        print("you are red")
    else:
        whoAmI= "blue"
        print("you are blue")

    h2 = random.randint(0, 1)
    if (h2 == 0):
        print("hint: the computer will use heuristic 1, this was decided using the rand.randint  function")
        heuristic = "zero"
    else:
        print("hint: the computer will use heuristic 2, this was decided using the rand.randint function")
        heuristic = "one"

    flipaCoin()

    if (whoAmI == "red"):
        while (not gameOver()):
           # printfunc(al)
            temp += 1
            if (turn == 'B'):
                if (heuristic == "one"):
                    minMax1b()
                else:
                    minMax2b()

            else:
                print("What moves would you like to make, you are red, your options are the following positions: ", redMoves)
                given = int(input())
                moves(given, al)
                whoNext(al)
    else:
        while (not gameOver()):
         #   printfunc(al)
            temp +=1
            if (turn == 'R'):
                if (heuristic == "one"):
                    minMax1r()
                else:
                    minMax2r()
            else:
                print("What moves would you like to make, you are blue, your options are the following positions: ", blueMoves)
                given = int(input())
                moves(given, al)
                whoNext(al)

    print("the count is ", count)
    print("# of rounds ", temp)
    mancalaCount(al)


#want minMax to make one move, #try to get most rocks in mancala
#right now assuming red moves first

def minMax1r():
    # assume red is starting first
    global count
    reset(al, first)
    reset(al, second)
   # count = 0
    redsmax = []  # array of blue's choices, red wants to pick the maximum one
    bluesmax = []
    redsmin = []  # mancala count for red player, when blue expands, blue is gonna choose the one where red mancala count is lowest
    bluesmin = []

    for i in range(10):  # select the max
        min = 0
        count += 1
        moves(redMoves[i], first)
        moves(redMoves[i], second)
        for i in range(10):  # select the min #add if else for alpha-beta pruning

            count += 1
           # print("the count in the second loop is ", count)
            moves(blueMoves[i], second)
            # printfunc(second)
            redsmin.append(redFinal(second))
            #bluesmin.append(blueFinal(second))
            reset(first, second)
            if (redFinal(second) == 0):
                break

       # print("reds min is",  redsmin)

        # go through redsmin, and add the smallest one to redsmax
        #alpha-beta pruning, its going to choose  the minimum, if its 0, stop
        #alpha > beta, you cut off
        beta = 100
        for i in range(len(redsmin)):
            count+=1
            if (redsmin[i] < beta):
                beta = redsmin[i]
                if (beta == 0):
                    break
        redsmax.append(beta)
        redsmin = []
        bluesmin = []
        reset(al, first)
       # print("redsmax is ", redsmax)

    alpha = 0
    s = 0
    for i in range(len(redsmax)):
        if (redsmax[i] > alpha and al[redMoves[i]] != 0):
            choice = redsmax[i]
            s = i
    print("R chose", redMoves[s], "which has", al[redMoves[s]], "stones")
    moves(redMoves[s], al)
    whoNext(redMoves[s])



def minMax1b():
    global c
    #assume red is starting first
    reset(al, first)
    reset(al, second)
    redsmax= [] #array of blue's choices, red wants to pick the maximum one
    bluesmax= []
    redsmin = [] #mancala count for red player, when blue expands, blue is gonna choose the one where red mancala count is lowest
    bluesmin = []


    for i in range(10): #select the max
        c+=1
        moves(blueMoves[i], first)
        moves(blueMoves[i], second)
        for i in range(10):  #select the min #add if else for alpha-beta pruning
            c+=1
            moves(redMoves[i], second)
           # printfunc(second)
          #  redsmin.append(redFinal(second))
            bluesmin.append(blueFinal(second))
            reset(first, second)
            if (blueFinal(second) == 0):
                break

      #  print("reds min is ", redsmin)
      #  print("blues min is ", bluesmin)


        #go through redsmin, and add the smallest one to redsmax
        beta = 100
        for i in range(len(bluesmin)):
            c += 1
            if (bluesmin[i] < beta):
                beta= bluesmin[i]
                if (beta == 0):
                    break
        bluesmax.append(beta)
        redsmin = []
        bluesmin = []
        reset(al, first)

    alpha = 0
    s = 0
    for i in range (len(bluesmax)):
        if (bluesmax[i] > alpha and al[blueMoves[i]] != 0 ):
            alpha = bluesmax[i]
            s = i

    print("B chose", blueMoves[s], "which has", al[blueMoves[s]], "stones")
    moves(blueMoves[s], al)
    whoNext(blueMoves[s])




    #make the move
    #store bluecount, store red count
    #reset
#get as many holes empty as possible
def minMax2r():

    global count
    # assume red is starting first
    reset(al, first)
    reset(al, second)
    redsmax = []  # array of blue's choices, red wants to pick the maximum one
    bluesmax = []
    redsmin = []  # mancala count for red player, when blue expands, blue is gonna choose the one where red mancala count is lowest
    bluesmin = []

    for i in range(10):  # select the max
        count += 1
        moves(redMoves[i], first)
        moves(redMoves[i], second)
        for i in range(10):  # select the min #add if else for alpha-beta pruning
            count += 1
            moves(blueMoves[i], second)
            # printfunc(second)
            redsmin.append(emptyHoles(second))
            reset(first, second)
            # if (emptyHoles(second) == 1):
            #     break
      #  print("reds min is ", redsmin)

        # go through redsmin, and add the smallest one to redsmax
        #alpha-beta pruning, its going to choose  the minimum, if its 0, stop
        beta = 100
        for i in range(len(redsmin)):
            count+=1
            if (redsmin[i] < beta):
                beta = redsmin[i]
                # if (beta == 1):
                #     break
        redsmax.append(beta)
        redsmin = []
        bluesmin = []
        reset(al, first)
       # print("redsmax is ", redsmax)

    alpha = 0
    s = 0
    for i in range(len(redsmax)):
        if (redsmax[i] > alpha and al[redMoves[i]] != 0):
            choice = redsmax[i]
            s = i
    print("R chose", redMoves[s], "which has", al[redMoves[s]], "stones")
    moves(redMoves[s], al)
    whoNext(redMoves[s])

def minMax2b():
    global count

    #assume red is starting first
    reset(al, first)
    reset(al, second)
    redsmax= [] #array of blue's choices, red wants to pick the maximum one
    bluesmax= []
    redsmin = [] #mancala count for red player, when blue expands, blue is gonna choose the one where red mancala count is lowest
    bluesmin = []


    for i in range(10): #select the max
        count+=1
        #moves(blueMoves[i], first)
        #moves(blueMoves[i], second)
        for i in range(10):  #select the min #add if else for alpha-beta pruning
            count+=1
            #moves(redMoves[i], second)
           # printfunc(second)
            bluesmin.append(emptyHoles(second))
            reset(first, second)
            if (emptyHoles(second) == 1):
                break

      #  print("reds min is ", redsmin)
      #  print("blues min is ", bluesmin)


        #go through redsmin, and add the smallest one to redsmax
        beta = 100

        for i in range(len(bluesmin)):
            count+=1
            if (bluesmin[i] < beta):
                beta= bluesmin[i]
                if (beta == 1):
                    break
        bluesmax.append(beta)
        redsmin = []
        bluesmin = []
        reset(al, first)

    alpha = 0
    s = 0
    for i in range (len(bluesmax)):
        if (bluesmax[i] > alpha and al[blueMoves[i]] != 0 ):
            alpha = bluesmax[i]
            s = i
    print("B chose", blueMoves[s], "which has", al[blueMoves[s]], "stones")
    moves(blueMoves[s], al)
    whoNext(blueMoves[s])


def emptyHoles(final):
    temp = 0
    for i in range(10):
        if (final[i] == 0):
            temp += 1
    return temp


def blueFinal(final):
    temp = 0
    temp +=final[6]
    temp += final[18]
    return temp

def redFinal(final):
    temp = 0
    temp += final[0]
    temp += final[12]
    return temp


#final count
def mancalaCount(final):
  #combining 2 mancala
    final[0] += final[12]
    final[12] = 0
    final[6] += final[18]
    final[18] = 0

    #if turn == b, all of blue's spots are empty, so red can add all the remaining to their mancala
    if (turn == 'B'):
        #go through the remining
        for x in redMoves:
            final[0] += final[x]
            final[x] = 0

    #if turn == r, then red's spots are empty, so blue can add all the reaminign thir mancala
    else:
        for x in blueMoves:
            final[6] += final[x]
            final[x] = 0

    print("blues total count is", final[6], "red's total count is", final[0])
    if (final[6] > final[0]):
        print ("Blue won this round")
    elif(final[0] > final[6]):
        print("Red won this round")
    else:
        print("It was a tie")


#redundant for now but want to wrap it around main incase i want to add code later on
def main():
   # computerVcomputer1()
     #computerVcomputer2()
    computerVperson()

main()
