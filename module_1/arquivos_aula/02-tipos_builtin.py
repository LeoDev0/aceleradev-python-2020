lista_convidados = ['Élysson', 'Priscila', 'Pedro', 'Maria']

print(lista_convidados)

lista_convidados.append('Mauricio')

print(lista_convidados)

lista_convidados.remove('Élysson')

print(lista_convidados)

print(lista_convidados[0])

print(lista_convidados[3])
print(lista_convidados[-1])

lista_convidados.append(50)

print(lista_convidados)

# tuple
tupla1 = (1, 2, 3)
tupla2 = (4,5,6)

print(tupla1)

tupla3 = tupla1 + tupla2

print(tupla3)

# chave -> valor

dados_pessoais = {'nome': 'Batman', 'cidade': 'Gothan'}

print(dados_pessoais)

dados_pessoais['veiculo'] = 'Batmovel'

print(dados_pessoais)

del dados_pessoais['cidade']

print(dados_pessoais)
