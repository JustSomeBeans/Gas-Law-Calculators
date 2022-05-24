def cal(k, pr):
    R = 8.3145
    r = (1 / 8.3145)
    p = str(input("Input pressure - "))
    if p != "x":
        p = float(p) * pr
    v = str(input("Input volume - "))
    if v != "x":
        v = float(v)
    t = str(input("Input temperature - "))
    if t != "x":
        t = float(t) + k
    n = str(input("Input mols - "))
    if n != "x":
        n = float(n)
    def get(w, x, y, z):
        ans = (w * (x * y) / z)
        print("The answer is " + str(ans))
    if p == "x":
        get(R, n, t, v)
    elif v == "x":
        get(R, n, t, p)
    elif t == "x":
        get(r, p, v, n)
    elif n == "x":
        get(r, p, v, t)
    srt()
def srt():
    ans = input("atm or kpa (at/kp) - ")
    ans2 = input("celcius or kelvin (c/k) - ")
    if ans2 == "c":
        if ans == "kp":
            cal(273.15, 1)
        if ans == "at":
            cal(273.15, 101.325)
    if ans2 == "k":
        if ans == "kp":
            cal(0, 1)
        if ans == "at":
            cal(0, 101.325)
srt()
