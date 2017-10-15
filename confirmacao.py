X1=4
Y1=4
X2=4
Y2=3
X3=5
Y3=1
X4=0
Y4=0
X5=2
Y5=2
X6=6
Y6=6
X7=2
Y7=5
X8=7
Y8=1
X9=2
Y9=2
X10=0
Y10=0
X11=2
Y11=2
XD1=6
YD1=4
XD2=8
YD2=2

NumeroDeDeslocacoes = [[15,8,17,58,4],[4,18,8,4,82]]
Coordenadas = [[2,8],[10,7],[1,3],[6,4],[8,2]]

def Somatorio():
    maxi = 1
    maxj = 4
    i=0
    total = 0
    while(i<= maxi):
        j=0
        while(j<=maxj):
            total += NumeroDeDeslocacoes[i][j]* ( abs(eval("XD" +str(i+1)) -
                                                      Coordenadas[j][0]) +
                                                 abs(eval("YD" + str(i+1)) -
                                                     Coordenadas[j][1]))
            j+= 1
        i+=1
    return total

def funcaoObjetivo():
    return 5 *(abs(XD1 - XD2)+abs(YD1 - YD2)) + Somatorio()

confirmacao= [
15*X1 + 15*Y1 + 8*X2 + 8*Y2 + 17 *X3 + 17*Y3 + 58*X4 + 58*Y4 + 4*X5 + 4*Y5 +
    4*X6 + 4*Y6 + 18*X7 + 18*Y7 + 8*X8 + 8*Y8 + 4*X9 + 4*Y9 + 82*X10 + 82*Y10 +
    5*X11 + 5*Y11 == funcaoObjetivo()
,
X1 >= XD1 - 2
,X1 >=  - XD1 + 2
,Y1 >= YD1 - 8
,Y1 >=  - YD1 + 8

,X2 >= XD1 - 10
,X2 >=  - XD1 + 10
,Y2 >= YD1 - 7
,Y2 >= -YD1 + 7

,X3 >= XD1 - 1
,X3 >=  - XD1 + 1
,Y3 >= YD1 - 3
,Y3 >=  - YD1 + 3

,X4 >= XD1 - 6
,X4 >=  - XD1 + 6
,Y4 >= YD1 - 4
,Y4 >=  - YD1 + 4

,X5 >= XD1 - 8
,X5 >=  - XD1 + 8
,Y5 >= YD1 - 2
,Y5 >=  - YD1 + 2

,X6 >= XD2 - 2
,X6 >=  - XD2 + 2
,Y6 >= YD2 - 8
,Y6 >=  - YD2 + 8

,X7 >= XD2 - 10
,X7 >=  - XD2 + 10
,Y7 >= YD2 - 7
,Y7 >=  - YD2 + 7

,X8 >= XD2 - 1
,X8 >=  - XD2 + 1
,Y8 >= YD2 - 3
,Y8 >=  - YD2 + 3

,X9 >= XD2 - 6
,X9 >=  - XD2 + 6
,Y9 >= YD2 - 4
,Y9 >=  - YD2 + 4

,X10 >= XD2 - 8
,X10 >=  - XD2 + 8
,Y10 >= YD2 - 2
,Y10 >=  - YD2 + 2

,X11 >= XD1 - XD2
,X11 >=  - XD1 + XD2
,Y11 >= YD1 - YD2
,Y11 >=  - YD1 + YD2
]


def printDesenvolvimento():
    lista = ["X","Y"]
    N = [item for sublist in NumeroDeDeslocacoes for item in sublist]
    lol = ""
    for a in range(1,11):
        for b in lista :
            lol += str(N[a-1]) + "*" + str(eval (b + str(a))) + "+ "
    lol += "5*"+ str(X11) + " + 5*" + str(Y11)
    lol += ("==" + str(funcaoObjetivo()) )
    print(lol)


print(confirmacao)
if(any(confirmacao)):
    print("Passou todas as verificacoes ! ")
    printDesenvolvimento()
else:
    print("falhou verificacoes")
