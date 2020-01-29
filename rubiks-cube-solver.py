#rubiks cube solver
#12 edge pieces: (W2, O7), (W5, B4), (W7, R2), (W4, G5), (R4, G7), (R7, Y2), (R5, B7), (Y4, G4), (Y7, O2), (Y5, B5), (O4, G2), (O5, B2)
#8 corner pieces: (W6, R1, G8), (W8, R3, B6), (W3, B1, O8), (W1, G3, O6), (Y1, R6, G6), (Y6, G1, O1), (Y3, R8, B8), (Y8, B3, O3)

#read cube with white facing downwards and green facing towards you
#color code: white=w, red=r, yellow=y, orange=o, blue=b, green=g
#        white red yellow orange blue green
cube = [ [  ], [  ], [  ], [  ], [  ], [  ] ]

solvedWhite = ['w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8']
solvedRed = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8']
solvedYellow = ['y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8']
solvedOrange = ['o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o8']
solvedBlue = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8']
solvedGreen = ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8']

#Define side variable, based off of the cube[index]
def defineSide():
    for i in range(len(cube)):
        if (i == 0):
            side = 'w'
        elif (i == 1):
            side = 'r'
        elif (i == 2):
            side = 'y'
        elif (i == 3):
            side = 'o'
        elif (i == 4):
            side = 'b'
        elif (i == 5):
            side = 'g'
    return side

#function that returns what each side(list) looks like, based on what letter you input
def getSide(side):
    if side == 'w':
        return cube[0]
    elif side == 'r':
        return cube[1]
    elif side == 'y':
        return cube[2]
    elif side == 'o':
        return cube[3]
    elif side == 'b':
        return cube[4]
    elif side == 'g':
        return cube[5]

#function returns a peice 
def getPeice(side, num): #Must be given num
    if side == 'w':
        return cube[0][num]
    elif side == 'r':
        return cube[1][num]
    elif side == 'y':
        return cube[2][num]
    elif side == 'o':
        return cube[3][num]
    elif side == 'b':
        return cube[4][num]
    elif side == 'g':
        return cube[5][num]

firstLevel = []
#Get first level
def getFirstLevel():
    firstLevel.append(
        cube[2][6], cube[2][7], cube[2][8], #red
        cube[4][6], cube[4][7], cube[4][8], #orange
        cube[5][6], cube[5][7], cube[5][8], #blue
        cube[6][6], cube[6][7], cube[6][8]) #green
    return firstLevel

#Test if first level is correct and matches its side
def isFirstLevelCorrect(firstLevel):
    counter = 0
    if cube[2][6] == cube[2][7] == cube[2][8] == 'r':
        counter += 1
    if cube[4][6] == cube[4][7] == cube[4][8] == 'o':
        counter += 1
    if cube[5][6] == cube[5][7] == cube[5][8] == 'b':
        counter += 1
    if cube[6][6] == cube[6][7] == cube[6][8] == 'o':
        counter += 1
    if counter == 4:
        return True
    return False

def isWhiteCrossSolved(cube):
    #use getSide() to return the white side, and check if the white cross is made
    side = getSide('w')
    if side[1] == 'w2' and side[3] == 'w4' and side[5] == 'w6' and side[7] == 'w8':
        return True
    else:
        return False

def whiteCross(cube):
    finished = False
    while finished == False:
        if  isWhiteCrossSolved(cube) == True:
            finished = True
        else:
            pass
            
def firstTwoLayers(cube):
    #count of how many corners have been completed, when count reaches 4, the first two layers are done
    count = 0
    while count < 4:
        #1st algorithm case
        if (cube[4][2] == 'w8' and cube[1][1] == 'r5') or \
            (cube[3][2] == 'w3' and cube[4][1] == 'b2') or \
                (cube[5][2] == 'w1' and cube[3][1] == 'o4') or \
                    (cube[1][2] == 'w6' and cube[5][1] == 'g7'):
            print("With {} side facing you, perform U, R, U', R'")

#The Solver Method
def solve(cube):
    solved = False
    while solved == False:
        if cube == [
            ['w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8'],
            ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8'],
            ['y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8'],
            ['o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o8'],
            ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8'],
            ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8']
        ]:
            solved = True
            return 'Cube solved'
        else:
            daisySolved = False
            while daisySolved == False:
                if getSide('y') == []:
                    pass
