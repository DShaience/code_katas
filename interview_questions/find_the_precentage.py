# https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    students = {"Krishna": [67, 68, 69],
                "Arjun": [70, 98, 63],
                "Malika": [52, 56, 60]
                }
    query_name = 'Malika'
    print(query_name, end=": ")
    print("{:.2f}".format(sum(students[query_name])/len(students[query_name])))
