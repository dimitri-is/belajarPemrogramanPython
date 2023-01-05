# penulisan statement
print("Hello World!")
print("Belajar Python dari Nol")
nama = "Penceng"
# output >
# Hello World!
# Belajar Python dari Nol
#
# jika ingin menulis lebih dari satu statement di satu baris. harus memisahnya dengan titik koma
print("Hello")
print("World!")
print("Latihan Python Untuk Pemula")
nama_depan = "Dimitri"
nama_belakang = "Irfan"
# output    >
# Hello
# World!
# Latihan Python Untuk Pemula


# penulisan string
judul = "Belajar Pemrograman Python sampai bisa"
penulis = 'Penceng Kode'
# atau bisa juga menggunakan triple tanda petik =
judul = "Belajar Pemrograman Python sampai bisa"
penulis = '''Penceng Kode'''


# penulisan case pada python
judul = "Belajar Dasar-dasar Python"
Judul = "Belajar Membuat Program Python"


# case style
# Snake Case digunakan pada:
module_name, package_name, method_name, function_name, , global_var_name, instance_var_name, function_parameter_name, local_var_name.

# CamelCase digunakan Pada:
ClassName, ExceptionName

# ALL CAPS digunakan Pada:
GLOBAL_CONSTANT_NAME


# penulisan blok
# print("hello")
# if nama == 'Penceng Kode':
#     print(nama)
#     print("Selamat datang")
# print("World!")
# penulisan yang benar
# blok percabangan if
if username == 'petanikode':
    print("Selamat Datang Admin")
    print("Silahkan ambil tempat duduk")

# blok percabangan for
for i in range(10):
    print i
# contoh yang salah
# blok percabangan if
    if username == 'petanikode':
    print("Selamat Datang Admin")
    print("Silahkan ambil tempat duduk")

    # blok percabangan for
    for i in range(10):
    print i
