# Baslık ve Sutun Adları
print("ASCII KODU | KARAKTER")
print("-----------|-------------------")

# 0 ile 127 arasındaki (dahil) tüm kodları dönen döngü
for i in range(128):
    # 0-31 ve 127 arası kontrol karakterleridir
    if (0 <= i <= 31) or i == 127:
        karakter = "Kontrol karakteri"
    # 32 kodu bosluk karakteridir
    elif i == 32:
        karakter = "[bosluk]"
    # Geri kalan yazdırılabilir karakterler
    else:
        karakter = chr(i)
    
    # Tablonun duzgun gorunmesi icin ASCII kodunu sol tarafa hizalıyoruz
    print(f"{str(i).ljust(10)} | {karakter}")

