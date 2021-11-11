# https://www.hackerrank.com/challenges/nested-list/problem


if __name__ == '__main__':
    python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

    sorted_students = sorted(python_students, key=lambda x: x[1])
    lowest_score = sorted_students[0][1]
    i = 1
    while (sorted_students[i][1] == lowest_score) & (i < len(python_students)):
        i += 1

    second_lowest_score = sorted_students[i][1]
    while (sorted_students[i][1] == second_lowest_score) & (i < len(python_students)):
        print(sorted_students[i][0])
        i += 1
















