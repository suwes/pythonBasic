# operasi logika atau boolean

# operator logika ada NOT, OR, AND, XOR

# NOT (kebalikan)
a = True
b = not a
print("===== NOT =====")
print("a =",a)
print("------- NOT")
print("b =",b)

# OR (ditambahkan, jika salah satu true maka hasil akan true)
a = False
b = False
c = a or b
print("\n===== OR =====")
print(a,"or",b,"=",c)
a = False
b = True
c = a or b
print(a,"or",b,"=",c)
a = True
b = False
c = a or b
print(a,"or",b,"=",c)
a = True
b = True
c = a or b
print(a,"or",b,"=",c)


# AND (dikalikan, jika dua duanya true maka hasil akan true)
a = False
b = False
c = a and b
print("\n===== AND =====")
print(a,"and",b,"=",c)
a = False
b = True
c = a and b
print(a,"and",b,"=",c)
a = True
b = False
c = a and b
print(a,"and",b,"=",c)
a = True
b = True
c = a and b
print(a,"and",b,"=",c)

# XOR (jika salah satu true maka hasilnya true, sisanya false)
a = False
b = False
c = a ^ b
print("\n===== XOR =====")
print(a,"xor",b,"=",c)
a = False
b = True
c = a ^ b
print(a,"xor",b,"=",c)
a = True
b = False
c = a ^ b
print(a,"xor",b,"=",c)
a = True
b = True
c = a ^ b
print(a,"xor",b,"=",c)

