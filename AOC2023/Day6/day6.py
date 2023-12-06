import numpy as np

datafile = "./day6.txt"

with open(datafile, "r") as f:
    lines = f.readlines()
    times = [int(l) for l in lines[0].strip().split(":")[1].split()]
    dists = [int(l) for l in lines[1].strip().split(":")[1].split()]


# completing the square
# dist = waittime * (ractime - waittime)
# use:
# d = w * (T - w)
# d = d0 <=>  # d0: time to beat
# wT - w**2 = d0
# w**2 - wT + T**2 / 4 = -d0 + T**2 / 4
# (w - T/2)**2 = -d0 + T**2 / 4
# w = T/2 +- sqrt(-d0 + T**2 / 4)
def calc_ways_to_beat(racetime, to_beat):
    lower_bound = racetime/2 - np.sqrt(-to_beat+racetime**2 / 4)
    upper_bound = racetime/2 + np.sqrt(-to_beat+racetime**2 / 4)
    lower_bound = np.ceil(lower_bound)
    upper_bound = np.floor(upper_bound)
    return upper_bound - lower_bound + 1


# PART A
multi = 1
for racetime, to_beat in zip(times, dists):
    num_wins = calc_ways_to_beat(racetime, to_beat)
    multi *= num_wins
print("A) Multiplication of ways to win:", int(multi))


# PART B
racetime = int("".join([str(i) for i in times]))
to_beat = int("".join([str(i) for i in dists]))

print("B) Ways to beat:", int(calc_ways_to_beat(racetime, to_beat)))