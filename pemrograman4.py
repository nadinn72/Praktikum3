def cari_terbesar_dari_n():
    terbesar = float('-inf')
    n = int(input("Masukkan jumlah bilangan (N) atau 0 untuk mengakhiri: "))

    if n == 0:
        print("Tidak ada bilangan yang dimasukkan.")
        return

    for i in range(n):
        bilangan = float(input(f"Masukkan bilangan ke-{i+1}: "))
        if bilangan > terbesar:
            terbesar = bilangan

    print(f"Bilangan terbesar adalah: {terbesar}")

cari_terbesar_dari_n()
