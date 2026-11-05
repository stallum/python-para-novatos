# Dicionários
Dicionários são coleções **mutáveis** que armazenam dados no formato de par **chave-valor**. Em vez de acessar elementos por índices numéricos (0, 1, 2...), você acessa os valores através de uma chave única e descritiva (como um dicionário real, onde você busca uma palavra para encontrar a sua definição).

No Python, criamos dicionários utilizando chaves `{}` com pares no formato chave: valor separados por vírgula.

**1. Criando e Acessando Elementos.**
As chaves funcionam como o "endereço" do dado dentro do dicionário. Elas geralmente são textos (strings), mas podem ser qualquer tipo imutável (como números ou tuplas).

```Python
# Criando um dicionario de aluno
aluno = {
    "nome": "Carlos",
    "idade": 20,
    "curso": "Python"
}

# Acessando valores pela chave
print(aluno["nome"])   # Exibe: Carlos
print(aluno["curso"])  # Exibe: Python
```

**2. Acesso Seguro com o Método .get().**
Se você tentar acessar uma chave que não existe usando colchetes (aluno["nota"]), o Python interromperá o programa gerando um erro KeyError. Para evitar falhas, usamos o método .get(), que permite definir um valor padrão de retorno caso a chave não seja encontrada.

```Python
aluno = {"nome": "Carlos", "idade": 20}

# Tentativa insegura: aluno["nota"] -> KeyError

# Forma segura usando .get()
nota = aluno.get("nota", "Não informada")
print(nota)  # Exibe: Não informada
```

**3. Adicionando e Alterando Elementos.**
Dicionários são mutáveis. Para alterar um valor existente ou inserir um novo par chave-valor, basta atribuir o dado à chave correspondente.

```Python
aluno = {"nome": "Carlos", "idade": 20}

# Alterando valor existente
aluno["idade"] = 21

# Adicionando uma nova chave e valor
aluno["matriculado"] = True

print(aluno) 
# Exibe: {'nome': 'Carlos', 'idade': 21, 'matriculado': True}
```
**4. Métodos Principais para Iteração.**
O Python oferece formas fluídas para percorrer e extrair informações de um dicionário:

`keys()`: Retorna todas as chaves do dicionário.

`values()`: Retorna todos os valores armazenados.

`items()`: Retorna os pares (chave, valor) em formato de tuplas.

```Python
produto = {"nome": "Teclado", "preco": 150.0, "estoque": 12}

# Percorrendo apenas as chaves
for chave in produto.keys():
    print(chave)

# Percorrendo chaves e valores juntos (A Forma Pythônica)
for chave, valor in produto.items():
    print(f"{chave}: {valor}")
```

**5. Removendo Elementos.**
Para apagar dados de um dicionário, utilize os métodos:

`pop(chave)`: Remove a chave informada e devolve o seu valor.

`del dicionario[chave]`: Apaga o par chave-valor diretamente da memória.

```Python
aluno = {"nome": "Ana", "idade": 22, "turma": "A"}

# Removendo e salvando a turma em uma variavel
turma_removida = aluno.pop("turma")

print(aluno)           # Exibe: {'nome': 'Ana', 'idade': 22}
print(turma_removida)  # Exibe: A
```
