# Listas
Listas são coleções ordenadas e mutáveis que permitem armazenar múltiplos itens dentro de uma única variável. Elas são a estrutura de dados mais versátil e utilizada no Python para agrupar dados relacionados.

No Python, criamos listas colocando os elementos separados por vírgulas dentro de colchetes `[]`.

**1. Criando e Acessando Elementos.**
Cada item de uma lista possui uma posição fixa chamada índice. No Python, a contagem de índices começa sempre no zero (0).

```Python
# Criando uma lista de frutas
frutas = ["maçã", "banana", "laranja"]

# Acessando itens pelo índice
print(frutas[0])   # Exibe: maçã
print(frutas[-1])  # Exibe: laranja (índices negativos contam do fim para o início)
```
**2. Fatiamento de Listas, ou Slicing.**
Você pode extrair um subconjunto (pedaço) da lista utilizando a sintaxe [início:fim]. Lembramos que o índice de fim é exclusivo.

```Python
numeros = [10, 20, 30, 40, 50]

# Pega do índice 1 até o 3 (o 4 fica de fora)
sub_lista = numeros[1:4]
print(sub_lista)  # Exibe: [20, 30, 40]
```
**3. Alterando a lista.**
Listas são mutáveis, o que significa que você pode alterar o valor de um elemento existente sem precisar recriar a lista.

```Python
frutas = ["maçã", "banana", "laranja"]
frutas[1] = "uva"  # Substitui 'banana' por 'uva'

print(frutas)  # Exibe: ['maçã', 'uva', 'laranja']
```
**4. Métodos Principais de Manipulação.**
O Python oferece métodos nativos na própria estrutura da lista para adicionar, remover e organizar elementos:

`len(lista)`: Função nativa que devolve a quantidade total de itens na lista.

`append(item)`: Adiciona um novo elemento ao final da lista.

`insert(indice, item)`: Insere um elemento em uma posição específica, deslocando os demais.

`remove(valor)`: Remove a primeira ocorrência do valor especificado.

`pop(indice)`: Remove e devolve o item do índice informado (se nenhum índice for passado, remove o último item).

`sort()`: Ordena a lista em ordem crescente (ou alfabética).

```Python
numeros = [3, 1, 4]

numeros.append(2)       # [3, 1, 4, 2]
numeros.insert(0, 5)    # [5, 3, 1, 4, 2]
numeros.remove(3)       # [5, 1, 4, 2]
ultimo = numeros.pop()  # Remove o 2 e guarda em 'ultimo'
numeros.sort()     Mutabilidade     # Ordena os restantes: [1, 4, 5]

print(numeros)          # Exibe: [1, 4, 5]
print(f"Tamanho da lista: {len(numeros)}") # Exibe: 3
```
**5. Percorrendo uma Lista de forma "Pythônica".** 
A maneira correta e mais legível de iterar sobre uma lista no Python é usando o laço for diretamente nos elementos, sem usar índices manuais.

```Python
compras = ["pão", "leite", "café"]

# Maneira recomendada (direta no item)
for item in compras:
    print(f"Comprar: {item}")
```

Dessa forma, o código fica limpo, legível e evita erros de "índice fora dos limites" (IndexError).
