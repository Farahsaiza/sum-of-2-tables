N=int(input("entrer la taille des tableaux: "))
T1=[]
for i in range (N):
    A=int(input("entrer un nbre pour le premier tableau: "))
    T1.append(A)
T2=[]
for i in range (N):
    B=int(input("entrer un nbre pour le deuxieme tableau: "))
    T2.append(B)
T=[]
for i in range  (N):
    C=T1[i]+T2[i]
    T.append(C)
print(T)

