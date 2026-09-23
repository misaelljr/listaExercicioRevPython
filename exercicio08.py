# Exercício 08
# Criando uma função para verificar um empréstimo.

def verificar_emprestimo(disponivel):
    # Verifica a disponibilidade do equipamento.
    if disponivel:
        return "Empréstimo permitido"
    else:
        return "Equipamento indisponível"


# Testando as duas possibilidades.
print(verificar_emprestimo(True))
print(verificar_emprestimo(False))