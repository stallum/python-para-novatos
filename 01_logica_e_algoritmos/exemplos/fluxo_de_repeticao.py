"""
Exemplo de Estrutura de Fluxo de Repetição de Código.
=============================================

Este script realiza a leitura de sua idade, verifica e exibe SE você é maior OU menor de idade.

Fluxo de Execução:
1. Cria uma lista com 10 termos organizados decrescentemente de 10 a 1.
2. Define i como o primeiro valor da lista
3. Exibe o valor de i
4. Define i como o próximo valor da lista e repete os processos 2, 3 e 4 até o ultimo valor da lista
5. Exibe 0

=============================================
Esse fluxo é chamado de Repteição pois em todas as vezes que esse código rodar ele executar uma mesma linha mais de uma vez.

=============================================

Para executar esse código, use um terminal nesse diretório e digite o seguinte comando com o python. 
`python 01_logica_e_algoritmos/exemplos/fluxo_de_repeticao.py`
"""

for i in range(10, 0, -1): 
    print(i)
print(0)