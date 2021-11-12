# https://www.hackerrank.com/challenges/text-wrap/problem

if __name__ == '__main__':
    text = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    width = 4

    n = (len(text) // width) + min([(len(text) % width), 1])
    ranges = [(i, i+width) for i in range(0, n*width, width)]
    i = 1
    for rng in ranges:
        print(text[rng[0]:rng[1]])
