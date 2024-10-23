def cari_terbesar_dari_tiga():
    a = float(input("Masukkan bilangan pertama: "))
    b = float(input("Masukkan bilangan kedua: "))
    c = float(input("Masukkan bilangan ketiga: "))

    if a > b:
        if a > c:
            terbesar = a
        else:
            terbesar = c
    else:
        if b > c:
            terbesar = b
        else:
            terbesar = c

    print(f"Bilangan terbesar adalah: {terbesar}")

cari_terbesar_dari_tiga()