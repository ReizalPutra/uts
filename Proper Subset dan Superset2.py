A={1,2,3}
B={0,1,2,3,4,5,6,7,8,9}
C={1,3,10,11,12}
#PROPER SUBSET
D=A<B
E=A<C
E1=B<C
print(10*"#"+"PROPER SUBSET"+10*"#")
print((f"apakah A adalah proper subset B = {D}"))
print((f"apakah a adalah proper subset c = {E}"))
print((f"apakah B adalah proper subset C = {E1}"))