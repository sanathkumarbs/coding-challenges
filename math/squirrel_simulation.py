#!/usr/bin/env python
"""Squirrel Simulation."""
 
# There's a tree, a squirrel, and several nuts. Positions are represented by
# the cells in a 2D grid. Your goal is to find the minimal distance for the
# squirrel to collect all the nuts and put them under the tree one by one.
# The squirrel can only take at most one nut at one time and can move in
# four directions - up, down, left and right, to the adjacent cell. 
# The distance is represented by the number of moves.
#
# https://leetcode.com/articles/squirrel-simulation/

# Input: 
#   Height : 5
#   Width : 7
#   Tree position : [2,2]
#   Squirrel : [4,4]
#   Nuts : [[3,0], [2,5]]
# Output: 12

def min_distance(height, width, tree_pos, squirell_pos, list_nut_pos):
    costs = []
    # costs = [tree_nut_tree_distance, squirrel_nut_tree_distance, diff]

    for nut_pos in list_nut_pos:
        tree_nut = abs(nut_pos[0]-tree_pos[0]) + abs(nut_pos[1]-tree_pos[1])
        squirell_nut = abs(nut_pos[0]-squirell_pos[0]) + abs(nut_pos[1]-squirell_pos[1])
        
        tree_nut_tree = 2 * tree_nut
        squirell_nut_tree = tree_nut + squirell_nut
        diff = tree_nut_tree - squirell_nut_tree

        res = (tree_nut_tree, squirell_nut_tree, diff)
        print ""
        print nut_pos
        print res
        print ""

        costs.append(res)

    print costs

def test_min_distance_one():
    height = 5
    width = 7
    tree_pos = [2, 2]
    squirell_pos = [4, 4]
    list_nut_pos = [
        [3,0],
        [2,5]
    ]
    min_distance(height, width, tree_pos, squirell_pos, list_nut_pos)

def test_min_distance_two():
    height = 5
    width = 7
    tree_pos = [2, 2]
    squirell_pos = [4, 4]
    list_nut_pos = [
        [0, 0],
        [0, 3],
        [0, 6],
        [2, 5],
        [3, 0]
    ]
    min_distance(height, width, tree_pos, squirell_pos, list_nut_pos)