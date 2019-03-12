#Value iteration
# This code has been Written by Anurag Sahu And Priyank Modi on the Night of before exams @ 12 - March - 2019
# AI Assignment 2

import sys
import copy


def move_possible(i, j):
    #check if wall
    if [i, j] in W:
        return False

    #out of the boundary
    if i < 0:
        return False
    if j < 0:
        return False
    if i >= n:
        return False
    if j > m or j == m:
        return False
        
    return True
    
def Prob_utility(i, j):
    maxVal = float("-inf")
    case_same = U[i][j]
    case_north = U[i-1][j]
    case_south = U[i+1][j]
    case_west = U[i][j-1]
    case_east = U[i][j+1]

    val = 0
    if (move_possible(i + 1, j)):
        val += 0.8 * case_south
    else:
        val += 0.8 * case_same
    if (move_possible(i, j - 1)):
        val += 0.1 * case_west
    else:
        val += 0.1 * case_same
    if (move_possible(i, j + 1)):
        val += 0.1 * case_east
    else:
        val += 0.1 * case_same
    #maxVal = max(maxVal, val)
    if(maxVal < val):
        maxVal = val
        Policy_Matrix[i][j] = "V"

    val = 0
    if (move_possible(i, j + 1)):
        val += 0.8 * case_east
    else:
        val += 0.8 * case_same
    if (move_possible(i + 1, j)):
        val += 0.1 * case_south
    else:
        val += 0.1 * case_same
    if (move_possible(i - 1, j)):
        val += 0.1 * case_north
    else:
        val += 0.1 * case_same
    # val += step_reward
    #maxVal = max(maxVal, val)
    if(maxVal < val):
        maxVal = val
        Policy_Matrix[i][j] = ">"

    val = 0
    if (move_possible(i - 1, j)):
        val += 0.8 * case_north
    else:
        val += 0.8 * case_same
    if (move_possible(i, j + 1)):
        val += 0.1 * case_east
    else:
        val += 0.1 * case_same
    if (move_possible(i, j - 1)):
        val += 0.1 * case_west
    else:
        val += 0.1 * case_same
    # val += step_reward
    #maxVal = max(maxVal, val)
    if(maxVal < val):
        maxVal = val
        Policy_Matrix[i][j] = "^"

    val = 0
    if (move_possible(i, j - 1)):
        val += 0.8 * case_west
    else:
        val += 0.8 * case_same
    if (move_possible(i + 1, j)):
        val += 0.1 * case_south
    else:
        val += 0.1 * case_same
    if (move_possible(i - 1, j)):
        val += 0.1 * case_north
    else:
        val += 0.1 * case_same
    # val += step_reward
    #maxVal = max(maxVal, val)
    if(maxVal < val):
        maxVal = val
        Policy_Matrix[i][j] = "<"

    return maxVal
        

if __name__ == '__main__':
    # size of grid
    [n, m] = [int(i) for i in input().split()]
    Policy_Matrix = [['-' for j in range(m+1)] for i in range(n+1)]
    policy = [[0 for j in range(m+1)] for i in range(n+1)]
    

    R = copy.deepcopy(policy)
    E = copy.deepcopy(policy)
    W = copy.deepcopy(policy)
    temp_U = copy.deepcopy(policy)
    U = copy.deepcopy(policy)
    #reward for each state
    for i in range(m):
        for j in range(n):
            R[i][j] = 0


    for i in range(1,n+1):
        L2 = [float(k) for k in input().split()]
        for j in range(1,m+1):
            R[i-1][j-1] = L2[j-1]

    # noof exit states and walls
    L3 = [int(i) for i in input().split()]
    e = L3[0]
    w = L3[1]

    #coord of exit states
    for i in range(2):
        for j in range(e):
            E[i][j] = 0

    for i in range(e):
        E[i] = [int(j) for j in input().split()]

    #coord of wall
    for i in range(2):
        for j in range(w):
            W[i][j] = 0

    for i in range(1,w+1):
        W[i-1] = [int(j) for j in input().split()]

    for i in input().split():
        start_state = int(i)

    step_reward = (input()) #unit step reward
    step_reward = float(step_reward)

    for i in range(m):
        for j in range(n):
            temp_U[i][j] = 0

    for i in range(m):
        for j in range(n):
            U[i][j] = 0

    for i in range(m):
        for j in range(n):
            U[i][j] = R[i][j]

    dis_fac = 0.99

    z = 0
    while True:
        z += 1
        delta = 0
        U = copy.deepcopy(temp_U)
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if [i-1, j-1] in E:
                    temp_U[i-1][j-1] = R[i-1][j-1]
                elif [i-1, j-1] in W:
                    temp_U[i-1][j-1] = 0
                else:
                    temp_U[i-1][j-1] = R[i-1][j-1] + step_reward + dis_fac * Prob_utility(i-1, j-1)
                delta = max(delta, abs(temp_U[i-1][j-1] - U[i-1][j-1]))

        print("iteration", z, "delta", delta)

        for row in range(len(temp_U)):
            print('-'*88)
            sys.stdout.write(str(row))
            for col in range(len(temp_U[row])):
                val = round(temp_U[row][col],3)
                sys.stdout.write(' | %14s'% val)
            print('|')
        print('-'*88)

        for i in range(n):
            for j in range(m):
                print(Policy_Matrix[i][j],end=' ')
            print()
        print("\n")

        if delta < 0.01*(1-dis_fac)/dis_fac:
            break

        
            




    
