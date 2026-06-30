# --- LIST ---
# membuat dan menampilkan list
x = ["apple", "banana", "mango"]
print(x)
y = [1, 4, 9, 12, 40]
print(y)

# --- INDEXING ---
print(x[2])  # mango
print(x[-2])  # banana
print(y[2])  # 9
print(y[-2])  # 12

# --- SLICING ---
print(x[1:3])  # ['banana', 'mango']
print(x[:2])  # ['apple', 'banana']
print(y[-3:])  # [9, 12, 40]

# --- CONCATENATION & REPEATING ---
# operator '+' menggabungkan list, '*' mengulang list
print(x + y)  # ['apple', 'banana', 'mango', 1, 4, 9, 12, 40]
print(x * 2)  # ['apple', 'banana', 'mango', 'apple', 'banana', 'mango']
print(y + [41, 42])  # [1, 4, 9, 12, 40, 41, 42]
print(x[2] + str(y[2]))  # mango9

# --- MUTABLE ---
# list bersifat mutable, artinya bisa diubah
b = [1, 4, 9, 17, 25]  # 17 itu salah harusnya 16, kita akan ubah
print(4**2)  # 16 hasilnya benar, ubah list b
b[3] = 16  # ubah elemen ke-4 (indeks 3) menjadi 16
print(b)  # [1, 4, 9, 16, 25]
print(len(b))  # panjang list b 5

# --- APPENDING ---
# menambahkan item ke akhir list menggunakan append()
b.append(36)  # menambahkan 36 ke akhir list b
print(b)  # [1, 4, 9, 16, 25, 36]
print(len(b))  # panjang list b 6

# --- ASSIGNMENT ---
# dua variabel bisa menunjuk ke list yang sama,
# sehingga perubahan pada salah satu akan memengaruhi yang lain
rtf = ["read", "the", "f*cking"]
rtfm = rtf
id(rtf) == id(rtfm)  # True, keduanya menunjuk ke list yang sama
rtfm.append("manuaaal")  # menambahkan "manuaaal" ke list rtfm
print(rtfm)  # ['read', 'the', 'f*cking', 'manuaaal']
print(rtf)  # ['read', 'the', 'f*cking', 'manuaaal']

# --- COPY ---
# untuk membuat salinan list, gunakan slicing [:]
correct_rtfm = rtfm[:]
correct_rtfm[-1] = "manual"
print(correct_rtfm)  # ['read', 'the', 'f*cking', 'manual']
print(rtfm)  # ['read', 'the', 'f*cking', 'manuaaal']


# --- SLICE ASSIGNMENT ---
# mengubah
alphabet = ["a", "b", "c", "d", "e", "f", "g"]
print(alphabet)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
alphabet[5:7] = ["F", "G"]  # ubah elemen ke-6 dan ke-7 menjadi F dan G
print(alphabet)  # ['a', 'b', 'c', 'd', 'e', 'F', 'G']

# menghapus
alphabet[1:7] = []
print(alphabet)  # ['a']

# mengosongkan seluruh list
alphabet[:] = []
print(alphabet)  # []
print(len(alphabet))  # panjang list alphabet 0

# --- NESTED LIST ---
# list bisa berisi list lain
lattidude = [123.497, 23.456]
longtitude = [34.567, 45.678]
planet = ["Earth", "Mars"]
location = [lattidude, longtitude, planet]
print(location)  # [[123.497, 23.456], [34.567, 45.678], ['Earth', 'Mars']]
print(len(location))  # panjang list location 3

print(location[0][1])  # 23.456
print(location[1][0])  # 34.567
print(location[2][1])  # Mars
# atau
print(location[0][1], location[1][0], location[2][1])
