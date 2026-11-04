# Laços de Repetição (Loops)
Laços de repetição são formas de fazer o código executar o mesmo bloco de instruções múltiplas vezes sem que você precise reescrever as mesmas linhas. Eles poupam tempo e deixam o código dinâmico.

Essa repetição é controlada principalmente por duas estruturas no Python: o `while` e o `for`.

`i` será utilizado novamente como nossa variável de controle.

## while
O `while` (enquanto) funciona como um if contínuo. Ele avalia uma condição e, enquanto essa condição for verdadeira, o código dentro dele continuará sendo executado.

⚠️ Atenção: É obrigatório atualizar o valor da variável de controle dentro do bloco; caso contrário, a condição nunca será falsa e o programa ficará preso em um "loop infinito".

```Python
# Exemplo de código com while.
i = 1
while i <= 3:
    print(i)
    i = i + 1  # Atualiza o valor de i para que o loop tenha um fim
print("Fim do loop")
```
Dessa forma, o código exibirá 1, 2 e 3. Quando i passa a valer 4, a condição i <= 3 se torna falsa. O Python encerra a repetição e segue o fluxo, exibindo "Fim do loop".

## for e range()
O `for` é utilizado quando você já sabe exatamente quantas vezes quer repetir uma ação ou quando precisa percorrer itens de uma sequência. Ele é o laço mais utilizado no Python e frequentemente trabalha em conjunto com a função embutida range(), que gera uma sequência numérica.

```Python
# Exemplo de código com for e range.
for i in range(1, 4):
    print(i)
print("Fim do loop")
```
Dessa forma, a função range(1, 4) gera os números 1, 2 e 3 (o limite final é sempre exclusivo, ou seja, para parar no 3, colocamos 4). A cada volta do laço, o for pega o próximo número da sequência, guarda na variável i e executa o bloco. O resultado na tela é exatamente igual ao do exemplo do while.

## Controlando o fluxo interno: break e continue
Dentro de qualquer laço (while ou for), você pode forçar uma interrupção usando palavras reservadas:

`break`: Quebra (encerra) o laço imediatamente, ignorando qualquer condição restante.

`continue`: Pula o resto do código da volta atual e vai direto para a próxima repetição do laço.

```Python
# Exemplo usando break e continue
for i in range(1, 6):
    if i == 3:
        continue  # Pula o número 3 e vai para o próximo
    
    if i == 5:
        break     # Encerra o laço quando chega no 5
        
    print(i)
```
Dessa forma, o código exibirá o 1 e o 2. Quando i for 3, o continue faz ele pular o print. O 4 é exibido normalmente. Quando chega no 5, o break encerra o laço inteiro antes do print. O resultado final na tela será apenas: 1, 2 e 4.
