# latihan konversi satuan temperature

# konversi satuan celcius
celcius = float(input("masukan suhu dalam celcius : "))
print("\nsuhu dalam celcius adalah ",celcius)

fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah ",fahrenheit)

kelvin = celcius + 273.15
print("suhu dalam kelvin adalah ",kelvin)

reamur = (4/5) * celcius
print("suhu dalam reamur adalah ",reamur)


# konversi satuan fahrenheit
fahrenheit = float(input("\nmasukan suhu dalam fahrenheit : "))
print("\nsuhu dalam fahrenheit adalah ",fahrenheit)

celcius = (5 / 9) * (fahrenheit - 32)
c1 = celcius
print("suhu dalam celcius adalah ",celcius)

kelvin = c1 + 273.15
print("suhu dalam kelvin adalah ",kelvin)

reamur = (4/9) * (fahrenheit - 32)
print("suhu dalam reamur adalah ",reamur)


# konversi satuan kelvin
kelvin = float(input("\nmasukan suhu dalam kelvin : "))
print("\nsuhu dalam kelvin adalah ",kelvin)

celcius = kelvin - 273.15
c2 = celcius
print("suhu dalam celcius adalah ",celcius)

fahrenheit = ((9/5) * c2) + 32
print("suhu dalam fahrenheit adalah ",fahrenheit)

reamur = (4/5) * c2
print("suhu dalam reamur adalah ",reamur)


# konversi satuan reamur
reamur = float(input("\nmasukan suhu dalam reamur : "))
print("\nsuhu dalam reamur adalah ",reamur)

celcius = (5/4) * reamur
c3 = celcius
print("suhu dalam celcius adalah ",celcius)

fahrenheit = ((9/4) * reamur) + 32
print("suhu dalam fahrenheit adalah ",fahrenheit)

kelvin = c3 + 273.15
print("suhu dalam kelvin adalah ",kelvin)

