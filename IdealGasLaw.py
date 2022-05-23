print("Enter variables and x as the missing variable.\nfor unused variables input 1\nif temperature is in c and the variable is unused input t\n")
def cal(k):
    global p1, v1, t1, n1, p2, v2, t2, n2, ans
    p1 = str(input("p1\n"))
    if p1 != "x":
        p1 = float(p1)
    v1 = str(input("v1\n"))
    if v1 != "x":
        v1 = float(v1)
    t1 = str(input("t1\n"))
    if t1 != "x" or "t":
        if t1 != "t":
            t1 = float(t1) + k
        if t1 == "t":
            t1 = 1
    n1 = str(input("n1\n"))
    if n1 != "x":
        n1 = float(n1)
    p2 = str(input("p2\n"))
    if p2 != "x":
        p2 = float(p2)
    v2 = str(input("v2\n"))
    if v2 != "x":
        v2 = float(v2)
    t2 = str(input("t2\n"))
    if t2 != "x" or "t":
        if t2 != "t":
            t2 = float(t2) + k
        if t2 == "t":
            t2 = 1
    n2 = str(input("n2\n"))
    if n2 != "x":
        n2 = float(n2)

    def ovr(p, v, t, n, tt, nn, las):
        ans = ((((p * v) / (t * n)) * (tt * nn)) / las)
        print("The answer is " + str(ans))

    def und(t, n, p, v, pp, vv, las):
        ans = ((((t * n) / (p * v)) * (pp * vv)) / las)
        print("The answer is " + str(ans))

    if p1 == "x":
        ovr(p2, v2, t2, n2, t1, n1, v1)
    elif v1 == "x":
        ovr(p2, v2, t2, n2, t1, n1, p1)
    elif t1 == "x":
        und(t2, n2, p2, v2, p1, v1, n1)
    elif n1 == "x":
        und(t2, n2, p2, v2, p1, v1, t1)
    elif p2 == "x":
        ovr(p1, v1, t1, n1, t2, n2, v2)
    elif v2 == "x":
        ovr(p1, v1, t1, n1, t2, n2, p2)
    elif t2 == "x":
        und(t1, n1, p1, v1, p2, v2, n2)
    elif n2 == "x":
        und(t1, n1, p1, v1, p2, v2, t2)
    srt()


def srt():
    kc = input("k or c\n")
    if kc == "k":
        cal(0)
    if kc == "c":
        cal(273)


srt()
