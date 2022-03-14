# operasi dan manipulasi string dengan method

## mengubah case pada string

# mengubah case ke besar
salam = "hallo"
print("normal = ", salam)

salam = salam.upper()
print("menjadi = ",salam)

salam = "Apa KabaRRR nYa"
print("normal = ", salam)

salam = salam.lower()
print("menjadi = ",salam)


## melakukan pengecekan case menggunakan isX

salam = "selamat77"
apakah_lower = salam.islower() # mengecek apakah lower case
print(salam,"is lower = ",str(apakah_lower)) 

apakah_upper = salam.isupper() # mengecek apakah upper case
print(salam,"is upper = ",str(apakah_upper))

apakah_alpha = salam.isalpha() # mengecek apakah semuanya huruf
print(salam,"is alpha =",str(apakah_alpha))

apakah_alnum = salam.isalnum() # mengecek apakah huruf dan angka
print(salam,"is alnum = ",str(apakah_alnum))

apakah_decimal = salam.isdecimal() # mengecek apakah angka saja
print(salam,"is decimal =",str(apakah_decimal))

apakah_space = salam.isspace() # spasi, tab, newline \n
print(salam,"is space =",str(apakah_space))

tittle = "Halo Semua Mari Makan Yuk"
apakah_tittle = tittle.istitle() # semua kata dimulai dengan huruf besar
print(tittle,"is tittle =",str(apakah_tittle))

