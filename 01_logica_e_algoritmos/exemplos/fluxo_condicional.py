"""
Exemplo de Estrutura de Fluxo Condicional de Código.
=============================================

Este script realiza a leitura de sua idade, verifica e exibe SE você é maior OU menor de idade.

Fluxo de Execução:
1. Define a idade como inteiro.
2. Verifica se a idade é maior ou menor que 18 anos
4. Exibe se você é maior ou menor de idade.

=============================================
Esse fluxo é chamado Condicional pois em todas as vezes que esse código rodar ele vai receber a entrada, processala verificando se essa entrada é maior ou menor que 18 e depois terá uma das duas saídas possíveis.

=============================================

Para executar esse código, use um terminal nesse diretório e digite o seguinte comando com o python. 
`python 01_logica_e_algoritmos/exemplos/fluxo_condicional.py`
"""

idade = int(input("Digite o numero que representa sua idade em anos."))

if idade >= 18: 
    print("você é maior de idade.")
else: 
    print("você é menor de idade.")
