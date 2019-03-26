oNumaraArray = ["0","1","2","3","4","5","6","7","8","9"];
oCevapArray  = ["A","B","C","D","E"," "];

def oNumaraGenerator(nArray):
    import random;
    ogrenciNumara = "";
    for i in range(11):
        randomSayi = random.choice(nArray);
        ogrenciNumara += randomSayi;
    return ogrenciNumara;

def oCevapGenerator(cArray):
    import random;
    ogrenciCevap = "";
    for i in range(30):
        randomCevap = random.choice(cArray);
        ogrenciCevap += randomCevap;
    return ogrenciCevap;

tWriter = open("ogrenciCevap.txt","w");

for i in range(100):
    newLine = oNumaraGenerator(oNumaraArray) + oCevapGenerator(oCevapArray) + "\n";
    print (newLine);
    tWriter.write(newLine);
tWriter.close();