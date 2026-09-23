Claro. Abaixo está o **README completo**, já pronto para copiar e colar no `README.md` do GitHub.

# 🐍 Revisão de Python para Desenvolvimento Web

Material de apoio da disciplina de **Programação Web**, destinado aos estudantes do **2º ano do Ensino Médio Integrado em Informática** do **Instituto Federal do Piauí (IFPI)**.

Este repositório contém as resoluções dos exercícios da **Lista de Exercícios — Revisão de Python para Desenvolvimento Web**.

O objetivo é revisar conceitos fundamentais de Python que serão utilizados nas próximas aulas de desenvolvimento Web com **Flask**.

---

## 🎯 Objetivo

Revisar conceitos básicos da linguagem Python necessários para iniciar o desenvolvimento de aplicações Web no lado do servidor.

Ao longo dos exercícios são trabalhados:

- Variáveis;
- Tipos básicos de dados;
- Estruturas condicionais (`if` e `else`);
- Listas;
- Estrutura de repetição `for`;
- Dicionários;
- Funções;
- Parâmetros;
- `return`;
- Listas de dicionários;
- Integração entre diferentes conceitos da linguagem.

---

## 📂 Estrutura do repositório

```text
listaExercicioRevPython/
├── README.md
├── exercicio01.py
├── exercicio02.py
├── exercicio03.py
├── exercicio04.py
├── exercicio05.py
├── exercicio06.py
├── exercicio07.py
├── exercicio08.py
├── exercicio09.py
└── exercicio10.py
```

Cada arquivo corresponde à resolução de um exercício da lista.

---

## ▶️ Como executar os exercícios

### 1. Verifique se o Python está instalado

Abra o terminal e execute:

```bash
python --version
```

Dependendo do sistema operacional, também pode ser necessário utilizar:

```bash
python3 --version
```

Se o Python estiver instalado corretamente, será apresentada a versão disponível no computador.

Exemplo:

```text
Python 3.x.x
```

### 2. Acesse a pasta do projeto

No terminal, navegue até a pasta onde os arquivos foram salvos.

### 3. Execute o exercício desejado

Por exemplo:

```bash
python exercicio01.py
```

Para executar outro exercício:

```bash
python exercicio07.py
```

Caso seu ambiente utilize `python3`:

```bash
python3 exercicio07.py
```

---

# 📚 Exercícios

## Exercício 01 — Variáveis

Revisão da criação de variáveis e armazenamento de informações.

O exercício utiliza dados de um aluno, como:

- Nome;
- Idade;
- Turma;
- Nota.

**Conceitos principais:** variáveis, strings, números e `print()`.

---

## Exercício 02 — Estruturas condicionais

Utilização de `if` e `else` para determinar a situação de um aluno a partir de sua nota.

Regra utilizada:

```text
Nota >= 6 → Aprovado
Nota < 6  → Reprovado
```

**Conceitos principais:** variáveis, operadores relacionais e estruturas condicionais.

---

## Exercício 03 — Empréstimo de equipamentos

Implementação de uma regra simples para verificar se determinado equipamento está disponível para empréstimo.

Exemplo:

```python
equipamento = "Notebook"
disponivel = True
```

**Conceitos principais:** valores booleanos, `if`, `else` e regras de negócio.

---

## Exercício 04 — Listas e repetição

Utilização de uma lista para armazenar vários alunos e da estrutura `for` para percorrer seus elementos.

Exemplo:

```python
alunos = ["Ana", "Carlos", "Maria"]
```

**Conceitos principais:** listas, `append()` e `for`.

---

## Exercício 05 — Dicionários

Representação das informações de um aluno utilizando um dicionário Python.

Exemplo:

```python
aluno = {
    "nome": "Maria",
    "nota": 8.5,
    "turma": "2º ano"
}
```

**Conceitos principais:** dicionários, chaves e valores.

---

## Exercício 06 — Dicionário de equipamento

Utilização de um dicionário para representar diferentes informações relacionadas a um equipamento.

São armazenados dados como:

- Código;
- Nome;
- Tipo;
- Disponibilidade.

**Conceitos principais:** dicionários e acesso aos valores por meio das chaves.

---

## Exercício 07 — Funções

Criação de uma função responsável por verificar a situação de um aluno.

```python
verificar_situacao(nota)
```

A função recebe uma nota e retorna:

```text
Aprovado
```

ou:

```text
Reprovado
```

**Conceitos principais:** funções, parâmetros, `if/else` e `return`.

---

## Exercício 08 — Função de empréstimo

Criação da função:

```python
verificar_emprestimo(disponivel)
```

A função verifica a disponibilidade de um equipamento e retorna uma mensagem adequada.

**Conceitos principais:** funções, parâmetros, valores booleanos e `return`.

---

## Exercício 09 — Lista de dicionários

Combinação de dois conceitos importantes:

```text
Lista + Dicionários
```

Cada aluno é representado por um dicionário:

```python
{"nome": "Ana", "nota": 8.0}
```

e vários alunos são armazenados dentro de uma lista:

```python
alunos = [
    {"nome": "Ana", "nota": 8.0},
    {"nome": "Carlos", "nota": 5.5},
    {"nome": "Maria", "nota": 9.0}
]
```

**Conceitos principais:** listas, dicionários, `for` e acesso aos dados.

---

## Exercício 10 — Desafio Integrador ⭐

O último exercício reúne vários conceitos trabalhados anteriormente.

São utilizados:

- Listas;
- Dicionários;
- Estrutura `for`;
- Estruturas `if/else`;
- Funções;
- Parâmetros;
- `return`.

O programa percorre uma lista de alunos, verifica a nota de cada um e apresenta sua situação.

Exemplo de saída:

```text
Ana - 8.0 - Aprovado
Carlos - 5.5 - Reprovado
Maria - 9.0 - Aprovado
João - 4.5 - Reprovado
```

---

# 🌐 Relação com Desenvolvimento Web

Por que estamos revisando Python em uma disciplina de **Programação Web**?

Nas próximas aulas utilizaremos Python no desenvolvimento do **Back-end** das nossas aplicações.

Até agora, trabalhamos com funções como:

```python
def inicio():
    return "Olá, turma!"
```

Com o Flask, poderemos associar essa função a uma **rota Web**:

```python
@app.route("/")
def inicio():
    return "Olá, turma!"
```

Assim, quando o navegador acessar determinada rota, uma função Python poderá ser executada para produzir uma resposta.

O fluxo básico será:

```text
Navegador
    ↓
Requisição HTTP
    ↓
Flask
    ↓
Rota
    ↓
Função Python
    ↓
Processamento
    ↓
Resposta
    ↓
Navegador
```

Portanto, os conceitos revisados neste repositório serão utilizados diretamente durante o desenvolvimento das nossas aplicações Web.

---

## 🚀 Próximos passos

Após esta revisão, avançaremos para:

```text
Python
   ↓
Flask
   ↓
Aplicação Web
   ↓
Rotas
   ↓
Funções Python
   ↓
Respostas para o navegador
```

A ideia é evoluir gradualmente de pequenos programas Python para **aplicações Web dinâmicas**.

---

## 👨‍🏫 Informações

**Disciplina:** Programação Web  
**Curso:** Ensino Médio Integrado em Informática  
**Turma:** 2º ano  
**Professor:** Misael Costa Júnior  
**Instituição:** Instituto Federal do Piauí — IFPI