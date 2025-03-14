# Desafio Sistema Bancário versão

Desafio proposto no bootcamp de python da plataforma DIO com a parceria da Suzano.

<details>
    <summary>Versão 01</summary>

## Entendendo o Desafio

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

---

### Operação de depósito

- Deve ser possível depositar valores positivos para a minha conta bancária.
- A v1 do projeto trabalha com apenas 1 usuário.
- Não precisamos identificar qual o número da agência e conta bancária.
- Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

---

### Operação de saque

- O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
- Caso o usuário não tenha saldo em conta, o sistema deve informar que não será possível sacar o dinheiro por falta de saldo.
- Todos os saques devem ser exibidos em uma variável e exibidos na operação de extrato.

---

### Operação de extrato

Essa operação deve listar todos os depósitos e saques realizados na conta.
- No fim da listagem deve ser exibido o saldo atual da conta.
- Os valors devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: `1500.45 = R$ 1500.45`
</details>

<details open>
    <summary>Versão 02</summary>

## Melhorias em geral

- [ ] Criar funções para todas as operações do sistema existentes
- [ ] Criar uma função para [Criar Usuário](#criar-usuário)
- [ ] Criar outra função para [Criar Conta Corrente](#criar-conta-corrente) e vincular com o usuário.
---

### Operação de Saque

- [ ] A função saque deve receber os argumentos apenas por nome (keyword only).
- [ ] Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
- [ ] Sugestão de retorno: Saldo e extrato
---

### Operação de Depósito

- [ ] A função depósito deve receber os argumentos apenas por posição (Positional only).
- [ ] Sugestão de argumentos: saldo, valor, extrato.
- [ ] Sugestão de retorno: saldo e extrato.
---

### Operação Extrato

- [ ] A função deve receber os argumentos por posição e nome (positional only e keyword only).
- [ ] Argumentos posicionais: saldo
- [ ] Argumentos nomeados: extrato.
---

### Criar usuário

- [ ] O programa deve armazenar os usuários em uma lista.
- [ ] Um usuário é composto por: nome, data de nascimento, cpf e endereço.
- [ ] O endereço é uma string com o formato: logradouro, numero - bairro - cidade/sigla estado.
- [ ] Deve ser armazenado somente os números do CPF.
- [ ] Não podem ser cadastrados 2 usuários com o mesmo CPF.
---

### Criar Conta Corrente

- [ ] O programa deve armazenar contas em uma lista.
- [ ] A conta deve ser composta por: agência, número da conta e usuário.
- [ ] O número da conta é sequencial, iniciando em 1.
- [ ] O número da agência é fixo: "0001".
- [ ] O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
</details>