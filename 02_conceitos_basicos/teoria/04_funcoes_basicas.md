Funções Básicas
Funções são blocos de código reutilizáveis projetados para realizar uma tarefa específica. Em vez de escrever as mesmas linhas repetidas vezes ao longo do programa, você isola esse trecho dentro de uma função e a executa (invoca) sempre que precisar.

No Python, criamos funções utilizando a palavra reservada def.

1. Definindo e Chamando uma Função
Para criar uma função, usamos def, definimos o seu nome, seguido de parênteses () e dois pontos :. O código pertencente à função deve ficar obrigatoriamente indentado.

```Python
# Definindo a função
def saudar():
    print("Olá! Seja bem-vindo ao Python para Cabeças-Duras.")

# Chamando (executando) a função
saudar()
```
Dessa forma, o código dentro de saudar() só roda no momento em que a função é chamada pelo seu nome.

2. Parâmetros e Argumentos (Entradas)
Parâmetros são as variáveis especificadas dentro dos parênteses da função para receber dados externos. Argumentos são os valores reais passados para a função no momento em que ela é invocada.

```Python
# 'nome' é o parâmetro recebido
def saudar_usuario(nome):
    print(f"Olá, {nome}! Seja bem-vindo.")

# "Ana" e "Carlos" são os argumentos passados
saudar_usuario("Ana")
saudar_usuario("Carlos")
```
Dessa forma, uma única função pode processar dados diferentes dinamicamente a cada execução.

3. Retorno de Valores com return (Saída)
A maioria das funções processa uma informação e precisa devolver um resultado para o programa continuar trabalhando. Para isso, utilizamos a palavra reservada return.

⚠️ Diferença fundamental: O print() apenas exibe um texto na tela para o usuário ver. O return devolve o valor para que o Python possa guardá-lo em uma variável ou usá-lo em outro cálculo.

```Python
# Função que recebe dois números e retorna o resultado da soma
def somar(a, b):
    resultado = a + b
    return resultado

# Guardando o valor devolvido pelo 'return' dentro da variável 'total'
total = somar(5, 3)
print(f"O resultado da soma é: {total}")
Quando o Python executa a linha do return, a função encerra a sua execução imediatamente.
```

4. Escopo de Variáveis (Local vs. Global)
Variáveis criadas dentro de uma função têm escopo local. Isso significa que elas só existem enquanto a função está sendo executada e são apagadas da memória logo em seguida.

```Python
def calcular_desconto(preco):
    desconto = 0.10  # Variável local
    return preco * (1 - desconto)

print(calcular_desconto(100))  # Exibe 90.0
# Se tentar usar 'desconto' fora da função, o Python gera um erro:
# print(desconto)  -> NameError: name 'desconto' is not defined
```
5. Boas Práticas: Documentando com Docstrings
Para manter o repositório dentro dos padrões, orientamos os alunos a documentar o objetivo de cada função logo na primeira linha do seu bloco usando aspas triplas """ (Docstring).

```Python
def converter_celsius_para_fahrenheit(celsius):
    """Recebe uma temperatura em graus Celsius e retorna o valor em Fahrenheit."""
    return (celsius * 9/5) + 32

```
