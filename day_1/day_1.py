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

def getListDistances_part_1():
    lists = parse_lists('day_1/input.txt')
    distance = []
    for i in range(len(lists[0])):
        distance.append(abs(lists[0][i] - lists[1][i]))

    distance_sum = functools.reduce(lambda x, y: x + y, distance)
    return distance_sum


def getListDistances_part_2():
    input_lists = parse_lists('day_1/input.txt')
    similarity_score = []
    for i in range(len(input_lists[0])):

        found_values = list(filter(lambda x: x == input_lists[0][i], input_lists[1]))
        similarity_score.append(len(found_values) * input_lists[0][i])

    similarity_score_sum = functools.reduce(lambda x, y: x + y, similarity_score)

    return similarity_score_sum


if __name__ == "__main__":
    print(f'Part 1 Answer:{getListDistances_part_1()}')
    print(f'Part 2 Answer:{getListDistances_part_2()}')