for i in range(10):
    print(i)

convidados = ['Elysson', 'Luana', 'Vinicius', 'Maria', 'Pedro', 'Priscila']

for convidado in convidados:
    print(convidado + ' esta convidado')


for i in range(len(convidados)):
    convidado = convidados[i]
    print(convidado + ' esta convidado (for range)')


saida = True
contador = 0

while contador > 5:
    contador = contador + 1
    print('While contador: ' + str(contador))
