# Exercício 10
# Integração de listas, dicionários, funções,
# estruturas condicionais e repetição.

# Função responsável por verificar a situação do aluno.
def verificar_situacao(nota):
    if nota >= 6:
        return "Aprovado"
    else:
        return "Reprovado"


# Lista contendo os alunos.
# Cada aluno é representado por um dicionário.
alunos = [
    {"nome": "Ana", "nota": 8.0},
    {"nome": "Carlos", "nota": 5.5},
    {"nome": "Maria", "nota": 9.0},
    {"nome": "João", "nota": 4.5}
]


# Percorre todos os alunos.
for aluno in alunos:

    # Obtém os dados do aluno atual.
    nome = aluno["nome"]
    nota = aluno["nota"]

    # Utiliza a função para descobrir a situação.
    situacao = verificar_situacao(nota)

    # Exibe o resultado.
    print(f"{nome} - {nota} - {situacao}")