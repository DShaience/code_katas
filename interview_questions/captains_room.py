# https://www.hackerrank.com/challenges/py-the-captains-room/problem
from collections import defaultdict

if __name__ == '__main__':
    rooms_assignments = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]
    k = 5
    assert (len(rooms_assignments) - 1) % k == 0, "Subtracting the captains room, the number of assignments must be divisible by k"

    room_assignment_counts = defaultdict(lambda: 0)
    for room_assignment in rooms_assignments:
        room_assignment_counts[room_assignment] += 1

    for room_number, num in room_assignment_counts.items():
        if num == 1:
            print(room_number)
            break


