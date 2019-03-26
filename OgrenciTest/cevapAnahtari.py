hDizi = ["A","B","C","D","E"];
def cAnahtari(p0):
    import random;
    rDizi = [];
    for i in range(30):
        rDizi.append(random.choice(p0));
    return rDizi;

t0 = open("Cevap.txt","w");
t0.write("".join(cAnahtari(hDizi)));
t0.close();

