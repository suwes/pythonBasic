# latihan komparasi dan logika

# membuat gabungan dari rentang area angka

# + = true, - = false


# soal

# +++++4-------10++++++

userInput = int(input("Msukan angka kurang dari 4 \natau\nlebih dari 10 : "))
print("angka yang kamu masukan : ",userInput)


# memeriksa angka kurang dari 4
hasilA = (userInput < 4)
print("kurang dari 4 =",hasilA)

# memeriksa angka lebih dari 10
hasilB = userInput > 10
print("lebih dari 10 =",hasilB)


# kita akan menggunakan OR untuk logikanya
hasilC = hasilA or hasilB
print("angka yang dimasukan nilainya :",hasilC)


# mencari angka pada kasus irisan
# ------4++++++++10--------

userInput = int(input("Msukan angka lebih dari 4 \ndan\nkurang dari 10 : "))
print("angka yang kamu masukan : ",userInput)


# memeriksa angka lebih dari 4
hasilA = (userInput > 4)
print("lebih dari 4 =",hasilA)

# memeriksa angka kurang dari 10
hasilB = userInput < 10
print("kurang dari 10 =",hasilB)


# kita akan menggunakan AND untuk logikanya
# jika salah satu false hasil akan false
hasilC = hasilA and hasilB
print("angka yang dimasukan nilainya :",hasilC)