#rubiks cube solver
#color code: white=w, red=r, yellow=y, orange=o, blue=b, green=g
#        white red yellow orange blue green
cube = [ [  ], [  ], [  ], [  ], [  ], [  ] ]

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
