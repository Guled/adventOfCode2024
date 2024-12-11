
## TBD need to fix the logic for this one.
## Answer not 558, 558 is too low.
multiline_string = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

def parse_input_file(fileName):
    with open(fileName, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        return lines

def parse_input_text(text):
    lines = text.split('\n')
    lines = [line.strip() for line in lines]
    lines = list(filter(lambda x: x != '', lines))
    return lines

def validate_list(lst):

    count_safe_reports = 0
    for line in lst:
        line = line.split(' ')
        line = list(filter(lambda x: x != '', line))
        state = "unknown"
        safe = True
        freebie = True

        for report_index in range(len(line)):
            if len(line) == 0 or len(line) == 1 or report_index == len(line) - 1:
                continue
            else:
                if state == "unknown":
                    difference = int(line[report_index]) - int(line[report_index + 1])
                    if difference > 0:
                        state = "increasing"
                    elif difference < 0:
                        state = "decreasing"
                    if abs(difference) < 1 or abs(difference) > 3:
                            safe = False

                else:
                    difference = int(line[report_index]) - int(line[report_index + 1])
                    if difference > 0 and state == "decreasing":
                        if freebie:
                            freebie = False
                        else:   
                            safe = False
                    elif difference < 0 and state == "increasing":
                        if freebie:
                            freebie = False
                        else:
                            safe = False
                    if abs(difference) < 1 or abs(difference) > 3:
                        if freebie:
                            freebie = False
                        else:
                            safe = False
                        
        if safe:
            count_safe_reports += 1

    return count_safe_reports


if __name__ == "__main__":
    # print(validate_list(parse_input_text(multiline_string)))
    print(f'Part 2 Answer: {validate_list(parse_input_file('day_2/input.txt'))}')


