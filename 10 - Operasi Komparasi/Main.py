# operasi komparasi

# setiap hasil dari komparasi adalah boolean

# operator komparasi >, <, >=, <=, ==, !=, is, is not

a = 5
b = 3

# lebih besar dari >
hasil = a > b
print(a,">",b,"=",hasil)

# kurang dari <
hasil = a < b
print(a,"<",b,"=",hasil)

# lebih besar atau sama dengan >=
hasil = a >= b
print(a,">=",b,"=",hasil)

# kurang dari atau sama dengan <=
hasil = a <= b
print(a,"<=",b,"=",hasil)

# sama dengan ==
hasil = a == b
print(a,"==",b,"=",hasil)

# tidak sama dengan !=
hasil = a != b
print(a,"!=",b,"=",hasil)

# is dan is not saat tidak bisa dipakai dalam syntax literal
# is dan not hanya bisa digunakan untuk komparasi object identity

x = 5 # ini adalah assignment membuat object x
y = 5 
z = 10

# mari kita lihat id address masing masing object x dan y

print(hex(id(x)))
print(hex(id(y)))

# jika literalnya sama maka adressnya sama
# jadi kita bisa menggunakan literal yang sama pada object yang berbeda

hasil = x is int(float(5))
print("hasil x = y =", hasil)

hasil = x is not z 
print("hasil x = z =", hasil)