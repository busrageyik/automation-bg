vize1=float(input("Vize 1 notunuzu giriniz: "))
vize2=float(input("Vize 2 notunuz giriniz: "))
final=float(input("Final notunuzu giriniz:"))

toplamNot=(0.30*vize1)+(0.30*vize2)+(0.40*final)

print("Not ortalamanız : ",toplamNot)


if toplamNot<=100:
    if toplamNot>=90:
        print("Harf Notunuz: AA")
    elif toplamNot>=85 and toplamNot<90:
        print("Harf Notunuz: BA")
    elif toplamNot >= 80 and toplamNot< 85:
        print("Harf Notunuz: BB")
    elif toplamNot >= 75 and toplamNot < 80:
        print("Harf Notunuz: CB")
    elif toplamNot >= 70 and toplamNot < 75:
        print("Harf Notunuz: CC")
    elif toplamNot >= 65 and toplamNot < 70:
        print("Harf Notunuz: DC")
    elif toplamNot >= 60 and toplamNot < 65:
        print("Harf Notunuz: DD")
    elif toplamNot >=55 and toplamNot<60:
        print("Harf notunuz: FD")
else:
        print("Harf notunuz: FF")