X1=60
Y1=60
X2=32
Y2=24
X3=85
Y3=17
X4=0
Y4=0
X5=8
Y5=8
X6=24
Y6=24
X7=36
Y7=90
X8=56
Y8=8
X9=8
Y9=8
X10=0
Y10=0
X11=10
Y11=10
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
    while (i<=maxi):
        j=0
        while(j<=maxj):
            total += NumeroDeDeslocacoes[i][j]* ( abs(eval("XD" +str(i+1)) -
                                                      Coordenadas[j][0]) +
                                                 abs(eval("YD" + str(i+1)) -
                                                     Coordenadas[j][1]))
            j += 1
        i+=1
    return total

def funcaoObjetivo():
    return 5*(abs(XD1-XD2)+abs(YD1-YD2)) + Somatorio()


confirmacao = [
X1 + Y1 + X2 + Y2 + X3 + Y3 + X4 + Y4 + X5 + Y5 + X6 + Y6+ X7 + Y7 + X8 + Y8 + X9 + Y9 + X10 + Y10 + X11 + Y11 == funcaoObjetivo()
,
X1 >= 15*XD1 - 30
,X1 >=( -15)*XD1 + 30
,Y1 >= 15*YD1 - 120
,Y1 >= (-15)*YD1 + 120

,X2 >= 8*XD1 - 80
,X2 >= (-8)*XD1 + 80
,Y2 >= 8*YD1 -56
,Y2 >= (-8)*YD1 + 56

,X3 >= 17*XD1 - 17
,X3 >=  (-17)*XD1 + 17
,Y3 >= 17*YD1 - 51
,Y3 >=  (-17)*YD1 + 51

,X4 >= 58*XD1 - 348
,X4 >=  (-58)*XD1 + 348
,Y4 >= 58*YD1 - 232
,Y4 >=  (-58)*YD1 + 232

,X5 >= 4*XD1 - 32
,X5 >=  (-4)*XD1 + 32
,Y5 >= 4*YD1 - 8
,Y5 >=  (-4)*YD1 + 8

,X6 >= 4*XD2 - 8
,X6 >=  (-4)*XD2 + 8
,Y6 >= 4*YD2 - 32
,Y6 >=  (-4)*YD2 + 32

,X7 >= 18*XD2 - 180
,X7 >=  (-18)*XD2 + 180
,Y7 >= 18*YD2 - 126
,Y7 >=  (-18)*YD2 + 126

,X8 >= 8*XD2 - 8
,X8 >=  (-8)*XD2 + 8
,Y8 >= 8*YD2 - 24
,Y8 >=  (-8)*YD2 + 24

,X9 >= 4*XD2 - 24
,X9 >=  (-4)*XD2 + 24
,Y9 >= 4*YD2 - 16
,Y9 >=  (-4)*YD2 + 16

,X10 >= 82*XD2 - 656
,X10 >=  (-82)*XD2 + 656
,Y10 >= 82*YD2 - 164
,Y10 >=  (-82)*YD2 + 164

,X11 >= 5*XD1 - 5*XD2
,X11 >=  (-5)*XD1 + 5*XD2
,Y11 >= 5*YD1 - 5*YD2
,Y11 >=  (-5)*YD1 + 5*YD2
]


def printDesenvolvimento():
    lista = ["X","Y"]
    lol = ""
    for a in range(1,12):
        for b in lista :
            lol += str(eval (b + str(a)))+ " + "
    lol += str(X11) + " + "+ str(Y11)
    lol += (" == " + str(funcaoObjetivo()) )
    print(lol)


print(confirmacao)
if(all(confirmacao)):
    print("Passou todas as verificacoes ! ")
    printDesenvolvimento()
else:
    print("falhou verificacoes")
