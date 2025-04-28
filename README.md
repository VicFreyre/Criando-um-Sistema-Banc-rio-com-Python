# Sistema Bancário em Python

Este repositório contém um sistema bancário simples, desenvolvido em Python, com funcionalidades de depósito, saque e extrato. O sistema é voltado para um único usuário e permite realizar depósitos, saques com limite diário e visualizar o extrato da conta.

## Funcionalidades

1. **Depósito**: Permite realizar depósitos de valores positivos. O valor é somado ao saldo e registrado para o extrato.
2. **Saque**: Permite realizar até 3 saques diários, com um limite de R$ 500,00 por saque. Se o saldo for insuficiente ou o limite diário de saques for atingido, uma mensagem de erro será exibida.
3. **Extrato**: Exibe todos os depósitos e saques realizados na conta, além de mostrar o saldo atual.

## Estrutura do Código

A classe principal do sistema é a `ContaBancaria`, que gerencia os depósitos, saques e o saldo da conta. A classe contém os seguintes métodos:

- **`__init__(self)`**: Inicializa a conta bancária com saldo de R$ 0,00, listas para armazenar depósitos e saques, e o contador de saques diários.
- **`depositar(self, valor)`**: Realiza um depósito de valor positivo e adiciona o valor à lista de depósitos.
- **`sacar(self, valor)`**: Permite realizar saques de até R$ 500,00, com limite de 3 saques diários.
- **`extrato(self)`**: Exibe o extrato da conta, mostrando todos os depósitos, saques realizados e o saldo atual.

## Como Usar

1. Clone este repositório para o seu computador:

   ```bash
   git clone https://github.com/seuusuario/repository-name.git
