**1.) Buat flowchart untuk menentukan bilangan terbesar dari 3 buah bilangan yang
diinputkan**
Jawaban

1. Definisi Fungsi:
```def cari_terbesar_dari_tiga():```
- Program dimulai dengan mendefinisikan sebuah fungsi bernama `cari_terbesar_dari_tiga`
- Fungsi ini tidak memiliki parameter

2. Input Pengguna:
```
a = float(input("Masukkan bilangan pertama: "))
b = float(input("Masukkan bilangan kedua: "))
c = float(input("Masukkan bilangan ketiga: "))
```
- Program meminta pengguna memasukkan tiga bilangan
- `float()` digunakan untuk mengkonversi input (yang awalnya string) menjadi bilangan desimal
- Bilangan-bilangan tersebut disimpan dalam variabel a, b, dan c

3. Logika Perbandingan:
```
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
```
- Program menggunakan struktur if-else bersarang untuk membandingkan ketiga bilangan
- Pertama, membandingkan a dengan b
- Jika a lebih besar dari b:
  - Kemudian membandingkan a dengan c
  - Jika a lebih besar dari c, maka a adalah terbesar
  - Jika tidak, maka c adalah terbesar
- Jika b lebih besar dari a:
  - Kemudian membandingkan b dengan c
  - Jika b lebih besar dari c, maka b adalah terbesar
  - Jika tidak, maka c adalah terbesar

4. Output:
```
print(f"Bilangan terbesar adalah: {terbesar}")
```
- Program mencetak bilangan terbesar yang ditemukan
- Menggunakan f-string untuk memformat output

5. Pemanggilan Fungsi:
```
cari_terbesar_dari_tiga()
```
- Program diakhiri dengan memanggil fungsi yang telah didefinisikan

**2.) Buat flowchart untuk menentukan bilangan terbesar dari N bilangan yang diinputkan, untuk menentukan jumlah N, berikan masukan angka 0**
Jawaban

1. Definisi Fungsi:
```def cari_terbesar_dari_n():```
- Program dimulai dengan mendefinisikan fungsi bernama `cari_terbesar_dari_n`
- Fungsi ini akan mencari nilai terbesar dari N bilangan yang dimasukkan pengguna

2. Inisialisasi Variabel:
```
terbesar = float('-inf')
```
- Membuat variabel `terbesar` dengan nilai awal negatif tak hingga (`-inf`)
- Ini memastikan bahwa bilangan pertama yang dimasukkan akan selalu lebih besar dari nilai awal

3. Input Jumlah Bilangan:
```
n = int(input("Masukkan jumlah bilangan (N) atau 0 untuk mengakhiri: "))
```
- Meminta pengguna memasukkan berapa banyak bilangan yang akan dibandingkan
- Input dikonversi ke integer menggunakan `int()`

4. Pengecekan Input Awal:
```
if n == 0:
    print("Tidak ada bilangan yang dimasukkan.")
    return
```
- Jika pengguna memasukkan 0, program akan menampilkan pesan dan mengakhiri fungsi
- `return` digunakan untuk keluar dari fungsi

5. Perulangan dan Perbandingan:
```
for i in range(n):
    bilangan = float(input(f"Masukkan bilangan ke-{i+1}: "))
    if bilangan > terbesar:
        terbesar = bilangan
```
- Menggunakan loop `for` untuk meminta input sebanyak N kali
- Setiap input dikonversi ke float dan dibandingkan dengan nilai terbesar saat ini
- Jika bilangan yang baru dimasukkan lebih besar, nilai `terbesar` diperbarui

6. Output Hasil:
```print(f"Bilangan terbesar adalah: {terbesar}")```
- Setelah semua bilangan dimasukkan, program mencetak bilangan terbesar yang ditemukan

7. Pemanggilan Fungsi:
```cari_terbesar_dari_n()```
- Program diakhiri dengan memanggil fungsi yang telah didefinisikan
