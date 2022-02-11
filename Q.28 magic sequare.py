




a=[[2,7,6],[9,5,1],[4,3,8]]
print("matrix is......")
for i in range (3):
    for j in range(3):
        print(a[i][j],end=" ")
    print()
sumd1=0
sumd2=0
for i in range(3):
    for j in range(3):
        if i==j:
            sumd1=sumd1+a[i][j]
        if i+j==2:
            sumd2=sumd2+a[i][j]
print(sumd1)
print(sumd2)
if sumd1==sumd2:
    sumr1=0
    sumc1=0
    sumr2=0
    sumc2=0
    sumr3=0
    sumc3=0
    for i in range(3):
        for j in range(3):
            if i==0:
                sumr1=sumr1+a[i][j]
                sumc1+=a[j][i]
            if i==1:
                sumr2+=a[i][j]
                sumc2+=a[j][i]
            if i==2:
                sumr3+=a[i][j]
                sumc3+=a[j][i]
    print(sumr1,sumr2,sumr3,sumc1,sumc2,sumc3)
    if sumd1==sumr1 and sumd1==sumr2 and sumd1==sumr3:
        f=0
    if sumd2==sumc1 and sumd2==sumc2 and sumd2==sumc3:
        f=0
    else:
        f=1
else:
    f=1
if f==0:
    print("matrix is a magic sequare")
else:
    print("matrix is not a magic sequare")




