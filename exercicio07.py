# Exercício 07
# Criando uma função para verificar a situação de um aluno.

def verificar_situacao(nota):
    # A função recebe uma nota e retorna a situação.
    if nota >= 6:
        return "Aprovado"
    else:
        return "Reprovado"


# Testando a função com diferentes notas.
print(verificar_situacao(8.5))
print(verificar_situacao(4.0))