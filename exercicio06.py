# Exercício 06
# Representando um equipamento utilizando um dicionário.

equipamento = {
    "codigo": 101,
    "nome": "Projetor Epson",
    "tipo": "Projetor",
    "disponivel": True
}

# Exibe algumas informações do equipamento.
print(
    f"Equipamento: {equipamento['nome']} - "
    f"Disponível: {equipamento['disponivel']}"
)