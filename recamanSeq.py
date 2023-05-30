# https://www.youtube.com/watch?v=FGC5TdIiT9U
"""
pivot | index |= current
0 - 0 = 0
0 - 1 = -1 (false)
0 + 1 = 1
1 - 2 = -1 (false)
1 + 2 = 3
3 - 3 = 0 (repeated)
3 + 3 = 6
6 - 3 = 3 (repeated)
3 - 4 = -1 (false)
3 + 4 = 7
"""


def recaman(n):
    sequence = []
    standingPoint = 0

    for number in range(0, n):
        nextPoint = standingPoint - number
        if nextPoint < 0 or nextPoint in sequence:
            nextPoint = standingPoint + number

        sequence.append(nextPoint)
        standingPoint = nextPoint
    return sequence


if __name__ == '__main__':
    print(recaman(54))

# sequence = []
#     pivot = 0
#
#     for index in range(0, n):
#         pivot = (pivot - index) if (pivot - index >= 0) and (pivot - index) not in sequence else pivot + index
#         sequence.append(pivot)
#     return sequence
