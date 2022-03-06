# operasi aritmatika

a = 10
b = 3

# pertambahan
hasil_tambah = a + b
print(a,"+",b,"=",hasil_tambah)

# pengurangan
hasil_kurang = a - b
print(a,"-",b,"=",hasil_kurang)

# perkalian
hasil_perkalian = a * b
print(a,"*",b,"=",hasil_perkalian)

# pembagian
hasil_pembagian = a / b
print(a,"/",b,"=",hasil_pembagian)

# modulus (hasil bagi)
hasil_modulus = a % b
print(a,"%",b,"=",hasil_modulus)

# floor division (kebalikan modulus / dapat di bagi menjadi)
hasil_fd = a // b
print(a,"//",b,"=",hasil_fd)

# exponen (panggkat)
hasil_pangkat = a ** b
print(a,"**",b,"=",hasil_pangkat)


# prioritas oprasi / oprational precedence

''' prioritas oprasi
    1. ( ) buka tutup kurung/pengelokmpokan
    2. exponen (**) 
    3. perkalian dan teman teman (* / // % +)
'''
x = 5
y = 4
z = 3

hasil = x ** y + z - x / y % z // x * y
print(x,"**",y,"+",z,"-",x,"/",y,"%",z,"//",x,"*",y,"=",hasil)

hasil = x + y * z
print(x,"+",y,"*",z,"=",hasil)

hasil = (x + y) * z # hasil akan berbeda jika kita mengelompokan
# x dan y akan di jumlahkan di awal
print("(",x,"+",y,")","*",z,"=",hasil)