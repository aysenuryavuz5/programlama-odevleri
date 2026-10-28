
print("ASCII TABLOSU (0-255)")
print("----------------------")

for sayi in range(256):
    if sayi < 32 or sayi == 127:
        karakter = "Kontrol karakteri"
    else:
        karakter = chr(sayi)

    print(sayi, ":", karakter)