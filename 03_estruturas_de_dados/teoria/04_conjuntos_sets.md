# Conjuntos, ou Sets
Os Conjuntos (ou Sets) são coleções **mutáveis**, **não ordenadas** e que **não permitem elementos duplicados**. Eles foram implementados no Python baseados diretamente na teoria matemática dos conjuntos.

No Python, criamos conjuntos colocando os elementos entre chaves `{}` ou utilizando a função construtora `set()`.

**1. Criando um Conjunto e a Regra da Unicidade.**
A principal característica de um set é eliminar automaticamente qualquer valor repetido adicionado a ele.

```Python
# Criando um conjunto com valores duplicados
numeros = {1, 2, 2, 3, 4, 4, 4, 5}

print(numeros)  # Exibe: {1, 2, 3, 4, 5} (duplicatas são ignoradas)
```

⚠️ Atenção: Para criar um conjunto vazio, você deve obrigatoriamente usar meu_set = set(). Se usar apenas `{}`, o Python criará um dicionário vazio.

**2. Ausência de Índices.**
Diferente das listas e tuplas, os conjuntos não possuem uma ordem fixa de elementos. Por isso, não é possível acessar valores usando índices (conjunto[0] gerará um erro do tipo TypeError).

```Python
frutas = {"maçã", "banana", "laranja"}

# Tentativa invalida: print(frutas[0]) -> TypeError

# Forma correta de verificar se um item existe no conjunto:
print("banana" in frutas)  # Exibe: True
```

**3. Operações Matemáticas entre Conjuntos.**
A maior utilidade dos sets está na facilidade de realizar operações matemáticas complexas em uma única linha de código:

União (|): Combina todos os elementos de dois conjuntos (sem duplicar).

Interseção (&): Mantém apenas os elementos que estão presentes em ambos os conjuntos.

Diferença (-): Retorna os elementos que estão no primeiro conjunto, mas NÃO no segundo.

Diferença Simétrica (^): Retorna os elementos que estão em um ou no outro, mas NÃO em ambos.

```Python
alunos_python = {"Ana", "Bruno", "Carlos"}
alunos_sql = {"Bruno", "Daniela", "Carlos"}

# Quem cursa Python OU SQL? (União)
print(alunos_python | alunos_sql) 
# Exibe: {'Ana', 'Bruno', 'Carlos', 'Daniela'}

# Quem cursa AMBOS os cursos? (Interseção)
print(alunos_python & alunos_sql) 
# Exibe: {'Bruno', 'Carlos'}

# Quem cursa APENAS Python? (Diferença)
print(alunos_python - alunos_sql) 
# Exibe: {'Ana'}
```

**4. Métodos Principais de Manipulação.**
Para modificar um conjunto durante a execução do programa, utilize:

`add(item)`: Adiciona um elemento ao conjunto (se já não existir).

`remove(item)`: Remove o item especificado. Gera erro se o item não for encontrado.

`discard(item)`: Removes o item especificado de forma segura (NÃO gera erro se o item não existir).

`clear()`: Apaga todos os elementos do conjunto.

```Python
linguagens = {"Python", "C"}

linguagens.add("Java")       # Adiciona 'Java'
linguagens.discard("Ruby")   # Não faz nada e não quebra o código
linguagens.remove("C")       # Remove 'C'

print(linguagens)  # Exibe: {'Python', 'Java'}
```

**5. Quando Usar Sets?**
Sets são úteis, ao meu ver, em duas principais situações:

- Remover duplicatas de listas: Converter uma lista em set e de volta para lista é o atalho mais rápido para limpar dados repetidos (lista_limpa = list(set(lista_suja))).

- Busca ultra-rápida (Pertencimento): Testar se um item está dentro de um set (item in conjunto) é absurdamente mais rápido computacionalmente do que buscar dentro de uma lista grande.
