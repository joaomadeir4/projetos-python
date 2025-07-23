# Sistema Bancário em Python

![Versão](https://img.shields.io/badge/vers%C3%A3o-2.0-blueviolet)
![Linguagem](https://img.shields.io/badge/linguagem-Python-blue)

## 📄 Descrição do Projeto

Este projeto implementa um sistema bancário em Python. Nascido de um desafio da [DIO](https://www.dio.me/). Que visava criar as operações básicas de depósito, saque e extrato, o sistema foi posteriormente refatorado para sua v2. A versão atual introduz uma arquitetura modular baseada em funções e expande as capacidades do sistema, permitindo o cadastro de múltiplos usuários e a criação de contas correntes.

## ⚙️ Funcionalidades

### Gerenciamento
-   [x] **Criar Usuário:** Cadastra um novo cliente no sistema.
-   [x] **Criar Conta Corrente:** Cadastra uma nova conta bancária vinculada a um usuário.

### Operações Bancárias
-   [x] **Depositar:** Permite ao usuário depositar valores positivos em sua conta.
-   [x] **Sacar:** Permite ao usuário sacar valores, respeitando um limite de R$ 500 por saque e um máximo de 3 saques diários.
-   [x] **Extrato:** Exibe todas as transações realizadas e o saldo atual da conta.

## 🛠️ Tecnologias Utilizadas
-   **Python 3**
-   **VS Code**
## ▶️ Como Executar o Projeto

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/joaomadeira4/projetos-python.git](https://github.com/joaomadeira4/projetos-python.git)
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd projetos-python
    ```
3.  Execute o script Python:
    ```bash
    python sistema_bancario.py
    ```
 
---

<details> <b> <summary>📜 Histórico e Evolução do Desafio</b></summary>
  <p>  

  ### Detalhamento da v1:
  
  -   **Operação de Depósito:** Deve ser possível depositar valores positivos para a conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma, não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

  
  -   **Operação de Saque:** O sistema deve permitir realizar `3 saques diários com limite máximo de R$ 500,00 por saque`. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

  
  -   **Operação de Extrato:** Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: `Não foram realizadas movimentações.` Os valores devem ser exibidos utilizando o formato `R$ xxx.xx`.

  ---

  ### Detalhamento da v2:

  Para a segunda versão, o desafio foi evoluir o código para um modelo mais robusto e escalável. As melhorias implementadas foram:

  -   **Modularização:** Separar as operações de saque, depósito e extrato em funções dedicadas, melhorando a organização e legibilidade do código.
  -   **Novas Funcionalidades:**
      -   **Criar Usuário:** Implementar uma função para cadastrar novos clientes no banco.
      -   **Criar Conta Corrente:** Desenvolver uma função para criar uma nova conta bancária, vinculando-a a um usuário já existente.
      -   **Consulta de Contas Correntes Cadastradas:** Listar todas as contas correntes cadastradas, exibindo para cada uma os detalhes de agência, número da conta e o nome do titular.</p>
</details>


<p align="center">Feito por <b>João Madeira</b></p>
<p align="center">
  <a href="https://github.com/joaomadeir4">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />
  </a>
  <a href="https://www.linkedin.com/in/joaomadeir4/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
</p>
