t0 = open("Sonuc.txt","w");
t0.write("\tÖğrenci \t\t\t\t\t\t  Cevap \t\t\t\t\t\t   Net \n");
t0.write("\t-------- \t\t\t\t\t\t ------- \t\t\t\t\t\t -------");

t1 = open("ogrenciCevap.txt","r");
t2 = open("Cevap.txt","r");

t0.write("\n");

for i in range(100):
    oNumara = t1.read(11)
    oCevap = t1.read(30);
    cevap = t2.read(30);



    dY ="";
    net = 0;
    d=0;
    y=0;
    for j in range(30):
        if(oCevap[j] == cevap[j]):
            d +=1;
            dY += "D";
        elif (oCevap[j] == " "):
            dY += " ";
        else:
            y+=1;
            dY += "Y";
    
    net = d - (y/4);
    
    t0.write("            \t\t\t"+oCevap+"\n");
    t0.write(" "+oNumara);
    t0.write("\t\t\t"+cevap);
    t0.write("\t\t\t\t"+str(net));
    t0.write("\n            \t\t\t"+dY+"\n");
    t1.read(1);
    t2.seek(0);
    t0.write("\n");

#x = (30+11);
#k = 1;

#for i in range (100):
#    print(oCevap[x*i:(x*i+11+k*i)]);
#    print(oCevap[(x*i+11+k*i):(x*(i+1))]);


t0.close();