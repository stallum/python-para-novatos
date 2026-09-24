As variáveis são um espaço na memória do computador usado para armazenar e manipular dados que podem mudar durante a execução de um programa.

## O que é uma variável?
- **Uma "caixa".** Pense nela em uma caixa rotulada onde você guarda um valor temporário.

- **Um identificador.** É o nome dado a essa variável para acha-lá facilmente no código.

- **Um dado mutável.** O conteúdo de uma variável pode ser alterado várias vezes enquanto o programa roda.

## Tipos de dados primitivos.
- **Inteiros (`int`).** Guardam numeros inteiros, sem casas decimais, como em quantidade.
- **Decimais (`float` e/ou `double`).** Guardam numeros com casas decimais, como preço ou altura.
- **Textos (`strings`).** Guardam palavras ou frases entre aspas.
- **Caracteres (`char`).** Guardam caracteres unicos, uma lista de caracteres aglomerados forma uma string.
- **Logicos (`boolean`).** Armazenam valores lógicos, `verdadeiro` e `falso`.

## Regras de Definição e uso de Variáveis.
Apesar dessas diferenças, quase todas as linguagens concordam em um conjunto de regras básicas para os nomes (as "etiquetas").

### Nomeação
- **Não utilizar espaços.** É por isso que nome do usuario não funciona. Para resolver isso, usamos padrões como nomeDoUsuario (`camelCase`) ou nome_do_usuario (`snake_case`).
- **Não começam com números.** Um nome como 1ano vai dar erro, mas ano1 é perfeitamente válido.
- **Não usam palavras reservadas.** Cada linguagem tem palavras especiais que usa para seus próprios comandos (`if`, `for`, `while`). Você não pode usar essas palavras como nomes de variáveis.

### Erros lógicos comuns
- **Utilizar antes de declaração.** Ao utilizar uma variável antes de cria-lá é possível, na maioria das linguagens, causar um erro. Em python, por ser uma linguagem dinamicamente tipada, esse erro pode não ser causado imediatamente, o que dificulta o diagnóstico de um possível `bug` no código, tome cuidado ao escrever seu código.
- **Conflito de tipo.** Obviamente é impossível somar um numero a um texto. Mas também, em outras linguagens, não é possível somar um float a um int sem ter um erro, caso não tenha-se a devida mudança de tipo.
-  **Problemas de escopo.** Tentar usar uma variável fora do bloco de código onde ela foi declarada. Por exemplo, usar uma variável criada dentro de uma função, mas lado de fora dela, para saber mais sobre função recomendo essa apostila em python.

## Boas práticas no uso de *Variáveis*

