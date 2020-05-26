"""
Fonte: http://dojopuzzles.com/problemas/exibe/ano-bissexto/
A cada 4 anos, a diferença de horas entre o ano solar e o do calendário
convencional completa cerca de 24 horas (mais exatamente: 23 horas, 15 minutos
e 864 milésimos de segundo). Para compensar essa diferença e evitar um
descompasso em relação às estações do ano, insere-se um dia extra no calendário
e o mês de fevereiro fica com 29 dias. Essa correção é especialmente importante
para atividades atreladas às estações, como a agricultura e até mesmo as festas
religiosas.

Um determinado ano é bissexto se:

O ano for divisível por 4, mas não divisível por 100, exceto se ele for também
divisível por 400.

Anos bissextos: 1600, 1732, 1888, 1944, 2008

Anos não bissexto: 1742, 1889, 1951, 2011
"""

import pytest


def eh_bissexto(ano):
    resto = ano % 4
    resto100 = ano % 100
    resto400 = ano % 400

    if not resto:
        if not resto400:
            return True
        elif resto100:
            return True

    return False


@pytest.mark.parametrize('ano', [1600, 1732, 1888, 1944, 2008])
def test_deve_ser_bissexto(ano):
    resp = eh_bissexto(ano)

    assert resp is True


@pytest.mark.parametrize('ano', [1742, 1889, 1951, 2011])
def test_nao_deve_ser_bissexto(ano):
    resp = eh_bissexto(ano)

    assert resp is False


def test_nao_deve_ser_bissexto_500():
    # setup
    ano = 500

    # execução do teste
    resp = eh_bissexto(ano)

    # verificação
    assert resp is False
