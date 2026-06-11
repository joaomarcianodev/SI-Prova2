# Sistema de Criptografia Assimétrica (RSA) do Zero

Este projeto implementa um sistema de cifragem e decifragem baseado em **Criptografia Assimétrica**, focando no protocolo RSA (Rivest-Shamir-Adleman). O código foi desenvolvido inteiramente do zero, em Python, sem a importação de bibliotecas prontas de criptografia.

## 1. Fundamentação Teórica

Segundo os pilares da Segurança da Informação, o objetivo da criptografia em sistemas como este é garantir a **Confidencialidade**, de forma que "os recursos do sistema só podem ser lidos por usuários autorizados" (detentores da chave correta).

A abordagem utilizada é a **criptografia assimétrica**, na qual "emissor e receptor utilizam chaves diferentes". O algoritmo RSA também respeita o princípio de segurança de **Projeto Aberto**, em que o algoritmo é público e amplamente conhecido e avaliado por terceiros, fazendo a segurança repousar inteiramente sobre o sigilo matemático das chaves geradas.

### 1.1 Aritmética Modular e Números Primos no RSA

A segurança do RSA baseia-se na dificuldade computacional de fatorar produtos de números primos grandes. O ciclo de vida da segurança assimétrica implementado neste software segue os passos:

1. **Geração de Números Primos:** O sistema escolhe dois números primos grandes, `p` e `q`.
2. **Cálculo do Módulo (n) e do Totiente de Euler (φ):**
   - Calcula-se `n = p * q`. Este será o módulo usado em ambas as chaves.
   - O Totiente de Euler, que contabiliza os inteiros positivos menores ou iguais a `n` que são coprimos com `n`, é calculado por `φ(n) = (p-1) * (q-1)`.
3. **Expoente de Cifragem (e):** Um número aleatório `e` é escolhido de modo que $1 < e < φ(n)$ e que o Máximo Divisor Comum (MDC) entre `e` e `φ(n)` seja 1 (ou seja, são coprimos).
4. **Expoente de Decifragem (d):** Encontrado através do **Algoritmo de Euclides Estendido**, `d` é o inverso modular de `e`. Matematicamente, satisfaz a equação: `(d * e) mod φ(n) = 1`.

### 1.2 Processo de Cifragem e Decifragem

Para cifrar, os caracteres de texto são convertidos para números reais (usando tabela ASCII) para se adequarem à aritmética modular.

- **Cifragem:** O texto claro `m` é convertido no texto cifrado `c` usando a Chave Pública `(e, n)`: $c = m^e \pmod n$.
- **Decifragem:** O texto cifrado `c` volta ao texto original `m` usando a Chave Privada `(d, n)`: $m = c^d \pmod n$.

## 2. Requisitos e Execução

- **Linguagem:** Python 3.x
- **Bibliotecas:** Nenhuma dependência externa necessária (usa-se apenas a biblioteca nativa `random`).

### Como executar:

1. Abra o terminal na pasta do projeto.
2. Execute o comando: `python rsa_algoritmo.py`
3. O sistema gerará as chaves automaticamente na tela.
4. Digite uma mensagem de teste quando solicitado.
5. O sistema exibirá o array numérico correspondente à mensagem cifrada.
6. Em seguida, o sistema utilizará a chave privada para comprovar a recuperação total da mensagem.

## 3. Validação (Vídeo)

O vídeo demonstrando o funcionamento e a geração correta das chaves, encontra-se disponível no link abaixo:

[Link do vídeo](https://youtu.be/DmyuQ9TCE_I)
