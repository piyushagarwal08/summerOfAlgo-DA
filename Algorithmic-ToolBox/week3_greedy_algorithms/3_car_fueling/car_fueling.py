# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    stops.insert(0,0)
    stops.append(distance)
    numRefills = 0
    currentRefill = 0
    while currentRefill < stops.index(distance):
        lastRefill = currentRefill
        while (currentRefill < stops.index(distance) and stops[currentRefill + 1] - stops[lastRefill] <= tank):
            currentRefill = currentRefill + 1
        if currentRefill == lastRefill :
            return -1
        if currentRefill < stops.index(distance):
            numRefills = numRefills + 1
    return numRefills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    #d,m, _, *stops = map(int,input().split())
    print(compute_min_refills(d, m, stops))
