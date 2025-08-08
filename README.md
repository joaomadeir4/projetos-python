# Sistema Bancário em Python

![Versão](https://img.shields.io/badge/vers%C3%A3o-3.0-blueviolet)
![Linguagem](https://img.shields.io/badge/linguagem-Python-blue)

## 📄 Descrição do Projeto

Este projeto é um sistema bancário desenvolvido em Python, inspirado em um desafio da [DIO](https://www.dio.me/) que propunha criar as operações básicas de depósito, saque e extrato. Com o tempo, o código foi refatorado e aprimorado, ganhando uma arquitetura mais robusta, agora estruturada com os princípios da Programação Orientada a Objetos (POO).

## ⚙️ Funcionalidades

### Gerenciamento
-   [x] **Criar Usuário:** Cadastra um novo cliente no sistema.
-   [x] **Criar Conta Corrente:** Cadastra uma nova conta bancária vinculada a um usuário.
-   [x] **Listar Contas:** Exibe os dados de todas as contas cadastradas.

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
      -   **Consulta de Contas Correntes Cadastradas:** Listar todas as contas correntes cadastradas, exibindo para cada uma os detalhes de agência, número da conta e o nome do titular.
      
      ---

  ### Detalhamento da v3:

A terceira versão do sistema marca uma refatoração completa, migrando do paradigma procedural para a Programação Orientada a Objetos (POO). O objetivo foi construir uma base mais robusta, escalável e coesa, seguindo boas práticas de modelagem e organização do código.

- **Modelagem de Domínio**: Criação de classes para representar as principais entidades — Cliente, PessoaFisica, Conta, ContaCorrente e Historico.

- **Sistema de Transações**: Implementação de uma classe abstrata Transacao, da qual herdam as classes concretas Saque e Deposito, permitindo polimorfismo, centralização do registro de operações e facilidade para incluir novas transações futuramente.

- **Separação de Responsabilidades**: Cada classe gerencia seu próprio estado e comportamento. Por exemplo, apenas a classe Conta pode alterar seu saldo e registrar movimentações no Historico.

- **Desacoplamento**: A função principal (main) foi simplificada e passou a atuar como uma camada de orquestração, delegando as tarefas para os objetos corretos.</p>
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
