import math

def period(L, g):
    if g == 0:
        raise ValueError
    elif isinstance(L, str):
        raise TypeError
    elif isinstance(g, str):
        raise TypeError
    elif abs(L - g) < 0.000001:
        raise ValueError
    else:
        return 2 * math.pi * math.sqrt(float(L)/float(g))

length = 5
gravity = 6
T = float(period(length, gravity))
print('The period of the pendulum is ' + str(T))