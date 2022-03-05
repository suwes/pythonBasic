# konversi tipe data atau casting
# merubah tipe data dari vari lain
# tipe data = int, float, string, bool

#integer
print("====INTEGER====")
data_int = 1
print(type(data_int))

data_float = float(data_int) # casting data diawali dengan tipe data
data_str = str(data_int) # casting data diawali dengan tipe data
data_bool = bool(data_int) # casting data diawali dengan tipe data
print("data float = ",data_float," bertipe = ",type(data_float))
print("data str = ",data_str," bertipe = ",type(data_str))
print("data bool = ",data_bool," bertipe = ",type(data_bool))

# float
print("====FLOAT====")
data_float = 10.5
print(type(data_float))

data_int = int(data_float) # casting data diawali dengan tipe data
data_str = str(data_float) # casting data diawali dengan tipe data
data_bool = bool(data_float) # casting data diawali dengan tipe data
print("data int = ",data_int," bertipe = ",type(data_int))
print("data str = ",data_str," bertipe = ",type(data_str))
print("data bool = ",data_bool," bertipe = ",type(data_bool))

# boolean
print("====BOOLEAN====")
data_bool = True
print(type(data_bool))

data_int = int(data_bool) # casting data diawali dengan tipe data
data_str = str(data_bool) # casting data diawali dengan tipe data
data_float = float(data_bool) # casting data diawali dengan tipe data
print("data int = ",data_int," bertipe = ",type(data_int))
print("data str = ",data_str," bertipe = ",type(data_str))
print("data float = ",data_float," bertipe = ",type(data_float))

# string
print("====STRING====")
data_str = "20"
print(type(data_str))

data_int = int(data_str) # stringnya harus angka
data_float = float(data_str) # cstringnya harus  angka
data_bool = bool(data_str) # casting data diawali dengan tipe data
print("data int = ",data_int," bertipe = ",type(data_int))
print("data float = ",data_float," bertipe = ",type(data_float))
# akan false jika stringnya kososng
print("data bool = ",data_bool," bertipe = ",type(data_bool))


