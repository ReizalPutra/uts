print("\n"+5*"#"+" OPERASI DIFFERENCE PADA DATA SET "+5*"#"+"\n")
A={1,3,5,7,9}
B={0,2,4,5,6,7,8,9}
#menggunakan operator -
C=(A-B)
print(f"nilai pada himpunan A adalah = {A}")
print(f"nilai pada himpunan B adalah = {B}")
print((f"hasil dari operasi DIFFERENCE (dengan operator A-B) nilai himpunan A dan B adalah = {C}"))
#menggunakan method differnce
D= A.difference (B)
print((f"hasil dari operasi DIFFERENCE (dengan method difference) nilai himpunan A dan B adalah = {D}"))
