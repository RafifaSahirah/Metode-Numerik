def bedaMaju(f, x0, h):
    k = [0, 1, 2, 3, 4]
    for i in k:
        print("Untuk k ke -", i)
        result = (f(x0 + h(i)) - f(x0)) / h(i)
        print("Beda Maju : ", result)

def bedaMundur(f, x0, h):
    k = [0, 1, 2, 3, 4]
    for i in k:
        print("Untuk k ke -", i)
        result = (f(x0) - f(x0 - h(i))) / h(i)
        print("Beda Mundur: ", result)

def bedaTengah(f, x0, h):
    k = [0, 1, 2, 3, 4]
    for i in k:
        print("Untuk k ke -", i)
        result = (f(x0 + h(i)) - f(x0 - h(i))) / (2 * h(i))
        print("Beda Tengah : ", result)

def turunanKedua(f, x0, h):
    k = [0, 1, 2, 3, 4]
    for i in k:
        print("Untuk k ke -", i)
        result = (f(x0 - h(i)) - 2*f(x0) + f(x0 + h(i))) / h(i) ** 2
        print("Turunan Kedua : ", result)

if __name__ == "__main__":
    fx = lambda x: 0.1 * x ** 4 + 0.2 * x ** 3 + 0.4 * x ** 2 + 0.5 * x + 1
    x0 = 0
    h = lambda h1: 10 ** -h1
    bedaMaju(fx, x0, h)
    print("\n")
    bedaMundur(fx, x0, h)
    print("\n")
    bedaTengah(fx, x0, h)
    print("\n")
    turunanKedua(fx, x0, h)




