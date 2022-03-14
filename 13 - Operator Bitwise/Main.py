# operator bitwise, biner, binary
# operasi pada masing masing bit
# berfungsi untuk melakukan proses logika

a = 9
b = 5

# bitwise OR ( | )
c = a | b # operator bitwise
print("\n====== OR ======")
print("nilai = ",a," biner = ",format(a,"08b")) # format untuk melihat biner
print("nilai = ",b," biner = ",format(b,"08b"))
print("-------------------------------- ( | )")
print("nilai = ",c," biner = ",format(c,"08b"))

# bitwise AND ( & )
c = a & b # operator bitwise
print("\n====== OR ======")
print("nilai = ",a," biner = ",format(a,"08b")) # format untuk melihat biner
print("nilai = ",b," biner = ",format(b,"08b"))
print("-------------------------------- ( & )")
print("nilai = ",c," biner = ",format(c,"08b"))

# bitwise XOR ( ^ )
c = a ^ b # operator bitwise
print("\n====== OR ======")
print("nilai = ",a," biner = ",format(a,"08b")) # format untuk melihat biner
print("nilai = ",b," biner = ",format(b,"08b"))
print("-------------------------------- ( ^ )")
print("nilai = ",c," biner = ",format(c,"08b"))

# bitwise NOT ( ~ )
# hati hati sata menggnakan not dalam bitwise
c = ~a # operator bitwise
print("\n====== OR ======")
print("nilai = ",a," biner = ",format(a,"08b")) # format untuk melihat biner
print("-------------------------------- ( ~ )")
print("nilai = ",c," biner = ",format(c,"08b")) # hasil akan minus jika nilai positif

# lalu bagaiman jika kita ingin mengbalikan nilai atau nge flip
# dengan menggunakan xor dan membuat variabel biner = 11111111 untuk
# meng xor kan nilai biner yang ingin di flip
d = 0b00001001 # isinya sama aja dengan 9
e = 0b11111111
f = d ^ e
print("-------------------------------- ( ^ )")
print("nilai = ",f," biner = ",format(f,"08b")) # maka nilai akan di flip



# shifting bitwise

# shift right ( >> )
c = a >> 2 # menggeser anggka biner ke kanan 2 kali
print("\n====== >> ======")
print("nilai = ",a," biner = ",format(a,"08b")) # format untuk melihat biner
print("-------------------------------- ( >> )")
print("nilai = ",c," biner = ",format(c,"08b"))  # angka biner akan menggeser

# shift left ( << )
c = a << 2 # menggeser anggka biner ke kiri 2 kali
print("\n====== << ======")
print("nilai = ",a," biner = ",format(a,"08b")) # format untuk melihat biner
print("-------------------------------- ( << )")
print("nilai = ",c," biner = ",format(c,"08b"))  # angka biner akan menggeser
