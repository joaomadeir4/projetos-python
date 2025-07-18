# Sistema Bancário Simples em Python

![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![Linguagem](https://img.shields.io/badge/linguagem-Python-blue)

## 📄 Descrição do Projeto

Este projeto é um sistema bancário simples, desenvolvido em Python como parte de um desafio de projeto da [Digital Innovation One (DIO)](https://www.dio.me/). O objetivo é implementar as operações básicas de uma conta bancária: depósito, saque e extrato.

##  Funcionalidades

-   [x] **Depositar:** Permite ao usuário depositar valores positivos em sua conta.
-   [x] **Sacar:** Permite ao usuário sacar valores, respeitando um limite de R$ 500 por saque e um máximo de 3 saques diários.
-   [x] **Extrato:** Exibe todas as transações realizadas (depósitos e saques) e o saldo atual da conta.

## Tecnologias Utilizadas

-   **Python 3**
-   **VS Code**
<br>

## Como Executar o Projeto

Para rodar este projeto em sua máquina, siga os passos abaixo:

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/joaomadeira4/projetos-python.git](https://github.com/joaomadeira4/projetos-python.git)
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd projetos-python
    ```
3.  Execute o script Python:
    ```bash
    python sistema_bancario.py
    ```
---

<details>
  <summary>📜 Descrição Original do Desafio DIO</summary>

  #### Desafio: Criando um Sistema Bancário com Python
  
  Fomos contratados por um grande banco para desenvolver um novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python.
  
  Para a primeira versão do sistema, devemos implementar apenas 3 operações: Depósito, Saque e Extrato.
  
  #### Instruções das Operações
  
  **Operação de Depósito:**
  
  Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma, não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
  
  **Operação de Saque:**
  
  O sistema deve permitir realizar `3 saques diários com limite máximo de R$ 500,00 por saque`. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
  
  **Operação de Extrato:**
  
  Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: `Não foram realizadas movimentações.`
  Os valores devem ser exibidos utilizando o formato `R$ xxx.xx`.

</details>