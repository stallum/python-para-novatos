Os tipos primitivos da maioria das linguagens de programação são relacionandos a tipos boleanos (verdadeiro e falso), numéricos (inteiros e racionais) e textuais (caracteres (em muitas linguagens) e strings), que são estritamentes necessários para a fabricação de programas, por isso, são chamadas primitivas.

Todos os tipos são associados a uma variável qualquer por meio de uma operação básica das linguagem de programação, camada `atribuição` onde, em python, uma variável qualquer (x ou y) recebe um valor qualquer (1 ou "olá") por meio do operando `=`. Dessa forma, temos isso: `x = 3` como uma atribuição válida para a linguagem de programação python. 

## Tipos Numéricos
Os tipos primitivos numéricos conhecidos no python são: os inteiros (int) e os racionais (floats). Esses tipos representam de maneira computacional conjuntos numéricos da matemática conhecida.

Esses tipos são usados para realizar matematica básica, como as 4 operações básicas da matemática (adição, subtração, multiplicação e divisão), e considerar um valor numérico ao criar variáveis com esses tipos estamos assumindo previamente que serão realizadas operações lógicas ou matemáticas com essas variáveis.

Considerando as quatro operações, como devemos fazê-las em `python`?

**Soma.** Feita por meio do operador `+` entre dois numeros sozinhos ou entre duas variáveis numericas quaisquer ou entre uma variável numérica qualquer e um numero, como em:
```
x = 5
y = x +3
print(y)
```
o resultado apresentado é: `8`

**Subtração.** Feita por meio do operador `-` entre dois numeros sozinhos ou entre duas variáveis numericas quaisquer ou entre uma variável numérica qualquer e um numero, como em:
```
y = 6 + 2
x = y - 3
print(x)
```

o resultado apresentado é: `5`

**Multiplicação.** Feita por meio do operador `*` entre dois numeros sozinhos ou entre duas variáveis numericas quaisquer ou entre uma variável numérica qualquer e um numero, como em:
```
x = 3
y = x * 3
print(y)
```

o resultado apresentando é: `9`

**Divisão.** Feita por meio do operador `/` entre dois numeros sozinhos ou entre duas variáveis numericas quaisquer ou entre uma variável numérica qualquer e um numero, como em:
```
x = 81
y = 81 / 27
print(y)
```

o resultado apresentado é: `3`

Ps.: o resultado de uma divisão SEMPRE é um número de tipo `float`.

**Potenciação.** Feita por meio do operador `**` entre dois numeros sozinhos ou entre duas variáveis numericas quaisquer ou entre uma variável numérica qualquer e um numero, como em:
```
x = 2
y = 3 ** x
print(y)
```
o resultado obtido é: `9`

**Divisão de Piso.** Feito por meio do operador `//` entre dois numeros sozinhos ou entre duas variáveis numericas quaisquer ou entre uma variável numérica qualquer e um numero, como em:
```
x = 27
y = 27 // 2
print(y)
```

o resultado obtido é: `13`. Ou seja, o resultado dessa operação é sempre um inteiro IGNORANDO o valor racional depois da virgula, trazendo só o inteiro do resultado.

**Resto de Divisão.** Feito por meio do operador `%` entre dois numeros sozinhos ou entre duas variáveis numericas quaisquer ou entre uma variável numérica qualquer e um numero, retornando o valor do resto obtido pela divisão dos dois operandos às extremidades da operação, como em:
```
x = 53
y = x % 2
print(y)
```

o resultado apresentado é: `1`, já que todo número impar dividido por 2 tem "1" como resto.

## Tipos Textuais
Em python há apenas um tipo primitivo relacionado diretamente a texto, o conhecido como `strings`, uma coleção concatenada[^1] de caractéres, que em python são apenas `strings` concatenadas a `strings`.



[^1]: isso significa associadas