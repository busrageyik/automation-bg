class Ogrenci:
    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinifi):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinifi = ogrenciSinifi

    def ogrenci_bilgileri(self):
        print("Kisi bilgileri: " + self.ogrenciAdi + self.ogrenciSoyadi + self.ogrenciSinifi)
class Soru():

      def NetSayisi(self):
        gecerli = False
        while (not gecerli):

            self.dogru = int(input("Dogru: "))
            self.yanlis = int(input("Yanlis: "))

            if (self.yanlis + self.dogru) <= 50:
                gecerli = True
                print("Dogru: " + str(self.dogru), "Yanlis: " + str(self.yanlis), "Bos: " + str(50-(self.dogru + self.yanlis)))
            else:
                print("Lutfen gecerli not giriniz!")


      def Hesapla(self):

            self.dogru = self.dogru - int(self.yanlis / 4)

            print("Toplam puaniniz: " + str(self.dogru * 2))


i1=Ogrenci("Büşra"," Geyik "," 3")
i1.ogrenci_bilgileri()

i2=Soru()
i2.NetSayisi()
i2.Hesapla()






