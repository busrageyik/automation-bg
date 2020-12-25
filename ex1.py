def bolunceksayi(min_sayi, max_sayi, bolunecek_sayi):
    numberList = []
    for numbers in range(min_sayi, max_sayi + 1):
        if(numbers % bolunecek_sayi == 0):
            numberList.append(numbers)

    return numberList

print(bolunceksayi(10, 40, 5))