# Tuplas 
Tuplas são coleções ordenadas de elementos muito semelhantes às listas, mas com uma diferença fundamental: elas são imutáveis. Isso significa que, uma vez criada, você não pode adicionar, remover ou alterar nenhum de seus valores.

No Python, criamos tuplas utilizando parênteses `()` com os elementos separados por vírgula.

**1. Criando e Acessando Elementos.**
Assim como nas listas, cada elemento da tupla possui um índice fixo que começa no zero (0).

```Python
# Criando uma tupla com coordenadas geograficas
coordenadas = (-23.5505, -46.6333)

# Acessando itens pelo índice
print(coordenadas[0])   # Exibe: -23.5505 (latitude)
print(coordenadas[-1])  # Exibe: -46.6333 (longitude)
```
⚠️ Atenção: Se você quiser criar uma tupla de apenas um único elemento, é obrigatório colocar uma vírgula após o valor, caso contrário o Python entenderá como um número ou texto comum entre parênteses: elemento_unico = (10,).

**2. A Imutabilidade na Prática.**
Se você tentar alterar o valor de um índice existente em uma tupla, o Python interromperá a execução e retornará um erro do tipo TypeError.

```Python
cores_rgb = (255, 0, 0)

# Tentativa de alteracao (isso vai gerar erro!):
# cores_rgb[0] = 200  
# TypeError: 'tuple' object does not support item assignment
```
Essa restrição garante que os dados armazenados na tupla permaneçam intactos durante toda a execução do programa.

**3. Desempacotamento de Tuplas (Unpacking).**
O desempacotamento é uma das funcionalidades mais úteis das tuplas. Ele permite atribuir os elementos de uma tupla diretamente a múltiplas variáveis em uma única linha.

```Python
# Criando um registro do usuario (nome, idade, cidade)
usuario = ("Ana", 25, "São Paulo")

# Desempacotando os valores nas variaveis correspondentes
nome, idade, cidade = usuario

print(nome)    # Exibe: Ana
print(idade)   # Exibe: 25
print(cidade)  # Exibe: São Paulo
```

**4. Métodos Principais.**
Por serem imutáveis, as tuplas possuem poucos métodos nativos (não existem métodos como `append(), remove() ou sort()`):

`len(tupla)`: Retorna a quantidade de itens na tupla.

`count(valor)`: Conta quantas vezes um determinado valor aparece dentro da tupla.

`index(valor)`: Retorna a posição (índice) da primeira ocorrência do valor informado.

```Python
respostas = ("sim", "não", "sim", "sim", "não")

print(len(respostas))          # Exibe: 5
print(respostas.count("sim"))  # Exibe: 3
print(respostas.index("não"))  # Exibe: 1 (primeira aparicao)
```

**5. Quando Usar Tuplas em Vez de Listas?**
Em alguns casos é mais vantajoso usar tuplas ao invés de listas como para: 

- Integridade dos Dados: Os dados forem fixos e não puderem ser alterados por engano pelo restante do código (ex: dias da semana, coordenadas, dados de configuração).

- Desempenho: Tuplas consomem menos memória e são levemente mais rápidas para o Python processar do que as listas.
