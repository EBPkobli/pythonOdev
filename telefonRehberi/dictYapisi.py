Names = ["Furkan","Ibrahim","Selma","Halit","Enis","Hakan","Fatma","Hilmi","Cengiz","Buse","Banu"];
Surnames = ["Kubilay","Aydın","Işık","Avcı","Uzun","Ocakbaşı","Kısa","Ketenci","Varan"];
my_Dict = {};
import random;

for i in range(100):
    newDude  = random.choice(Names) + " " + random.choice(Surnames);
    newPhone = "0 5" + str(random.randint(0,9)) + str(random.randint(0,9)) +" " + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + " " + str(random.randint(0,9)) + str(random.randint(0,9)) + " " + str(random.randint(0,9)) + str(random.randint(0,9));
    my_Dict[newDude] =  newPhone

while True:
    print("1- Tüm telefonları göster");
    print("2- Yeni telefon ekle");
    print("3- Olan telefonu değiştir");
    print("4- Olan telefonu sil")
    print("5- Tüm telefonları sil");
    print("6- Çıkış yap");

    x = raw_input();
    if(x == "1"):
        for key,value in my_Dict.items():
            print (key +"\t\t\t => \t\t\t"+value);
    elif(x == "2"):
        print("Yeni kişi oluştur : ");
        newDude = raw_input();
        print("Yeni telefon oluştur :");
        newPhone = raw_input();
        my_Dict[newDude] = newPhone;
    elif(x == "3"):
        print("Değiştirilecek telefonun sahibinin adı : ");
        key = raw_input();
        if key in my_Dict:
            print("Yeni telefon : ");
            newPhone = raw_input();
            my_Dict[key] = newPhone;
        else:
            print("Kişi bulunamadı.");
    elif(x == "4"):
        print("Silinecek kişi : ");
        myDude = raw_input();
        if(myDude in my_Dict):
            del my_Dict[key];
        else:
            print("Kişi bulunamadı.");
    elif(x == "5"):
        print("Silmekten emin misin? e/h");
        x = raw_input();
        if(x == "e"):
            my_Dict.clear();
            print("Tüm rehber silindi");
        else:
            print("İşlem iptal edildi");
    elif(x == "6"):
        break;