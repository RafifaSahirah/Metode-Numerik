import numpy as np

class Data:
    def __init__(value, x, y):
        value.x = x
        value.y = y

def interpolate(f: list, xi: int, n: int) -> float:
    result = 0.0
    for i in range(n):
        temp = f[i].y
        for j in range(n):
            if j != i:
                temp = temp * (xi - f[j].x) / (f[i].x - f[j].x)
        result += temp
    return result

if __name__ == "__main__":
    f = [Data(1, 7.03948302), Data(2, 11.2347113), Data(3, 15.3418565), Data(4, 19.1049999), Data(5, 23.2723955),
         Data(6, 27.4985445), Data(7, 31.6573844), Data(8, 35.81462), Data(9, 39.5455326), Data(10, 43.4423335)]

    print("Nilai dari f(4.5) adalah", interpolate(f, 4.5, 10))