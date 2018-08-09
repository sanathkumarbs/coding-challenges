def nutsbolts(nuts, bolts):
    print nuts[0]
    return recurse_solve(nuts, bolts, 0, len(bolts), 0, [])
    
def recurse_solve(nuts, bolts, start, end, pivot, result=[]):
    if start >= end:
        return
    
    match = partition(bolts, start, end, nuts[pivot])

    # print "start: ", start, "end: ", end, "match: ", match

    result.append(str(nuts[pivot]) + " " + str(bolts[match]))

    if (pivot + 1) < len(nuts):
        if bolts[match] > nuts[pivot + 1]:
            # print "recursing"
            # print "start: ", start, "end: ", match, "pivot: ", pivot + 1, "pval: ", nuts[pivot + 1]
            # print "bolts: ", bolts
            # print " "
            recurse_solve(nuts, bolts, 0, match, pivot + 1, result)
        else:
            # print "recursing"
            # print "start: ", match + 1, "end: ", end, "pivot: ", pivot + 1, "pval: ", nuts[pivot + 1]
            # print "bolts: ", bolts
            # print " "
            recurse_solve(nuts, bolts, match + 1, len(bolts), pivot + 1, result)
            
    return result

def partition(arr, start, end, pivot):
    partitionpoint = start
    foundat = None

    for curr in range(start, end):
        if arr[curr] < pivot:
            arr[curr], arr[partitionpoint] = arr[partitionpoint], arr[curr]
            partitionpoint += 1
        elif arr[curr] == pivot:
            foundat = curr
            partitionpoint += 1

    arr[foundat], arr[partitionpoint - 1] = arr[partitionpoint - 1], arr[foundat]

    return partitionpoint - 1

def test_nutsbolts_one():
    nuts = [4, 32, 5, 7]
    bolts = [32, 7, 5, 4]

    res = nutsbolts(nuts, bolts)
    print "\n".join(res)

def test_nutsbolts_two():
    nuts = [6, 38, 32, 35, 9, 19, 21]
    bolts = [6, 32, 35, 21, 38, 19, 9]

    res = nutsbolts(nuts, bolts)
    print "\n".join(res)