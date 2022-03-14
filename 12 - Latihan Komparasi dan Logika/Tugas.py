# mencari nilai dalam beberapa rentang
# dengan menggunakan operator komparasi dan logika


# soal 1

# ---- 0 ++++ 3 ---- 5 ++++ 8 ---- 10 ++++

userInput = int(input("masukan nilai : "))
print("nilai yang kamu masukan =",userInput)

hasilA = (userInput > 0)
print("lebih dari 0 =",hasilA)

hasilB = (userInput < 3)
print("kurang dari 3 =",hasilB)

hasilC = (userInput > 5)
print("lebih dari 5 =",hasilC)

hasilD = (userInput < 8)
print("kurang dari 8 =",hasilD)

hasilE = (userInput > 10)
print("lebih dari 10 =",hasilE)

hasil = (hasilA and hasilB) or (hasilC and hasilD) or hasilE
print("hasilnya = ",hasil)


# soal 2

# ++++ 0 ---- 3 ++++ 5 ---- 8 ++++ 10 ----

userInput = int(input("masukan nilai : "))
print("nilai yang kamu masukan =",userInput)

hasilA = (userInput < 0)
print("kurang dari 0 =",hasilA)

hasilB = (userInput > 3)
print("lebih dari 3 =",hasilB)

hasilC = (userInput < 5)
print("kurang dari 5 =",hasilC)

hasilD = (userInput > 8)
print("lebih dari 8 =",hasilD)

hasilE = (userInput < 10)
print("kurang dari 10 =",hasilE)

hasil = (hasilA or hasilB) and (hasilC or hasilD) and hasilE
print("hasilnya = ",hasil)

