print("ASCII KARAKTER TABLOSU")
print("ASCII KODU | KARAKTER")
print("----------------------")

for i in range(128):
    if i <= 31 or i == 127:
        karakter = "Kontrol karakteri"
    elif i == 32:
        karakter = "[boşluk]"
    else:
        karakter = chr(i)

    print(i, "|", karakter)
