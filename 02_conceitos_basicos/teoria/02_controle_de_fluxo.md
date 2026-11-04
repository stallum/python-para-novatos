# Controle de Fluxo
Controle de fluxo é a forma de fazer o código executar o que você quer que seja feito. Ou seja, se você quer que em determinado ponto ele verifique uma informação e daí decida entre uma rota e outra, ele seguirá a rota decidida a partir do processamento do dado de entrada.

Essa sequência é realizada pela palavra reservada (estrutura de controle) do Python if e seus complementos, como o else e o elif.

`i` será utilizado como "variável imaginária".

## if
O `if` é a principal estrutura para o controle de fluxo. Nele você joga o poder de decisão de executar um trecho do código a partir de uma condição estabelecida.

```Python
# Exemplo de código com if.
i = 2
print(1)
if i == 2: 
    print(2)
```
Dessa forma, caso o valor de i seja alterado para qualquer outro valor que não seja o inteiro 2, o código apenas exibe o valor 1. O bloco interno é ignorado.

## else
O else é o principal complemento do if, trazendo a lógica do se não. Assim, se a condição do if for verdadeira, o código do if é executado; se não for, o código do else é acionado automaticamente.

```Python
# Exemplo de código com if e else.
i = 2
if i % 2 == 0: 
    print("par")
else: 
    print("impar")
```
Dessa forma, caso o valor de i seja um número ímpar, ele cai no else e exibe "impar". Quando o valor de i for par, o código segue o fluxo do if e exibe "par".

## elif
O `elif` é a contração de "else if" (se não, se). Ele é utilizado quando temos mais de duas opções possíveis, permitindo testar várias condições intermediárias exclusivas antes de o código cair no else final.

```Python
# Exemplo de código com if, elif e else.
i = 0
if i > 0:
    print("positivo")
elif i < 0:
    print("negativo")
else:
    print("zero")
```
Dessa forma, o código testa a primeira condição (if). Se for falsa, testa a segunda (elif). Se todas as condições anteriores forem falsas, ele executa o bloco padrão (else).
