import functools

def parse_lists(fileName):
    with open(fileName, 'r') as f:
        
        lines = f.readlines()

        firstList, secondList = [], [] 

        for line in lines:
            partialParse = line.strip().split(' ')
             

            getFistLast = lambda x: (x[0], x[-1])
            first_last = getFistLast(partialParse)
            firstList.append(int(first_last[0]))
            secondList.append(int(first_last[1]))
        
        firstList.sort()
        secondList.sort()
        
        return firstList, secondList

def getListDistances():
    lists = parse_lists('input.txt')
    distance = []
    for i in range(len(lists[0])):
        distance.append(abs(lists[0][i] - lists[1][i]))

    distance_sum = functools.reduce(lambda x, y: x + y, distance)
    print(distance_sum)

getListDistances()