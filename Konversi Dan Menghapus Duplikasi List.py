print("\n"+5*"#"+" KONVERSI TIPE DATA LIST KE DATA SET_ "+5*"#"+"\n")
mylist=["senin", 1, "selasa", 2, "rabu", 2, "kamis", 4,"senin", 4] 
print(f" contoh data list = {mylist}") 
myset=set(mylist)
print(f"hasil konversi data list menjadi data set = {myset}")
print("\n"+5*"#"+" KONVERSI TIPE DATA SET KE DATA LIST "+5*"#"+"\n")
print (f"contoh data set = {myset}")
con_list=list(myset)
print(f"hasil konversi data set menjadi data list = {con_list}")