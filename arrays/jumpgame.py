import sys

https://leetcode.com/problems/jump-game/description/
https://leetcode.com/problems/jump-game-ii/description/

# This is a DFS approach
# Very expensive
def minjumps(arr, mins, jumps=0, index=0):
    if index >= len(arr):
        return jumps

    for n in range(1, arr[index] + 1):
        res = minjumps(arr, mins, jumps + n, index + n)
        if res < mins:
            mins = res

    return mins



def test_minjumps_one():
    arr = [2,0,3,5,7,1,1,2,1,9]
    print(minjumps(arr, sys.maxint))