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
XD1=6
YD1=4
Coordenadas = [[2,8],[10,7],[1,3],[6,4],[8,2]]

def funcaoObjetivo():
    maxj = 4
    j=0
    total = 0
    while(j<=maxj):
        total += abs(eval("XD1") - Coordenadas[j][0]) + abs(eval("YD1") - Coordenadas[j][1])
        j += 1
    return total

confirmacao = [
X1 + Y1 + X2 + Y2 + X3 + Y3 + X4 + Y4 + X5 + Y5 == funcaoObjetivo()
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
]


def printDesenvolvimento():
    lista = ["X","Y"]
    lol = ""
    for a in range(1,6):
        for b in lista :
            lol += str(eval (b + str(a))) + " + "
    lol += ("== " + str(funcaoObjetivo()) )
    print(lol)


print(confirmacao)
if(any(confirmacao)):
    print("Passou todas as verificacoes ! ")
    printDesenvolvimento()
else:
    print("falhou verificacoes")
