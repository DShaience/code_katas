# https://www.hackerrank.com/challenges/designer-door-mat/problem

if __name__ == '__main__':
    N = 9       # number of rows
    M = N * 3   # chars in each row

    pattern_01 = '---'
    pattern_02 = '.|.'

    mat = ''
    lines = []
    mid_repeats = 1
    for i in range(0, N // 2):
        edges = ((N // 2) - i) * pattern_01
        mid = (mid_repeats * pattern_02)
        mid_repeats += 2
        line = edges + mid + edges + '\n'
        lines.append(line)

    mid_line = '-' * ((M // 2) - 3) + 'WELCOME' + '-' * ((M // 2) - 3) + '\n'
    mat = "".join(lines) + mid_line + "".join(lines[::-1])

    print(mat)


