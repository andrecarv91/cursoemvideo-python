# Exercício Python 105
# Faça um programa que tenha uma função notas() que pode receber
# várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

from statistics import mean
def notas(*n, sit=False):    
    """
        -> Função para analisar notas e situações de vários alunos.
        :param n: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional, indicando se deve ou não adicionar a situação
        :return: dicionário com várias informações sobre a situação da turma
    """
    dados = {}
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['média'] = mean(n)
    if sit == True:
        if mean(n) >= 7:
            dados['situação'] = 'BOA'
        elif mean(n) >= 5:
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'RUIM'

    return dados


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
