#rubiks cube solver
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
    for i in len(cube):
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
            solved = False
            # ^ temporary
