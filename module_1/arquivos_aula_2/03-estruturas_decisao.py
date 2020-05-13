idade = 20

if idade < 18:
    print("Menor de idade")
else:
    print("Maior de idade")


veiculo = {'tipo': 'moto2', 'marca': 'Honda', 'potencia_motor': 140}

if veiculo['tipo'] == 'moto' and veiculo['marca'] == 'Honda':
    print('O veículo é uma Moto')
else:
    print('O veículo não é uma Moto')


resultado = veiculo['tipo'] == 'moto'

print(resultado)


if veiculo['tipo'] == 'moto' or veiculo['potencia_motor'] < 120:
    print("Você tem um veículo muito rápido")
else:
    print('Seu veículo não é rápido')


if (veiculo['tipo'] == 'moto2' and veiculo['potencia_motor'] > 120) or veiculo['marca'] == 'Honda2':
    print("O seu veículo é muito bom")


if veiculo['tipo'] == 'moto':
    print("moto")
elif veiculo['tipo'] == 'carro':
    print('carro')
elif veiculo['tipo'] == 'moto2':
    print('moto2')

condicao = [1,2,3]

if len(condicao):
    print('verdadeiro')
else:
    print('falso')

print(len(condicao))
