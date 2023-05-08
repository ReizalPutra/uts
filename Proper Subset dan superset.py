A={1,2,3}
B={0,1,2,3,4,5,6,7,8,9}
C={1,3,10,11,12}
#PROPER SUPERSET
G=A>C
F=B>A
F1=C>B
print(10*"#"+"PROPER SUPERSET"+10*"#")
print((f"apakah A adalah proper superset C = {G}"))
print((f"apakah B adalah proper superset A = {F}"))
print((f"apakah C adalah proper superset B = {F1}"))
