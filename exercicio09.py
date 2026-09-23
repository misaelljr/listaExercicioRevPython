# Exercício 09
# Trabalhando com uma lista de dicionários.

alunos = [
    {"nome": "Ana", "nota": 8.0},
    {"nome": "Carlos", "nota": 5.5},
    {"nome": "Maria", "nota": 9.0}
]

# Percorre a lista.
for aluno in alunos:
    # Acessa nome e nota de cada dicionário.
    print(f"{aluno['nome']} - Nota: {aluno['nota']}")