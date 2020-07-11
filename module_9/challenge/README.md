# Desafio Continuous integration

A integração contínua é uma parte importante do desenvolvimento de software e possui várias
vantagens, como um ciclo de desenvolvimento mais rápido, maior qualidade do software. O Travis CI é um serviço que fornece integração contínua e testará seu projeto de software a cada mudança, para isso precisamos criar um arquivo na raiz do nosso projeto, chamado .travis.yml, este arquivo contém as configurações específicas do nosso projeto, a plataforma do travisci usa esse arquivo para para saber como validar nosso projeto.

Nosso projeto deverá rodar em versões do Python 2.7.13, PyPy 7.1.1, Python 3.6.1, PyPy 7.1.1-beta0, vamos configurar o arquivo para usar o Pytest para rodar os testes e  instalar as dependências que estão em requirements.txt

A solução deve ser implementada dentro da string config no arquivo main.py

## Tópicos



Neste desafio você vai aprender:

- Conceitos de integração contínua
- Configuração Travis CI


## Requisitos

Você precisará de python 3.6 (ou superior) e do gerenciador de pacotes pip.

O recomendado é você utilizar um [ambiente virtual](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais). Para isto, execute os comandos como no exemplo abaixo:

    pip3 install virtualenv
    virtualenv venv -p python3
    source venv/bin/activate 
    pip install -r requirements.txt

Ao terminar o desafio, você pode sair do ambiente criado com o comando `deactivate`
