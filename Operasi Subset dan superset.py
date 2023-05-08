print("\n"+5*"#"+" OPERASI SUPERSET PADA DATA SET "+5*"#"+"\n")
A={1,2,3}
B={0,1,2,3,4,5,6,7,8,9}
C={1,3,10,11,12}
#SUPERSET
g=A>=C
f=B>=A
h=A>=A
print(10*"#"+"SUPERSET"+10*"#")
print(f"nilai pada himpunan A adalah = {A}")
print(f"nilai pada himpunan B adalah = {B}")
print(f"nilai pada himpunan C adalah = {C}")
print((f"apakah A adalah superset C = {g}"))
print((f"apakah B adalah superset A = {f}"))
print((f"apakah A adalah superset A = {h}"))