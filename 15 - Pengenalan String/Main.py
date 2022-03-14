# string adalah sebuah tipe data yang terdiri dari beberapa kumpulan karakter

# 1. MEMBUAT STRING

# dengan menggunakan single quote ''
print('Menggunakan single quote')

# dengan menggunakan double quote ""
print("Menggunakan double quote")

# gabungan antara single quote dan double quote
print("'Hallo, apa kabar?'") 
print('"Kabar baik"')
print("ini adalah hari jum'at") # jika ada single quote dalam string, gunakan penutup double quote



# 2. MENGGUNAKAN TANDA \

# mengatasi penutup yang digunakan dalam string
print('ayo sholat jum\'at')
print('let\'s play\'n happy')

# backslash \
# untuk menampilkan backslash kedalam string -> gunakan double backslash \\
print("C:\\User\\NameUser")

# tab
print("akan \tjauhan")

# backspace atau delete
print("spasi \bini \bakan \bdihapus")

# newline
print("baris pertama.\nbaris kedua.") # LF -> Line Feed -> unix, mac, linux
print("baris pertama.\rbaris kedua.") # CR -> Carriage Return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF -> Carriage Return Line Feed -> windows
# LE, CR, CRLF digunakan untuk mendeteksi enter atau line sequence pada sistem operasi



# 3. STRING LITERAL ATAU RAW

# sangat penting dalam menulis string
# contoh menulis path C:\newfolder -> perhatikan \n -> akan eror
print("C:\newfolder") # akan eror pathnya

# berikut pemecahan masalahnya

# menggunakan raw string
print(r"C:\newfolder") # tambahkan r didepan untuk memandakan raw string
# apapun yang kita masukan dalam pentup mau itu \ akan dianggap sebagai string

# multiline literal string
print("""

nama\t: suwes
alamat\t: jakarta

""")

# multiline literal dan rawstring
print(r"""

nama\t: suwes
alamat\t: jakarta

""")