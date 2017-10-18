X1 = 3.5
Y1 = 3
X2 = 4.5
Y2 = 2
X3 = 4.5
Y3 = 2
X4 = 0.5
Y4 = 1
X5 = 2.5
Y5 = 4
XD = 5.5
YD = 5
D = 6.5

Coordenadas = [[2,8],[10,7],[1,3],[6,4],[8,2]]

def maiorDistancia(Coordenadas):
    total = 0
    for (a,b) in Coordenadas:
        total = max(total,abs(XD - a) + abs(YD - b))
    return(total)


confirmacao = [
X1 >= XD - 2
,X1 >=  - XD + 2
,Y1 >= YD - 8
,Y1 >=  - YD + 8

,X2 >= XD - 10
,X2 >=  - XD + 10
,Y2 >= YD - 7
,Y2 >= -YD + 7

,X3 >= XD - 1
,X3 >=  - XD + 1
,Y3 >= YD - 3
,Y3 >=  - YD + 3

,X4 >= XD - 6
,X4 >=  - XD + 6
,Y4 >= YD - 4
,Y4 >=  - YD + 4

,X5 >= XD - 8
,X5 >=  - XD + 8
,Y5 >= YD - 2
,Y5 >=  - YD + 2

,D >= X1+Y1
,D >= X2+Y2
,D >= X3+Y3
,D >= X4+Y4
,D >= X5+Y5
,maiorDistancia(Coordenadas)==6.5
]

print(confirmacao)
if(all(confirmacao)):
    print("Passou todas as verificacoes ! ")
else:
    print("falhou verificacoes")
