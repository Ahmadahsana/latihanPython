# import time

# helo = 'mari kita makan'
# type(helo)
# print(helo)
# for i in range(5):
# print(helo)

#     time.sleep(2)

# nama = "Hartono"
# alamat = 'Mataram'
# umur = 19
# tinggi = 170.5
# menikah = True
# # mencetak isi variabel

# print('', nama)
# print("Alamat : ", alamat)
# print("Umur : ", umur)
# print("Tinggi : ", tinggi)
# if(menikah):
#     print("Status: menikah")
# else:
#     print("Status: belum menikah")

# jawab = 'ya'
# hitung = 0

# while():
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")
#     if jawab == 'tidak':
#         break

# print(f"Total perulagan: {hitung}")


# isiDompet = ["uang", "ktp", "SIM", "ATM"]

# isiDompet.append("kunci")
# print(isiDompet)
# isiDompet.remove("ktp")
# print(isiDompet)
# print(isiDompet[2])

# atasMeja = ['hp', 'buku', 'gelas', 'aqua', 'monitor']
# for isi in atasMeja:
#     print(f'di atas meja ada {isi}')

# a = input('masukkan benda :')
# isi = []

# while(True):
#     a = input('masukkan benda :')
#     isi.append(a)
#     jawab = input('tambah lagi? (ya/tidak)')
#     if jawab == 'tidak':
#         break

# print(f'yang kamu inginkan adalah : {isi}')


banyak = int(input('ada berapa banyak data? '))
dataNama = []
dataUsia = []

for i in range(0, banyak):
    print(f'data ke {i+1}')
    inputNama = input('nama : ')
    inputUsia = input('umur: ')

    dataNama.append(inputNama)
    dataUsia.append(inputUsia)

for i in range(0, len(dataNama)):
    nama = dataNama[i]
    usia = dataUsia[i]
    print(f'{nama} usianya {usia}')


print('baca ini')
