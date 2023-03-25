print('===============VENDA DO P1-A===============')                        #QUESTÃO 2
print('Preço da maçã por unidade --> R$ 1,30')                              #QUESTÃO 2
print('Preço da maçã - caixa com 12 und --> R$ 1,00')                       #QUESTÃO 2
qmaca=int(input('Digite quantas maçãs você deseja: '))                      #QUESTÃO 2
if qmaca <= 11:                                                             #QUESTÃO 2
    valorf1=qmaca*1.30                                                      #QUESTÃO 2
    print('O valor total da sua compra foi de: {:.2f}'.format(valorf1))     #QUESTÃO 2
else:                                                                       #QUESTÃO 2
    valorf2=qmaca*1                                                         #QUESTÃO 2
    print('O valor total da sua compra foi de:', valorf2)                   #QUESTÃO 2
print('================================================')                   #QUESTÃO 2