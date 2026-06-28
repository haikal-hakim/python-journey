# --- TANDA KUTIP TUNGGAL DAN GANDA ---
print('Test')  # tanda kutip tunggal
print("Test")  # tanda kutip ganda
print('1993')  # ini string bukan angka karena diapit tanda kutip
print(type('1993'))  # <class 'str'>
# Hasilnya sama, gunakan salah satu secara konsisten

# --- KARAKTER ESCAPE ---
print('doesn\'t')  # gunakan \' untuk escape tanda kutip tunggal
print("doesn't")  # atau gunakan tanda kutip ganda

print("\"Yes,\" he said.")  # \" untuk escape tanda kutip ganda
print('"Isn\'t," she said.')  # \' untuk escape tanda kutip tunggal

# --- KARAKTER KHUSUS ---
s = "Hello\nWorld"  # \n adalah baris baru
print(s)  # menghasilkan dua baris output menggunakan print()

# --- RAW STRING ---
print("C:\tnew\nfolder")  # \t adalah tab
print(r"C:\new\folder")
# r adalah raw, artinya Python membaca string apa adanya

# --- STRING MULTI-BARIS ---
# string bisa mencakup beberapa baris, menggunakan tanda kutip tiga
# serta menambahkan \ setelah tanda kutip
print("""\
      Usage: script [OPTIONS]
      -h                        Display this usage message
      -R                        Show the README and exit
      """)

# --- PENGGABUNGAN & PENGULANGAN ---
print(7 * "bla" + "hh")  # blablablablablahh
# '+' menggabungkan, '*' pengulangan

# --- PENGGABUNGAN & KELANJUTAN ---
print("Herukopter")
print("Heru" "kopter")

x = ("Tulis kata-kata dalam kurung, "
     "agar Python tahu bahwa teks ini dilanjutkan.")
print(x)
# penggunaan literal concatenation untuk memecah string panjang agar lebih mudah dibaca pada kode

# '+' untuk menggabungkan variabel
x = "Heru"
print(x + "kopter")  # Herukopter

# --- INDEKS ---
word = "Python"
# karakter pertama memiliki indeks 0
print(word[0])  # P
print(word[5])  # n
# indeks negatif dihitung dari akhir (kanan ke kiri)
print(word[-1])  # n
print(word[-2])  # o

# --- PEMOTONGAN ---
word = "Alice"
# word[start:stop] kapan mulai dan kapan berhenti
print(word[0:2])  # Al dari posisi 0 (uncluded) ke 2 (excluded)
print(word[1:9])  # lice Python menangani slice di luar jangkauan

print(word[:2])  # Al dari awal ke posisi 2
print(word[1:5])  # lice dari posisi 1 ke 5
print(word[-3:5])  # ce dari kedua-terakhir ke akhir

print("B" + word[1:])  # Blice mengubah karakter pertama string
print(word[:2] + "Z")  # AlZ mengubah karakter terakhir string
# +---+---+---+---+---+
# | A | l | i | c | e |
# +---+---+---+---+---+
#   0   1   2   3   4
#  -5  -4  -3  -2  -1

# --- LEN() ---
# Fungsi bawaan len() untuk mengetahui banyaknya karakter dalam sebuah string
x = "abcdefghijklmnopqrstuvwxyzaaaaaaaaa"
print(len(x))  # 35