print(10*"-"+" TIPE-TIPE DATA SET "+10*"-")

# membuat set yang kosong
kosong =set()
print(f"ini data set yang kosong atau belum ditambahkan = {kosong}")

# menambahkan set
# numerik
tambah_num= int((input(" Masukan angka atau tipe data numerik = ")))
kosong.add(tambah_num)
# string
tambah_str= input("Masukan tipe data string = ")
kosong.add(tambah_str)

print(f"ini merupakan isi data set setelah ditambahkan = {kosong}")


