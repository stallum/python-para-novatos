"""
Exemplo de Estrutura de Fluxo Sequencial de Código.
=============================================

Este script realiza a leitura de dois numeros inteiros quaisquer como strings, os transforma em inteiros faz a soma de um com o outro e exibe o seu resultado.

Fluxo de Execução:
1. Define as variáveis.
2. Transforma elas em Inteiro.
3. Soma os valores das varáveis para uma terceira
4. Exibe o resultado da soma.

=============================================
Esse fluxo é chamado Sequencial pois em todas as vezes que esse código rodar, e não houver erros de digitação do usuário, ele será executado de cima a baixo sem desvios em seu fluxo.

=============================================

Para executar esse código, use um terminal nesse diretório e digite o seguinte comando com o python. 
`python 01_logica_e_algoritmos/exemplos/fluxo_sequencial.py`
"""

x = input("digite um numero para o primeiro termo da soma. \n")
y = input("digite um numero para o segundo termo da soma. \n")

x, y = map(int, [x, y])
soma = x + y

print(soma)