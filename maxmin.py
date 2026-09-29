

def min_max(tests):
    lowest = tests[0]
    highest = tests[0]

    for i in tests:
        if i > highest:
            highest = i
        if i < lowest:
            lowest = i

    return [lowest, highest]



#test cases

test1 = [2,4,1,0,2,-1]
test2 = [20,50,12,6,14,8]
test3 = [100,-100]

print(min_max(test1))
print(min_max(test2))
print(min_max(test3))
