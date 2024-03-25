import sys
import traceback

class InterpolateNewton:
    X = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    Y = [7.03948302, 11.2347113, 15.3418565, 19.1049999, 23.2723955, 27.4985445, 31.6573844, 35.81462, 39.5455326, 43.4423335]

    def __init__(value):
        value.n = len(value.X)

    def compute(value):
        try:
            print("      x         y")
            result = 0
            for a in range(int(value.X[-1]) * 2 + 1):
                t = 0.5 * a
                if t == 4.5:
                    result = value.__interpolate(t)
                print("{:7.2f}\t\t{:7.4f}".format(t, value.__interpolate(t)))
            print("\nNilai dari f(4,5) adalah {:6.4f}".format(result))
        except Exception as e:
            raise

    def __interpolate(value, t):
        try:
            c = [0 for _ in range(value.n)]
            w = [0 for _ in range(value.n)]
            for i in range(0, value.n):
                w[i] = value.Y[i]
                for j in reversed(range(i)):
                    w[j] = (w[j + 1] - w[j]) / (value.X[i] - value.X[j])
                c[i] = w[0]
            s = c[value.n - 1]
            for i in reversed(range(value.n - 1)):
                s = s * (t - value.X[i]) + c[i]
            return s
        except Exception as e:
            raise

if __name__ == '__main__':
    try:
        obj = InterpolateNewton()
        obj.compute()
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)