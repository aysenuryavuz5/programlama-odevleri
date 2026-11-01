
print("ASCII KARAKTER TABLOSU (0-127)")
print("---------------------------------------")
print("ASCII KODU | KARAKTER")
print("---------------------------------------")

for sayi in range(128):
    if sayi < 32 or sayi == 127:
        karakter = "Kontrol karakteri"
    elif sayi == 32:
        karakter = "[boşluk]"
    else:
        karakter = chr(sayi)

    print(f"{sayi:<10} | {karakter}")
