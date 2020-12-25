birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]
gecerli = False

def sayiAtama():
  return int(input("Sayi:"))

def sayiOkunus(sayi):
    if (sayi>=10 and sayi<100):
        birinci = sayi % 10
        ikinci = sayi // 10

        print(onlar[ikinci] + " " + birler[birinci])
        return True
    return False

while (not gecerli):
    gecerli = sayiOkunus(sayiAtama())






