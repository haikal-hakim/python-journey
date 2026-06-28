# --- OPERASI DASAR ---
print(2 + 2)  # 4 penjumlahan
print(50 - 5 * 6)  # 20  pengurangan & perkalian
print(8 / 5)  # 1.6 pembagian selalu menghasilkan float

# --- PEMBAGIAN BULAT & SISA BAGI ---
print(17 / 3)  # 5.666  pembagian biasa
print(17 // 3)  # 5 pembagian bulat (membuang bagian desimal)
print(17 % 3)  # 2 sisa bagi
print(5 * 3 + 2)  # 17 hasil bagi * pembagi + sisa = angka asal

# --- PERPANGKATAN ---
print(5**2)  # 25   5 pangkat 2
print(2**7)  # 128  2 pangkat 7

# --- VARIABEL ---
width = 20
height = 5 * 9
print(width * height)  # 900

# --- TIPE CAMPURAN ---
# integer + float = float, Python otomatis mengubah int ke float
print(4 * 3.75 - 1)  # 14.0

# --- KONVERSI TIPE DATA ---
print(int(3.9))  # 3 float ke int (dipotong, bukan dibulatkan)
print(float(10))  # 10.0  int ke float
print(str(42))  # '42' int ke string
# int(), float(), str() adalah fungsi bawaan untuk mengubah tipe data

# --- BILANGAN KOMPLEKS ---
c = 3 + 5j
print(c)  # (3+5j)
print(type(c))  # <class 'complex'>
# type() adalah fungsi bawaan Python untuk mengecek tipe data dari sebuah variabel
