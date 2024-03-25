import numpy as np

def riemanKiri (h, f ,n) :
    riemanleft = h * sum(f[:n-1])
    err_riemanl = 2 - riemanleft
    print("Nilai dari Method Rieman Kiri : ", riemanleft)
    print("Nilai dari Errornya : ", err_riemanl)

def riemanKanan (h, f) :
    riemanRight = h * sum(f[1::])
    err_riemanR = 2 - riemanRight
    print("Nilai dari Method Rieman Kanan : ", riemanRight)
    print("Nilai dari Errornya : ", err_riemanR)

def riemanTengah(h, n) :
    riemanMid = h * sum(np.cos(((2*np.pi*x[:n-1]) + (2*np.pi*x[1:]))/2))
    err_mid = 2 - riemanMid
    print("Nilai dari Method Rieman Tengah : ", riemanMid)
    print("Nilai dari Errornya : ", err_mid)

def trapesium (h, f, n):
    trap = (h / 2) * (f[0] + 2 * sum(f[1:n - 1]) + f[n - 1])
    err_trap = 2 - trap
    print("Nilai dari Method Trapesium : ", trap)
    print("Nilai dari Errornya : ", err_trap)

def simpson (h, f, n):
    simp = (h / 3) * (f[0] + 2 * sum(f[:n - 2:2]) + 4 * sum(f[1:n - 1:2]) + f[n - 1])
    err_simp = 2 - simp
    print("Nilai dari Method Simpson : ", simp)
    print("Nilai dari Error : ", err_simp)

if __name__ == "__main__":
    a = 0
    b = 1
    n = 4
    h = (b - a) / n
    x = np.linspace(a, b, n)
    f = np.cos(2 * np.pi * x)

    riemanKiri(h,f,n)
    print("")
    riemanKanan(h, f)
    print("")
    riemanTengah(h, n)
    print("")
    trapesium(h, f, n)
    print("")
    simpson(h, f, n)


