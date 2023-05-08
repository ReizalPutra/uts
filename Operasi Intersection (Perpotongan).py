print("\n"+5*"#"+" OPERASI INTERSECTION PADA DATA SET "+5*"#"+"\n")
A={1,3,5,7,9}
B={0,2,4,5,6,7,8,9}
#menggunakan operator &
C=(A&B)
print(f"nilai pada himpunan a adalah = {A}")
print(f"nilai pada himpunan b adalah = {B}")
print((f"hasil dari operasi perpotongan (dengan operator A&B) nilai himpunan a dan b adalah = {C}"))
#menggunakan method intersection
D=A.intersection(B)
print((f"hasil dari operasi perpotongan (dengan method intersection) nilai himpunan a dan b adalah = {D}"))