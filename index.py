n1 = float(input('Digite a primeira nota do aluno'))
n2= float(input('Digite a segunda nota'))
n3= float(input('Digite a terceira nota'))
n4= float(input('Digite a quarta nota'))
m= (n1 + n2 + n3 + n4) / 4
print ("A media entre {} mais {} mais {} mais {} é igual a {:.1f}.".format(n1, n2, n3, n4 , m))
if m < 5:
    print('Você foi reprovado')
else:
    print('aprovado')