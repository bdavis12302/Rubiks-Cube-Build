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

def getSide(side):
    if side == w:
        return cube[0]
    elif side == r:
        return cube[1]
    elif side == y:
        return cube[2]
    elif side == o:
        return cube[3]
    elif side == b:
        return cube[4]
    elif side == g:
        return cube[5]

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
        else:
            solved = False
            # ^ temporary
