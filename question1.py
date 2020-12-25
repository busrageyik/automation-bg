class Insan:
    def __init__(self, ad, soyad, yas, ulke, sehir):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.ulke=ulke
        self.sehir=sehir
        self.yetenekler= []

    def kisi_bilgileri(self):
        print("Kisi bilgileri: "+ self.ad+ self.soyad+ self.yas+ self.ulke+ self.sehir)

    def yetenek_ekle(self):
        yetenek=input("yetenek: ")
        self.yetenekler.append(yetenek)
        print(self.yetenekler)

i1=Insan("Büşra"," Geyik"," 24"," Turkiye"," Istanbul")
i1.kisi_bilgileri()
i1.yetenek_ekle()







