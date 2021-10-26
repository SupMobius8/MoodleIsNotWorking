inimesed=[]
palgad=[]
from random import *
def sisesta_andmed(i, p):
    N=4
    for n in range(N):
        inimene=input('Teie nimi: ')
        i.append(inimene)
        palk=randint(1000,10000)
        p.append(palk)
    return i,p
def andmed_ekranile(i,p):
    N=len(i)
    for n in range(N):
        print(i[n],'-',p[n])
def kustutamine(i,p):
    nimi=input('Sisesta nimi, keda vaja kustutada: ')
    n=i.count(nimi)
    abi_list=[]
    if n>0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(e)
                print(t,'.',i[e],'-',p[e])
        j=int(input('Järjekordne number: '))
        i.pop(abi_list[j-1])
        p.pop(abi_list[j-1])
    return(i,p)
def suurim_palk(i,p):
    suurim=max(p)
    d=p.index(suurim)
    print(i[d],"-",p[d])
    return i,p 
def sorteerimine(i,p,v):
    N=len(p)
    if v==1:
        for n in range(0,N):
            for m in range (n,N):
                if p[n]<p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    else:
        for n in range(0,N):
            for m in range (n,N):
                if p[n]>p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    andmed_ekranile(i,p)
def vordsed_palgad(i,p):
    N=len(p)
    dublikatid=[x for x in palgad if palgad.count(x)>1 ]
    print(list(set(dublikatid)))
while 1:
    valik=input('a - andmete sisestamine\ne - andmed ekranile\nk - kustutamine inimese palk\nmax - suurim palk\ns - sorteerimine\nTeie valik: ')
    if valik.lower()=='a':
        inimesed,palgad=sisesta_andmed(inimesed,palgad)
    elif valik.lower()=='e':
        andmed_ekranile(inimesed,palgad)
    elif valik.lower()=='k':
        inimesed,palgad=kustutamine(inimesed,palgad)
    elif valik.lower()=='max':
        inimesed,palgad=suurim_palk(inimesed,palgad)
    elif valik.lower()=="s":
        sorteerimine(inimesed,palgad,int(input("1-kahaneb, 2-kasvab")))
    elif valik.lower()=="d":

    else:
        break
    print()
inimesed,palgad=sisesta_andmed(inimesed,palgad)
andmed_ekranile(inimesed,palgad)

#while nimi.isalpha()!=True:
#            try:
#                nimi=input("Try one more time: ")
#            except:
#                ValueError