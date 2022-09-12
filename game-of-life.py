#!/usr/bin/env python3
import copy
import time
import os

array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

max_x = len(array[0])-1
max_y = len(array)-1

def find_alive_cells(array):
    alive_cells = []
    index_y = 0
    for row in array:
        index_x = 0
        for item in row:
            if item == 1:
                alive_cells.append({"x": index_x, "y": index_y})
            index_x += 1
        index_y += 1
    
    return alive_cells

## Neigbor checking stuff
def has_neighbor_1(array, x, y, neighbors):
    if array[y-1][x-1] == 1:
        neighbors[0] = True
    else:
        neighbors[0] = False

def has_neighbor_2(array, x, y, neighbors):
    if array[y-1][x] == 1:
        neighbors[1] = True
    else:
        neighbors[1] = False

def has_neighbor_3(array, x, y, neighbors):
    if array[y-1][x+1] == 1:
        neighbors[2] = True
    else:
        neighbors[2] = False

def has_neighbor_4(array, x, y, neighbors):
    if array[y][x-1] == 1:
        neighbors[3] = True
    else:
        neighbors[3] = False

def has_neighbor_5(array, x, y, neighbors):
    if array[y][x+1] == 1:
        neighbors[4] = True
    else:
        neighbors[4] = False

def has_neighbor_6(array, x, y, neighbors):
    if array[y+1][x-1] == 1:
        neighbors[5] = True
    else:
        neighbors[5] = False

def has_neighbor_7(array, x, y, neighbors):
    if array[y+1][x] == 1:
        neighbors[6] = True
    else:
        neighbors[6] = False

def has_neighbor_8(array, x, y, neighbors):
    if array[y+1][x+1] == 1:
        neighbors[7] = True
    else:
        neighbors[7] = False


## Evaluate neighbors
def evaluate_neighbors(array, x, y, max_x, max_y):
    neighbors = [False, False, False, False, False, False, False, False]
 
    if y == 0:
        if x == 0:
            has_neighbor_8(array, x, y, neighbors)
            has_neighbor_5(array, x, y, neighbors)
            has_neighbor_7(array, x, y, neighbors)
            #print("Case 1 x=" + str(x) + " y=" + str(y) + " Top left corner")
        if x > 0 and x < max_x:
            has_neighbor_4(array, x, y, neighbors)
            has_neighbor_5(array, x, y, neighbors)
            has_neighbor_6(array, x, y, neighbors)
            has_neighbor_7(array, x, y, neighbors)
            has_neighbor_8(array, x, y, neighbors)
            #print("Case 2 x=" + str(x) + " y=" + str(y) + " Top row")
        if x == max_x:
            has_neighbor_7(array, x, y, neighbors)
            has_neighbor_6(array, x, y, neighbors)
            has_neighbor_4(array, x, y, neighbors)
            #print("Case 3 x=" + str(x) + " y=" + str(y) + " Top right corner")
    
    elif y == max_y:
        if x == 0:
            has_neighbor_2(array, x, y, neighbors)
            has_neighbor_3(array, x, y, neighbors)
            has_neighbor_5(array, x, y, neighbors)
            #print("Case 4 x=" + str(x) + " y=" + str(y) + " Bottom left corner")
        if x > 0 and x < max_x:
            has_neighbor_1(array, x, y, neighbors)
            has_neighbor_2(array, x, y, neighbors)
            has_neighbor_3(array, x, y, neighbors)
            has_neighbor_4(array, x, y, neighbors)
            has_neighbor_5(array, x, y, neighbors)
            #print("Case 5 x=" + str(x) + " y=" + str(y) + " Bottom row")
        if x == max_x:
            has_neighbor_1(array, x, y, neighbors)
            has_neighbor_2(array, x, y, neighbors)
            has_neighbor_4(array, x, y, neighbors)
            #print("Case 6 x=" + str(x) + " y=" + str(y) + " Bottom rignt corner")
    
    elif x == max_x:
        if y > 0 and y < max_y:
            has_neighbor_2(array, x, y, neighbors)
            has_neighbor_4(array, x, y, neighbors)
            has_neighbor_1(array, x, y, neighbors)
            has_neighbor_6(array, x, y, neighbors)
            has_neighbor_7(array, x, y, neighbors)
            #print("Case 7 x=" + str(x) + " y=" + str(y) + " Right column")
    elif x == 0:
        if y > 0 and y < max_y:
            has_neighbor_2(array, x, y, neighbors)
            has_neighbor_3(array, x, y, neighbors)
            has_neighbor_5(array, x, y, neighbors)
            has_neighbor_7(array, x, y, neighbors)
            has_neighbor_8(array, x, y, neighbors)
            #print("Case 8 x=" + str(x) + " y=" + str(y) + " Left column")
    
    else:
        has_neighbor_1(array, x, y, neighbors)
        has_neighbor_2(array, x, y, neighbors)
        has_neighbor_3(array, x, y, neighbors)
        has_neighbor_4(array, x, y, neighbors)
        has_neighbor_5(array, x, y, neighbors)
        has_neighbor_6(array, x, y, neighbors)
        has_neighbor_7(array, x, y, neighbors)
        has_neighbor_8(array, x, y, neighbors)
        #print("Np special case")

    return neighbors

## Conway's sules
def game_of_life(array, max_x, max_y):
    new_array = copy.deepcopy(array)
    index_y = 0
    for row in array:
        index_x = 0
        for item in row:
            #print(f'{index_x} -- {index_y}')
            neighbors = evaluate_neighbors(array, index_x, index_y, max_x, max_y)
            
            if neighbors.count(True) < 2:
                new_array[index_y][index_x] = 0
                #print("Cell dies due to underpopulation")
            elif neighbors.count(True) == 3:
                new_array[index_y][index_x] = 1
                #print("Cell resurrectes")
            elif neighbors.count(True) > 3:
                new_array[index_y][index_x] = 0
                #print("Cell dies of overpopulation")
            index_x += 1
            
        index_y += 1
        
    return new_array

def print_array(array):
    os.system("clear")
    for row in array:
        for item in row:
            if item == 1:
                print("⬜", end="")
            else:
                print("⬛", end="")
        print()

    print("--- Iteration " + str(iteration) + " ---")

iteration = 0
switch = 1
while switch == 1:
    print_array(array)
    x = input("x> ")
    if x == "done":
        break
    y = input("y> ")
    array[int(y)][int(x)] = 1
    
input("Press enter to continue...")

while True:
    os.system("clear")
    iteration += 1
    array = game_of_life(array, max_x, max_y)
    for row in array:
        for item in row:
            if item == 1:
                print("⬜", end="")
            else:
                print("⬛", end="")
        print()
    print("--- Iteration " + str(iteration) + " ---")
    time.sleep(0.10)
