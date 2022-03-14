# operator assignmnet biasanya digunakan untuk melakukan penyingkatan
# contoh : a = 10 <- assignment
# a = a + 1, dengan mengunakan operator assignment : a += 1.


# OPERATOR ASSIGNMENT ARITMATIKA
# +=, -=, *=, /=, 

a = 5

print("\nnilai a : ",a)
a += 1 # artinya a = a + 1
print("nilai a += 1 : ",a)

print("\nnilai a : ",a)
a -= 2 # artinya a = a - 2
print("nilai a -= 2 : ",a)

print("\nnilai a : ",a)
a *= 5 # artinya a = a * 10
print("nilai a *= 5 : ",a)

print("\nnilai a : ",a)
a /= 3 # artinya a = a / 1
print("nilai a /= 3 : ",a)

# modulus dan floor division

b = 10
print("\nnilai b : ",b)
b %= 3 # artinya b = b % 3
print("nilai b %= 3 : ",b)

b = 10
print("\nnilai b : ",b)
b //= 5 # artinya b = b // 3
print("nilai b //= 3 : ",b)

# eksponen

b = 5
print("\nnilai b : ",b)
b **= 3 # artinya b = b ** 3
print("nilai b **= 3 : ",b)



# OPERATOR ASSIGNMENT BITWISE

# logika 
# or (|=), and (&=), xor (^=)

# OR
a = True
print("\nnilai a = ",a)
a |= False
print("nilai a |= False : ",a)

a = False
print("nilai a = ",a)
a |= False
print("nilai a |= False : ",a)

# AND
a = True
print("\nnilai a = ",a)
a &= False
print("nilai a &= False : ",a)

a = True
print("nilai a = ",a)
a &= True
print("nilai a &= False : ",a)

# XOR
a = True
print("\nnilai a = ",a)
a ^= False
print("nilai a ^= False : ",a)

a = True
print("nilai a = ",a)
a ^= True
print("nilai a ^= False : ",a)

# shifting
# shiftright (>>), shiftleft (<<)
a = 0b0100
print("\nnilai a :",a," bit :",format(a,"04b"))
a >>= 2
print("nilai a :",a," bit :",format(a,"04b"))

a = 0b0100
print("\nnilai a :",a," bit :",format(a,"04b"))
a <<= 1
print("nilai a :",a," bit :",format(a,"04b"))